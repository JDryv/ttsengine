TTS_LOCAL = True
TTS_ENGINE = "coqui-tts" # "coqui-tts" or "..."
COQUI_ENGINE = "tacotron2-DDC" # "tacotron2-DDC" or "..."
COQUI_ENGINE_DICT = {
    "tacotron2-DDC":"tts_models/en/ljspeech/tacotron2-DDC"
}
COQUI_ENGINE_MODEL_NAME = COQUI_ENGINE_DICT[COQUI_ENGINE]
