from flask import Blueprint, request, render_template
import torch
import whisper

api = Blueprint("api", __name__, template_folder='templates', static_folder='static', static_url_path='api/static')
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

@api.route("/", methods=["GET", "POST"])
def home():
    print(request.files, flush=True)
    
    if request.method == "GET":
        return render_template("index.html", result=None)
    
    f = request.files['audio_data']
    with open('audio.wav', 'wb') as audio:
        f.save(audio)
    
    model = whisper.load_model("base", device=DEVICE)
    result = model.transcribe("audio.wav")
    print('result -->', result["text"], flush=True)
    
    return result["text"]