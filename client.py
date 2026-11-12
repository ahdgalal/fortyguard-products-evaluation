import json
import os
import pathlib
import time

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ["FORTYGUARD_API_KEY"]

# Step 1: Submit request
submit_url = "https://api.fortyguard.com/v1/heatmap"

headers = {"api-key": api_key, "Content-Type": "application/json"}
payload = {
    "polygon_aoi": {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [-112.0783, 33.4448],
                            [-112.0697, 33.4448],
                            [-112.0697, 33.4520],
                            [-112.0783, 33.4520],
                            [-112.0783, 33.4448],
                        ]
                    ],
                },
            }
        ],
    },
    "date_time": {"start_date": "2026-07-10", "start_time": "14:00", "filter_type": 1},
    "granularity": 100,
}

start = time.time()

response = requests.post(submit_url, headers=headers, json=payload)
print("Submit status code:", response.status_code)
print("-" * 50)
print(payload["date_time"])
print(response.text)

activity_id = response.json()["data"]["activity_id"]
print(f"Task submitted. Activity ID: {activity_id}")


# Step 2: Check task status
status_url = f"https://api.fortyguard.com/v1/status/{activity_id}"

result = None

for _ in range(120):
    status_response = requests.get(status_url, headers=headers)

    if status_response.status_code == 404:
        time.sleep(5)
        continue

    status_data = status_response.json()["data"]
    status = status_data["status"].lower()

    if status in ("completed", "succeeded"):
        print("Task completed successfully!")
        result = status_response.json()
        break
    elif status in ("failed", "error"):
        result = status_response.json()
        print("Task failed.")
        break
    else:
        print("Task is still processing...")
        time.sleep(5)
else:
    print("Task did not complete in time.")


# Report
name = "phoenix_heatmap"
pathlib.Path("tests").mkdir(exist_ok=True)
record = {
    "name": name,
    "request": payload,
    "submit_status": response.status_code,
    "activity_id": activity_id,
    "seconds": round(time.time() - start, 1),
    "result": result,
}
pathlib.Path(f"tests/{name}.json").write_text(json.dumps(record, indent=2))
print(f"Time taken {record['seconds']} seconds")
