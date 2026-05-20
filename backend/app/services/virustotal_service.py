import os
import requests
import base64

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("VIRUSTOTAL_API_KEY")


def check_virustotal(url):

    headers = {
        "x-apikey": API_KEY
    }

    url_id = base64.urlsafe_b64encode(
        url.encode()
    ).decode().strip("=")

    endpoint = f"https://www.virustotal.com/api/v3/urls/{url_id}"

    response = requests.get(
        endpoint,
        headers=headers
    )

    if response.status_code != 200:
        return {
            "malicious": 0,
            "suspicious": 0
        }

    data = response.json()

    stats = data["data"]["attributes"]["last_analysis_stats"]

    return {
        "malicious": stats.get("malicious", 0),
        "suspicious": stats.get("suspicious", 0)
    }

