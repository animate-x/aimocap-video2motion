import os
import sys
import time
from pathlib import Path

import requests


BASE_URL = "https://aimocap.net"


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python submit_mocap_job.py path/to/source.mp4")

    source_path = Path(sys.argv[1])
    if not source_path.exists():
        raise SystemExit(f"File not found: {source_path}")

    api_key = os.environ.get("AIMOCAP_KEY", "").strip()
    if not api_key:
        raise SystemExit("Set AIMOCAP_KEY before running this example.")

    headers = {"Authorization": f"Bearer {api_key}"}
    create_payload = {
        "title": source_path.stem,
        "sourceFilename": source_path.name,
        "targetIds": ["default", "unitree_g1"],
        "exportFps": 30,
    }

    create_response = requests.post(
        f"{BASE_URL}/api/v1/mocap/jobs",
        json=create_payload,
        headers=headers,
        timeout=30,
    )
    create_response.raise_for_status()
    create_data = create_response.json()["data"]

    with source_path.open("rb") as source_file:
        upload_response = requests.put(
            create_data["uploadUrl"],
            data=source_file,
            headers={"Content-Type": "video/mp4"},
            timeout=120,
        )
    upload_response.raise_for_status()

    complete_response = requests.post(
        f"{BASE_URL}/api/v1/mocap/jobs/{create_data['jobId']}/complete-upload",
        headers=headers,
        timeout=30,
    )
    complete_response.raise_for_status()

    while True:
        job_response = requests.get(
            f"{BASE_URL}/api/v1/mocap/jobs/{create_data['jobId']}",
            headers=headers,
            timeout=30,
        )
        job_response.raise_for_status()
        job_data = job_response.json()["data"]
        status = job_data["job"]["status"]
        print("status:", status)
        if status in {"completed", "failed", "canceled"}:
            break
        time.sleep(5)

    result_response = requests.get(
        f"{BASE_URL}/api/v1/mocap/jobs/{create_data['jobId']}/result",
        headers=headers,
        timeout=30,
    )
    result_response.raise_for_status()
    result = result_response.json()["data"]

    print("preview:", result.get("previewVideoUrl"))
    for output in result.get("outputs", []):
        url = output.get("fbxUrl") or output.get("motionJsonUrl")
        print(output["targetId"], output["resultType"], url)


if __name__ == "__main__":
    main()
