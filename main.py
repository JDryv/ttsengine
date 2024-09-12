import torch
from TTS.api import TTS
import os
import numpy as np
from playsound import playsound







def generate_audio(text):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print (f"Using device: {device}")
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC").to(device)
    tts.tts_to_file(text=text, file_path="output.wav")
    return "output.wav"




# Get current directory and set audio file path
current_dir = os.path.dirname(os.path.abspath(__file__))
audio_file_path = os.path.join(current_dir, "..", "output.wav")





if __name__ == "__main__":
    text = "M' bout' to go AWOL"
    #generate_audio(text)
    #play the audio file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    audio_file_path = os.path.join(current_dir, "..", "output.wav")
    # Call the play_audio function
    # Play the sound
    playsound(audio_file_path)
