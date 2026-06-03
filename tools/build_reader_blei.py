#!/usr/bin/env python3
"""Build the reader payload (paper sections + narration audio + sync map) for the
Blei VI review — slice 1 of the PKIS read+listen tool.

Run on the VPS:  python3 build_reader_blei.py
Env: PIPER=/path/to/piper  PIPER_MODEL=/path/to/voice.onnx  OUTDIR=/home/pkis/pkis-wiki/wiki/reader/blei-vi-review
Needs: piper, ffmpeg, ffprobe on PATH.
"""
import os, json, subprocess, tempfile, shutil

SLUG = "blei-vi-review"
TITLE = "Variational Inference: A Review for Statisticians"

# Each section: paper_md = the ACTUAL paper content shown on screen (prose + $LaTeX$);
# narration = the spoken track (hybrid: prose kept, math translated, sparse highlights,
# + PKIS-consolidation callouts). narration is TTS'd; paper_md is read on screen.
SECTIONS = [
    {
        "id": "s1",
        "title": "1 · Introduction",
        "paper_md": (
            "One of the core problems of modern statistics is to approximate "
            "difficult-to-compute probability densities. This is especially central in "
            "Bayesian statistics, which frames all inference about unknown quantities as a "
            "computation involving the posterior.\n\n"
            "This paper reviews **variational inference (VI)**, which approximates "
            "probability densities through *optimization*. Posit a family $\\mathcal{Q}$ of "
            "densities over the latent variables, then find the member closest to the target "
            "posterior, where closeness is measured by Kullback–Leibler divergence.\n\n"
            "Compared with MCMC: MCMC produces (asymptotically) exact samples but can be "
            "computationally intensive; VI tends to be faster and easier to scale, but only "
            "finds a density *close* to the target. VI suits large data and quickly exploring "
            "many models; MCMC suits smaller data where one pays a heavier cost for precision."
        ),
        "narration": (
            "Here's the problem this whole paper is organized around. In modern Bayesian "
            "statistics, almost everything you want to know lives in a posterior distribution, "
            "and that posterior is usually impossible to compute directly. The field has two "
            "big strategies. The first is Markov chain Monte Carlo, which samples from the "
            "posterior; given enough time it's asymptotically exact, but it can be slow. This "
            "paper is about the second strategy, variational inference, which doesn't sample at "
            "all. It turns inference into optimization: propose a family of simpler "
            "distributions, then find the member closest to the true posterior. The payoff is "
            "speed and scalability; the price is that you only ever get close, never exact. So "
            "the rule of thumb to carry through the paper is: variational inference for large "
            "data and fast model exploration, M-C-M-C when the dataset is small and you'll "
            "happily pay for precision. "
            "One connection to your own knowledge base: this exact framing is already a node "
            "you made, your bridge note titled, alternative inference engines for latent "
            "variable models. Keep that note in view as you read, because the paper is really "
            "the long-form version of the connection you already drew."
        ),
    },
    {
        "id": "s21",
        "title": "2.1 · The problem of approximate inference",
        "paper_md": (
            "Let $\\mathbf{x}=x_{1:n}$ be observations and $\\mathbf{z}=z_{1:m}$ the latent "
            "variables, with joint density $p(\\mathbf{z},\\mathbf{x})$. Inference requires the "
            "posterior\n\n"
            "$$p(\\mathbf{z}\\mid\\mathbf{x}) = \\frac{p(\\mathbf{z},\\mathbf{x})}{p(\\mathbf{x})}.$$\n\n"
            "The denominator is the **evidence** (marginal likelihood), "
            "$p(\\mathbf{x}) = \\int p(\\mathbf{z},\\mathbf{x})\\,d\\mathbf{z}$, which for many "
            "models has no closed form or requires exponential time. Variational inference "
            "instead posits a family $\\mathcal{Q}$ and solves\n\n"
            "$$q^*(\\mathbf{z}) = \\arg\\min_{q(\\mathbf{z})\\in\\mathcal{Q}} "
            "\\mathrm{KL}\\!\\left(q(\\mathbf{z})\\,\\|\\,p(\\mathbf{z}\\mid\\mathbf{x})\\right)."
            "$$"
        ),
        "narration": (
            "Let's make the problem precise. We have observations x and hidden variables z, and "
            "a model that gives us their joint distribution. What we want is the posterior, the "
            "latents given the data, which by definition is that joint divided by the evidence, "
            "p of x. And there's the whole difficulty in one symbol: the evidence is the joint "
            "integrated over every configuration of the latent variables. For most interesting "
            "models that integral has no closed form, or would take exponential time. The "
            "running example makes this visceral. In a Bayesian mixture of Gaussians, computing "
            "the evidence means summing over every possible assignment of every data point to "
            "every cluster, K to the n configurations, exponential. So the move of variational "
            "inference is to stop trying to compute the posterior, and instead approximate it: "
            "pick a family of candidate distributions, and search for the one closest to the "
            "true posterior in K-L divergence. We've turned an intractable integral into a "
            "tractable optimization. "
            "And this is literally your Intractable Posterior Inference problem card, which "
            "you've already covered fairly well. The paper is handing you the canonical "
            "statement of a problem that's already central in your graph."
        ),
    },
    {
        "id": "s22",
        "title": "2.2 · The evidence lower bound",
        "paper_md": (
            "We cannot directly minimize $\\mathrm{KL}(q\\|p(\\mathbf{z}\\mid\\mathbf{x}))$ "
            "because it depends on $\\log p(\\mathbf{x})$. Instead we optimize the **evidence "
            "lower bound (ELBO)**,\n\n"
            "$$\\mathrm{ELBO}(q) = \\mathbb{E}\\!\\left[\\log p(\\mathbf{z},\\mathbf{x})\\right] "
            "- \\mathbb{E}\\!\\left[\\log q(\\mathbf{z})\\right],$$\n\n"
            "which is equivalent to the KL up to an additive constant. Indeed "
            "$\\log p(\\mathbf{x}) = \\mathrm{KL}(q\\|p(\\mathbf{z}\\mid\\mathbf{x})) + "
            "\\mathrm{ELBO}(q)$, so $\\mathrm{ELBO}(q)\\le \\log p(\\mathbf{x})$. A useful "
            "rewriting is\n\n"
            "$$\\mathrm{ELBO}(q) = \\mathbb{E}[\\log p(\\mathbf{x}\\mid\\mathbf{z})] - "
            "\\mathrm{KL}(q(\\mathbf{z})\\|p(\\mathbf{z})).$$\n\n"
            "The first term is the expected complete log-likelihood (optimized by the EM "
            "algorithm); the second keeps $q$ near the prior."
        ),
        "narration": (
            "But there's an immediate catch, and watching how the paper escapes it is the key "
            "idea. We just said: minimize the K-L divergence from q to the true posterior. We "
            "can't, because that divergence contains the very posterior we can't compute. So "
            "here's the trick. Write down the log evidence, and it splits exactly into two "
            "pieces: the K-L divergence we wanted to minimize, plus a second quantity called the "
            "ELBO, the evidence lower bound. Now, the evidence is a fixed constant, and K-L "
            "divergence is never negative. Those two facts together mean that pushing the ELBO "
            "up is identical to pushing that unreachable divergence down. We optimize the thing "
            "we can compute, and it does our intended job for free. That's why it's a lower "
            "bound: the ELBO always sits below the log evidence, and the gap is exactly the "
            "error of our approximation. There's a second reading worth holding onto: the ELBO "
            "also equals the expected log likelihood of the data minus the divergence between q "
            "and the prior. A tug of war, fit the data but stay near the prior. "
            "Now, hold onto the ELBO as a portable object, not a detail of this one paper, and "
            "your own knowledge base proves the point: your Variational Autoencoder card is "
            "trained by maximizing the ELBO, and your Stochastic V-I card scales the same bound. "
            "So this isn't one technique, it's the hinge connecting several things you already "
            "track. And that first term, the expected complete log likelihood, is exactly what "
            "your E-M algorithm card's M-step maximizes, which is precisely the E-M to V-I edge "
            "in that bridge note."
        ),
    },
    {
        "id": "s23",
        "title": "2.3 · The mean-field variational family",
        "paper_md": (
            "A common choice for $\\mathcal{Q}$ is the **mean-field family**, in which the "
            "latent variables are mutually independent:\n\n"
            "$$q(\\mathbf{z}) = \\prod_{j=1}^{m} q_j(z_j).$$\n\n"
            "This family cannot capture correlation between latent variables, but each factor "
            "$q_j$ can take any form. The independence assumption is what makes the ELBO "
            "tractable to optimize one coordinate at a time."
        ),
        "narration": (
            "The ELBO tells us what to maximize; now we have to choose the family we maximize "
            "over, and that choice is a direct tradeoff between tractability and fidelity. The "
            "standard choice is the mean-field family: assume every latent variable is "
            "independent, so q factorizes into a separate piece per variable. Be clear-eyed "
            "about what that buys and costs. It costs you correlation. A mean-field q literally "
            "cannot represent any dependence between latent variables, so if the true posterior "
            "has strong correlations, you'll miss them. What it buys is everything that follows: "
            "because the variables decouple, the ELBO becomes optimizable one coordinate at a "
            "time, each with a clean closed-form update. Note what it does not restrict: each "
            "individual factor can take any shape it needs; it's only the joint structure we've "
            "simplified. "
            "This is your Mean-Field Variational Approximation card, and here's the "
            "consolidation worth pausing on: your card already flags this exact tradeoff, that "
            "the independence assumption buys tractability but systematically underestimates "
            "posterior variance. The paper is confirming a principle you'd already distilled. "
            "That's the moment to bump that card from noted to understood."
        ),
    },
    {
        "id": "s24",
        "title": "2.4 · Coordinate ascent (CAVI)",
        "paper_md": (
            "**Coordinate ascent variational inference (CAVI)** optimizes the mean-field ELBO "
            "by updating each factor in turn, holding the others fixed. The optimal update is\n\n"
            "$$q_j^*(z_j) \\;\\propto\\; \\exp\\!\\left\\{ \\mathbb{E}_{-j}\\!\\left[ "
            "\\log p(z_j \\mid \\mathbf{z}_{-j}, \\mathbf{x}) \\right] \\right\\} \\;\\propto\\; "
            "\\exp\\!\\left\\{ \\mathbb{E}_{-j}\\!\\left[ \\log p(z_j, \\mathbf{z}_{-j}, "
            "\\mathbf{x}) \\right] \\right\\}.$$\n\n"
            "CAVI climbs the ELBO to a local optimum. It is closely related to Gibbs sampling: "
            "both use the complete conditional, but CAVI takes its expected log rather than a "
            "sample."
        ),
        "narration": (
            "Now the algorithm, and this is the part worth really understanding, not just the "
            "formula but why it's forced. We optimize the mean-field ELBO by coordinate ascent: "
            "freeze every factor but one, update that one to its optimum, cycle, repeat. The "
            "optimal update for a single factor is proportional to the exponential of the "
            "expected log complete conditional. Take the conditional of that variable given all "
            "the others and the data, average its log over your current estimates of the other "
            "variables, and exponentiate. That looks arbitrary until you see where it comes "
            "from. If you hold everything else fixed, the part of the ELBO that depends on this "
            "one factor is, up to a constant, the negative K-L divergence between the factor and "
            "exactly that exp-of-expected-log distribution. And negative divergence is maximized "
            "when the two are equal. So the update isn't a trick pulled from a hat; it's just, "
            "set this factor equal to the thing the objective was secretly measuring distance "
            "to. The form is forced. "
            "This is your Coordinate Ascent V-I card, currently your most lightly held node in "
            "this arc, so this is the section to deepen. And the family resemblance closes the "
            "loop back to your bridge note: this is the same complete conditional that Gibbs "
            "sampling uses. Gibbs draws a sample from it, C-A-V-I takes its expected log, E-M "
            "point-estimates. Three relatives of one idea, which is exactly what alternative "
            "inference engines for the same latent variable model was pointing at. The paper "
            "just earned that bridge note."
        ),
    },
]


