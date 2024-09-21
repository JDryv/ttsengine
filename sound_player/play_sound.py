import requests
from pydub import AudioSegment
from pydub.playback import play

# Replace with the actual sound file you want to play
url = 'http://sound-server:5000/sounds/example.wav'

response = requests.get(url)

with open('temp.wav', 'wb') as f:
    f.write(response.content)

sound = AudioSegment.from_wav('temp.wav')
play(sound)
