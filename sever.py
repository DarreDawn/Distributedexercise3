from flask import Flask, request, jsonify
app = Flask(__name__)

# weather data
weather_data = {
    "Beijing": {"description": "Sunny", "temperature": 25},
    "Shanghai": {"description": "Cloudy", "temperature": 22},
    "New York": {"description": "Rainy", "temperature": 15},
}

@app.route('/weather', methods=['POST'])
def get_weather():
    data = request.get_json()
    location = data.get('location')
    # find weather
    weather_info = weather_data.get(location)
    if weather_info:
        return jsonify(weather_info)
    else:
        return jsonify({"error": "Location not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
