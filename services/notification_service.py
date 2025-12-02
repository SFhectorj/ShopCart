import json
import time
import os

# CALL NOTIFICATION SERVICE (BIG POOL)
REQUEST_FILE = "../notification_microservice/notification_requests.json"
RESPONSE_FILE = "../notification_microservice/notification_responses.json"
DEFAULT_TIMEOUT = 10.0
POLL_INTERVAL = 0.2


def send_notification(status="success", message="No message provided.", include_status=True, timeout=DEFAULT_TIMEOUT):
    request_payload = [{
        "operation": "SEND",
        "data": {
            "status": status,
            "message": message,
            "include_status": include_status
        }
    }]

    req_dir = os.path.dirname(REQUEST_FILE) or "."
    os.makedirs(req_dir, exist_ok=True)

    try:
        with open(REQUEST_FILE, "w") as f:
            json.dump(request_payload, f, indent=2)
    except Exception as e:
        return f"[ERROR] Failed to write notification request: {e}"

    elapsed = 0.0
    while elapsed < timeout:
        try:
            if os.path.exists(RESPONSE_FILE):
                with open(RESPONSE_FILE, "r") as f:
                    try:
                        responses = json.load(f)
                    except json.JSONDecodeError:
                        responses = []

                if responses:
                    try:
                        with open(RESPONSE_FILE, "w") as fr:
                            json.dump([], fr)
                    except Exception:
                        pass

                    first = responses[0]
                    return first.get("message", "[ERROR] Invalid response format")
        except Exception:
            pass

        time.sleep(POLL_INTERVAL)
        elapsed += POLL_INTERVAL

    return f"[ERROR] Notification service did not respond within {timeout} seconds."
