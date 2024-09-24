# producer.py
import time
import sys
from io import BytesIO
from pydub.generators import Sine

def generate_audio_chunks():
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

if __name__ == "__main__":
    generate_audio_chunks()
