# AIMoCap Video2Motion

AI video mocap from short video to animation-ready FBX and Unitree G1 robot
motion output.

<p>
  <a href="https://animatex.github.io/aimocap"><strong>Project Page</strong></a>
  ·
  <a href="https://huggingface.co/spaces/animatex/aimocap"><strong>HF Space</strong></a>
  ·
  <a href="https://aimocap.net"><strong>AIMoCap Studio</strong></a>
  ·
  <a href="https://aimocap.net/docs"><strong>Docs</strong></a>
</p>

![AIMoCap demo poster](assets/hero-video-poster.jpg)

## What It Does

AIMoCap is a browser-first Video2Motion workflow for teams that want to turn a
clean source video into motion files that can move downstream.

- Generate humanoid FBX motion for animation review and cleanup.
- Produce Unitree G1 robot motion JSON from the same video workflow.
- Use a hosted Studio for upload, trim, target selection, review, and download.
- Try a public demo path before integrating the API into production tools.

## Demo Gallery

| Demo | Output | Try |
| --- | --- | --- |
| Video to humanoid motion | FBX animation output | [Project page](https://animatex.github.io/aimocap) |
| Video to Unitree G1 motion | Robot motion JSON | [HF Space](https://huggingface.co/spaces/animatex/aimocap) |
| Multi-target review | One clip, multiple targets | [AIMoCap Studio](https://aimocap.net) |

## Where AIMoCap Fits

| Approach | Input | Output | Best fit |
| --- | --- | --- | --- |
| Pose estimation repos | Image or video | Keypoints | Research, analysis, model building |
| Traditional mocap | Capture stage | High quality motion | Studio capture sessions |
| AIMoCap | Short video | FBX and robot motion | Fast review, animation delivery, robot motion collection |

## Quick API Shape

The public API is asynchronous:

1. Create a mocap job.
2. Upload the source video.
3. Complete upload admission.
4. Poll job status.
5. Download finished outputs.

See [examples/python](examples/python) for a minimal Python example.

## Public Repository Scope

This repository is a public entry point for AIMoCap. It includes docs, examples,
demo links, and output format notes.

It does not include hosted service source, production processing code, account
systems, storage adapters, billing systems, private model assets, or deployment
configuration.

## Links

- Project page: https://animatex.github.io/aimocap
- Website: https://aimocap.net
- API docs: https://aimocap.net/docs/api-overview
- Output formats: [examples/output-formats](examples/output-formats)
- Roadmap: [docs/open-source-roadmap.md](docs/open-source-roadmap.md)
