# API Quickstart

AIMoCap uses an asynchronous API flow:

1. Create a job.
2. Upload the source video.
3. Complete upload admission.
4. Poll until the job reaches a final state.
5. Read the result and download outputs.

Public base URL:

```text
https://aimocap.net
```

Public target IDs:

```text
default
unitree_g1
```

See `examples/python` for a minimal end-to-end example.
