from flask import Flask, jsonify
import requests
import threading 
import time

app = Flask(__name__)

data_lock = threading.Lock()
airplane_data = {}

def update_data():
    try:
        response = requests.get("https://api.aviationstack.com/v1/flights?access_key=3674ce3a0d73ecc8fece652e092c9237")
        if response.status_code == 200:
            data = response.json()
            with data.lock:
                airplane_data.clear()
                airplane_data.update(data)
            print("Airplane data updated")
        else: 
            print("Failed to fetch data.", response.status_code)
    except Exception as e:
        print("Error during update", e)

    time.sleep(60)

@app.route("/airplane")
def get_airplane_data():
    with data_lock:
        return jsonify(airplane_data) 

if __name__ == "__main__":
    updater_thread = threading.Thread(targer=update_data, daemon=True)
    updater_thread.start()

    app.run(debug=True)

