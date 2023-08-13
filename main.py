from vosk import Model, KaldiRecognizer
from pydub import AudioSegment
import json
# Устанавливаем Frame Rate
FRAME_RATE = 16000
CHANNELS=1
def speech_to_text(media):
    model = Model("vosk-model-small-ru-0.22")
    rec = KaldiRecognizer(model, FRAME_RATE)
    rec.SetWords(True)
    
# Используя библиотеку pydub делаем предобработку аудио
    mp3 = AudioSegment.from_wav(media)
    mp3 = mp3.set_channels(CHANNELS)
    mp3 = mp3.set_frame_rate(FRAME_RATE)

# Преобразуем вывод в json
    rec.AcceptWaveform(mp3.raw_data)
    result = rec.Result()
    text = json.loads(result)["text"]
    return text

print(speech_to_text(r'test2rus.wav'))