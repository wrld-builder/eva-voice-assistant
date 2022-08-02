from speech_recognition import Recognizer
from speech_recognition import Microphone
from speech_recognition import WaitTimeoutError
from speech_recognition import UnknownValueError
from speech_recognition import RequestError
from vosk import Model
from vosk import KaldiRecognizer
from pyaudio import PyAudio
from pyaudio import paInt16
from json import loads

class RecorderRecognizer:
    def __init__(self):
        self.__recognizer = Recognizer()
        self.__microphone = Microphone()

    def record_audio(self):
        with self.__microphone:
            self.__recognizer.adjust_for_ambient_noise(self.__microphone, duration=2)

            try:
                print('Eva is listening...')
                listened_audio = self.__recognizer.listen(self.__microphone, 5, 5)

            except WaitTimeoutError:
                print('Exception: check work of your microphone')
                return

            return listened_audio

    def use_offline_recognize_audio(self):
        model = Model("model/vosk-model-small-ru-0.22")
        rec = KaldiRecognizer(model, 16000)
        audio_p = PyAudio()
        audio_stream = audio_p.open(format=paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        audio_stream.start_stream()

        while True:
            data = audio_stream.read(4000)
            if len(data) == 0:
                break

            if rec.AcceptWaveform(data):
                x = loads(rec.Result())
                print(x['text'])

            else:
                pass

        return rec.FinalResult()

    def recognize_audio(self, listened_audio, *args: tuple):
        recognized_data = ""

        try:
            print('Eva is doing recognition...')
            recognized_data = self.__recognizer.recognize_google(listened_audio, language="ru").lower()

        except UnknownValueError:
            pass

        except RequestError:
            print('Exception: check your internet connection')
            print('Trying to use offline voice recognition...')
            recognized_data = self.use_offline_recognize_audio()

        if recognized_data:
            return recognized_data.capitalize()
        else:
            return ''