import wave


def wav_duration(path):
    with wave.open(path, "rb") as w:
        return w.getnframes() / float(w.getframerate())


def concat_wavs(wav_paths, out_path):
    """Concatenate same-format WAVs into one (no ffmpeg needed; piper outputs are uniform)."""
    with wave.open(wav_paths[0], "rb") as w0:
        params = w0.getparams()
    with wave.open(out_path, "wb") as out:
        out.setparams(params)
        for p in wav_paths:
            with wave.open(p, "rb") as w:
                out.writeframes(w.readframes(w.getnframes()))


def main():
    piper = os.environ.get("PIPER", "piper")
    model = os.environ["PIPER_MODEL"]
    outdir = os.environ.get("OUTDIR", f"/home/pkis/pkis-wiki/wiki/reader/{SLUG}")
    os.makedirs(outdir, exist_ok=True)
    tmp = tempfile.mkdtemp()
    wavs, sections_meta, t = [], [], 0.0
    try:
        for s in SECTIONS:
            wav = os.path.join(tmp, f"{s['id']}.wav")
            # piper reads text on stdin, writes a wav
            p = subprocess.run([piper, "--model", model, "--output_file", wav],
                               input=s["narration"], text=True, capture_output=True)
            if p.returncode != 0:
                raise RuntimeError(f"piper failed on {s['id']}: {p.stderr[:400]}")
            d = wav_duration(wav)
            wavs.append(wav)
            sections_meta.append({
                "id": s["id"], "title": s["title"], "paper_md": s["paper_md"],
                "narration": s["narration"],
                "t_start": round(t, 2), "t_end": round(t + d, 2),
            })
            t += d
            print(f"  {s['id']}: {d:.1f}s  (->{t:.1f}s)")
        # concat wavs -> single wav (no ffmpeg)
        audio_path = os.path.join(outdir, "audio.wav")
        concat_wavs(wavs, audio_path)
        payload = {
            "slug": SLUG, "title": TITLE,
            "source_iri": f"pkis:source:{SLUG}",
            "audio_url": f"/pkis-api/reader/{SLUG}/audio.wav",
            "total_duration": round(t, 2),
            "sections": sections_meta,
        }
        with open(os.path.join(outdir, "payload.json"), "w") as f:
            json.dump(payload, f, indent=2)
        print(f"DONE: {outdir}  ({t:.1f}s audio, {len(sections_meta)} sections)")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
