#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
import os
import torch
import whisper
import numpy as np

app = Flask(__name__)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        model = whisper.load_model("base", device=DEVICE)

        
        f = request.files['audio_data']
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
            
        # audio = whisper.load_audio("audio.wav")
        # audio = whisper.pad_or_trim(audio)
        # mel = whisper.log_mel_spectrogram(audio).to(model.device)
        # _, probs = model.detect_language(mel)
        
        result = model.transcribe("audio.wav")
        print(result["text"], flush=True)
            
        print('file uploaded successfully')

        return render_template('index.html', request="POST", result=result["text"])
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False)