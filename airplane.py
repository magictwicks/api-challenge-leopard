from flask import Flask
import requests
import threading 
import time

app = Flask(__name__)

@app.route("/")
def home():
    return ""

def update_data():
    while True: # run forever
        try: 
            data = requests.get("https://api.aviationstack.com/v1/flights
    ? access_key = 3674ce3a0d73ecc8fece652e092c9237")
