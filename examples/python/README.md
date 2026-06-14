# Python Example

This example shows the public asynchronous AIMoCap API shape.

Set an environment variable before running:

```bash
export AIMOCAP_KEY="your_public_api_key"
```

Run:

```bash
python submit_mocap_job.py path/to/source.mp4
```

The script demonstrates:

- creating a mocap job
- uploading the source video
- completing upload admission
- polling job status
- printing preview and output URLs

The example uses a placeholder public API key environment variable. Do not put
real keys in source control.
