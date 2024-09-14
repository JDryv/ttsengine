import os
import torch
import torchaudio
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts

print("Loading model...")
config = XttsConfig()
config.load_json("config.json")
model = Xtts.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir="/home/jack/.local/share/tts/tts_models--multilingual--multi-dataset--xtts_v2", use_deepspeed=False)
model.cuda()

print("Computing speaker latents...")
gpt_cond_latent, speaker_embedding = model.get_conditioning_latents(audio_path=["GSH.wav"])

print("Inference...")
out = model.inference(
    """
The revolution will not be right back after a message about a white tornado, white lightning, or white people
The revolution will not go better with Coke
The revolution will be no re-run, brothers
The revolution will be live""",
    "en",
    gpt_cond_latent,
    speaker_embedding,
    temperature=0.7, # Add custom parameters here
)
torchaudio.save("xtts.wav", torch.tensor(out["wav"]).unsqueeze(0), 24000)
