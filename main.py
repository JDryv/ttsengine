import torch
from tts.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"
print (f"Using device: {device}")

def generate_audio(text):
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", device=device)
    tts.tts_to_file(text=text, file_path="output.wav")
    return "output.wav"

if __name__ == "__main__":
    text = "Hello, I am a text-to-speech model.Wow, this is amazing!"
    generate_audio(text)
