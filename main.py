import torch
from TTS.api import TTS
# import os
# import soundfile as sf
# import sounddevice as sd



def generate_audio(text):
    processing_device = "cuda" if torch.cuda.is_available() else "cpu"
    print (f"Using device: {processing_device}")
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC").to(processing_device)
    tts.tts_to_file(text=text, file_path="output.wav")
    return "output.wav"


if __name__ == "__main__":
    text = "M' bout' to go AWOL"
    generate_audio(text)
    # #play the audio file
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # sound_file = os.path.join(current_dir, "output.wav")


    # print(sd.query_devices())
    # # Read the sound file
    # data, samplerate = sf.read(sound_file)

    # # Play the sound
    # sd.play(data, samplerate)

    # # Wait until the sound finishes playing
    # sd.wait()
