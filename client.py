import json
import requests

# RPC函数的URL
RPC_URL = "http://127.0.0.1:5000/weather"


def get_weather(location):
    payload = json.dumps({"location": location})
    headers = {'content-type': 'application/json'}

    response = requests.post(RPC_URL, data=payload, headers=headers)

    if response.status_code == 200:
        weather_info = response.json()
        print(f"Weather in {location}: {weather_info['description']}, {weather_info['temperature']}°C")
    else:
        print("Failed to get weather information.")


if __name__ == "__main__":
    location = input("Enter a location to get weather information: ")
    get_weather(location)
