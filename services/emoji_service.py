import time
import os

# CALL TEXT-TO-EMOJI MICRO-SERVICE (BIG POOL)
REQUEST_FILE = "../Ethan-s-Emoji-Micro-Service/request.txt"
RESPONSE_FILE = "../Ethan-s-Emoji-Micro-Service/response.txt"

def get_emoji(keyword: str):
    """
    Sends a keyword to the emoji microservice and returns the emoji response.
    If no emoji is found, returns "" (empty string) so UI stays clean.
    """

    # Clear previous response
    with open(RESPONSE_FILE, "w") as f:
        f.write("")

    # Send request
    with open(REQUEST_FILE, "w") as f:
        f.write(keyword)

    # Wait for response (up to 10 seconds)
    for i in range(20):
        time.sleep(0.5)

        if os.path.exists(RESPONSE_FILE):
            with open(RESPONSE_FILE, "r", encoding="utf-8") as f:
                response = f.read().strip()

            if response:
                # Clear request after reading
                with open(REQUEST_FILE, "w") as f:
                    f.write("")
                return response if not response.startswith("ERROR") else ""

    return ""  # fallback if no response
