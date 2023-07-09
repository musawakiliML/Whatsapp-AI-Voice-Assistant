import openai
from pydub import AudioSegment
from decouple import config

openai.api_key = config('OPENAI_API_KEY')

input_file = 'data/test.ogg'

# Load audio file
audio_file = AudioSegment.from_ogg(input_file)

mp3_file = './data/test.mp3'

# Export audio file to mp3
audio_file.export(mp3_file, format='mp3')
audio_file = open(mp3_file, 'rb')

whisper_response = openai.Audio.transcribe(
    file=audio_file,
    model='whisper_1',
    language='en',
    temperature=0.5,
)

audio_file.close()
print(whisper_response)
