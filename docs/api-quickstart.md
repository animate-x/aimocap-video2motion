# API Quickstart

AIMoCap uses an asynchronous video-to-motion job flow. The public examples
describe the request and response shape used by client integrations.

## Base URL

```text
https://aimocap.net
```

## Public Target IDs

| Target ID | Output | Notes |
| --- | --- | --- |
| `default` | FBX | Humanoid animation output |
| `unitree_g1` | motion JSON | Unitree G1-oriented motion output |

## Job Lifecycle

1. Create a mocap job with source metadata and target IDs.
2. Upload the source video using the returned upload URL.
3. Complete upload admission for the job.
4. Poll until the job reaches `completed`, `failed`, or `canceled`.
5. Read the result object and download target-specific outputs.

## Minimal Create Payload

```json
{
  "title": "walk-cycle",
  "sourceFilename": "walk.mp4",
  "targetIds": ["default", "unitree_g1"],
  "exportFps": 30
}
```

## Status Model

| Status | Meaning |
| --- | --- |
| `queued` | Job has been accepted and is waiting to run |
| `processing` | Motion generation is in progress |
| `completed` | Result metadata and outputs are available |
| `failed` | Job did not complete successfully |
| `canceled` | Job was canceled before completion |

See [examples/python](../examples/python) for a minimal end-to-end example.
