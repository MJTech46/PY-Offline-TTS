# System imports
import os
from datetime import datetime
import threading
import time
import webbrowser

# Third-party imports
import soundfile as sf
from flask import Flask, jsonify, render_template, request, send_from_directory
from kokoro_onnx import Kokoro


# pip install flask soundfile kokoro_onnx


# Configurations
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GENERATED_FOLDER = os.path.join(BASE_DIR, "Generated_Audios")
os.makedirs(GENERATED_FOLDER, exist_ok=True)



# Voice generation engine setup
print("Loading Kokoro model...")
kokoro = Kokoro(
    "lib/kokoro-v1.0.int8.onnx",
    "lib/voices-v1.0.bin"
)
print("Model loaded!")



# Supporting functions
def open_browser():
    time.sleep(2)
    webbrowser.open("http://127.0.0.1:5000")



# Flask app setup
app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon'
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    text = data["text"]
    voice = data["voice"]
    speed = float(data["speed"])
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".wav"
    filepath = os.path.join(GENERATED_FOLDER, filename)

    samples, sample_rate = kokoro.create(
        text=text,
        voice=voice,
        speed=speed,
        lang = data["lang"]
    )
    sf.write(filepath, samples, sample_rate)

    return jsonify({
        "success": True,
        "filename": filename,
        "url": "/download/" + filename
    })


@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(
        GENERATED_FOLDER,
        filename,
        as_attachment=True
    )


@app.route("/audio/<filename>")
def audio(filename):
    return send_from_directory(
        GENERATED_FOLDER,
        filename
    )


if __name__ == "__main__":
    threading.Thread(target=open_browser,daemon=True).start()
    app.run(host="0.0.0.0",port=5000, debug=False, use_reloader=False)