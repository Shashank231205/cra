from flask import Flask, render_template, request, jsonify
from inference import run_inference
from image_receiver import save_base64_image
from robo_controller import trigger_motor
import csv
import datetime
import os

app = Flask(__name__)

LOG_DIR = 'logs'
LOG_PATH = os.path.join(LOG_DIR, 'prediction_log.csv')

# Ensure log directory and file exist
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

if not os.path.exists(LOG_PATH):
    with open(LOG_PATH, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Timestamp', 'Label', 'Confidence', 'Action'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    img_path = save_base64_image(data['image'])

    result = run_inference(img_path)  # expects {"label": ..., "confidence": ...}
    action = trigger_motor(result["label"])

    # Log
    with open(LOG_PATH, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.datetime.now(), result["label"], result["confidence"], action])

    return jsonify({**result, "action": action})

@app.route('/logs')
def logs():
    with open(LOG_PATH) as f:
        reader = csv.reader(f)
        next(reader)
        return jsonify(list(reader))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
