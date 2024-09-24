import time
import sys
from io import BytesIO
from pydub.generators import Sine
import time
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts


def initialize_TTS():
    """
    Initialize the TTS model and compute the speaker latents.
    input: None
    output: model, gpt_cond_latent, speaker_embedding
    """
    print("Loading model...")
    config = XttsConfig()
    config.load_json("config.json")
    model = Xtts.init_from_config(config)
    model.load_checkpoint(config, checkpoint_dir="/home/jack/.local/share/tts/tts_models--multilingual--multi-dataset--xtts_v2", use_deepspeed=False)
    model.cuda()
    print("Computing speaker latents...")
    gpt_cond_latent, speaker_embedding = model.get_conditioning_latents(audio_path=["LJ_latent.wav"])
    return model, gpt_cond_latent, speaker_embedding


def generate_audio_chunks(model, gpt_cond_latent, speaker_embedding):
    """
    Generate audio chunks using sine wave and write to stdout.
    input: model, gpt_cond_latent, speaker_embedding
    output: None
    """
    chunk_counter = 0
    while True:
        # Generate a 1-second sine wave audio chunk (440 Hz tone)
        sine_wave = Sine(440).to_audio_segment(duration=1000)  # 1-second chunk

        # Save the chunk to an in-memory buffer (BytesIO) as a .wav file
        buffer = BytesIO()
        sine_wave.export(buffer, format='wav')

        # Write the binary data of the audio chunk to stdout (pipe)
        sys.stdout.buffer.write(buffer.getvalue())
        sys.stdout.flush()  # Ensure immediate sending

        # Logging to stderr for chunk generation
        print(f"Generated chunk {chunk_counter}", file=sys.stderr)

        chunk_counter += 1
        time.sleep(1)  # Simulate delay between chunks


model, gpt_cond_latent, speaker_embedding = initialize_TTS()
generate_audio_chunks(model, gpt_cond_latent, speaker_embedding)
