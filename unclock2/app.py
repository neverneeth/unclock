from flask import Flask, render_template, jsonify, request
import random
from datetime import datetime
import pytz
from timezonefinder import TimezoneFinder

app = Flask(__name__)
tf = TimezoneFinder()

@app.route('/')
def index():
    # Render the main template with no initial clocks
    return render_template('index.html')

@app.route('/add_clock', methods=['POST'])
def add_clock():
    # Generate random coordinates within valid latitude and longitude ranges
    lat = random.uniform(-90, 90)
    lon = random.uniform(-180, 180)

    # Find the timezone based on coordinates
    timezone = tf.timezone_at(lng=lon, lat=lat)
    if timezone:
        timezone_obj = pytz.timezone(timezone)
        current_time = datetime.now(timezone_obj).strftime('%H:%M:%S')
        coordinates = f"Lat: {lat:.2f}, Lon: {lon:.2f}"
        
        return jsonify({
            'success': True,
            'timezone': timezone,
            'coordinates': coordinates,
            'current_time': current_time
        })
    else:
        return jsonify({'success': False, 'error': 'Could not find timezone for the given coordinates'})

@app.route('/get_time', methods=['GET'])
def get_time():
    tz = request.args.get('timezone')
    if tz in pytz.all_timezones:
        timezone = pytz.timezone(tz)
        current_time = datetime.now(timezone).strftime('%H:%M:%S')
        return jsonify({'time': current_time})
    else:
        return jsonify({'error': 'Invalid timezone'}), 400
if __name__ == '__main__':
    app.run(debug=True)