from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route("/iot")
#http://127.0.0.1:5000/iot
def iot():
    # ThingSpeak Channel 9: MathWorks Weather Station
    url = "https://api.thingspeak.com/channels/9/feeds.json?results=10"

    try:
        response = requests.get(url)
        # Raise an error if the HTTP status code is bad (e.g., 404 or 500)
        response.raise_for_status()

        data = response.json()

        # Check if 'feeds' key exists to avoid KeyError
        if "feeds" in data:
            return jsonify(data["feeds"])
        else:
            return jsonify({"error": "Unexpected data format from ThingSpeak"}), 502

    except requests.exceptions.RequestException as e:
        # Handle connection errors (DNS, Timeout, etc.)
        return jsonify({"error": str(e)}), 503


if __name__ == "__main__":
    app.run(debug=True, port=5000)