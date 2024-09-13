import torch
from TTS.api import TTS
from params import *
import subprocess

def initialize_tts():
    if TTS_LOCAL:
        processing_device = "cuda" if torch.cuda.is_available() else "cpu"
        print (f"Using device: {processing_device}")

    if COQUI_ENGINE == "tacotron2-DDC":
        tts = TTS(model_name=COQUI_ENGINE_MODEL_NAME).to(processing_device)
        return tts

    if COQUI_ENGINE == "xtts_v2":
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=torch.cuda.is_available())
        return tts


def generate_audio(text, tts):

    if TTS_ENGINE == "coqui-tts":
        tts.tts_to_file(text=text, file_path="output.wav")

    if TTS_ENGINE == "google-tts":
        pass
    pass


if __name__ == "__main__":
    tts = initialize_tts()
    while True:
        count = 0
        text = input("Enter the text: ")
        generate_audio(text,tts)
        wav_file_path = "output.wav"
        # Command to play the .wav file using ffplay
        command = f"ffplay -nodisp -autoexit {wav_file_path}"
        # Run the command using subprocess
        subprocess.run(command, shell=True)
