# app.py
from flask import Flask, render_template, jsonify
import speedtest

app = Flask(__name__)
speed_test = speedtest.Speedtest()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speedtest')
def speedtest_route():
    try:
        download_speed = round(speed_test.download() / 1e6, 2)  # Convert to Mbps
        return jsonify({'download_speed': download_speed})
    except Exception as e:
        print('Error during speed test:', e)
        return jsonify({'download_speed': 0})

if __name__ == '__main__':
    app.run(debug=True)