# player.py
import subprocess
from io import BytesIO
import os

def play_audio_chunks():
    # Launch the producer subprocess and connect to its stdout
    process = subprocess.Popen(['python3', 'producer.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    chunk_counter = 0

    while True:
        # Read a chunk of audio data from the producer
        chunk_size = 44 + 44100 * 2  # Size of a 1-second WAV file (44-byte header + 44100 samples of 2 bytes)
        chunk_data = process.stdout.read(chunk_size)

        if chunk_data:
            # Save the chunk data to a temporary wav file
            temp_filename = f"temp_chunk_{chunk_counter}.wav"
            with open(temp_filename, 'wb') as f:
                f.write(chunk_data)

            # Play the chunk using ffplay
            subprocess.run(['ffplay', '-nodisp', '-autoexit', temp_filename])

            # Remove the temporary file after playback
            os.remove(temp_filename)

            chunk_counter += 1
        else:
            break  # Exit if no more data is coming

if __name__ == "__main__":
    play_audio_chunks()
