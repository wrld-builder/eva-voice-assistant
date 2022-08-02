from pyttsx3 import init
from recognition import RecorderRecognizer
from response_filter import ResponseFilter
from random import choice
from weather import WeatherDefinition

class EvaAssistant:
    def __init__(self):
        self.__name = "Eva"
        self.__sex = "Female"
        self.__speech_language = "ru"
        self.__recognition_language = "ru"
        self.__initialEngine = init()
        self.__rec_rec = RecorderRecognizer()
        self.__response_filter = ResponseFilter()

    def setupAssistant(self):
        voices = self.__initialEngine.getProperty('voices')

        if self.__speech_language == "en":
            self.recognition_language = "en-US"
            if self.__sex == "female":
                self.__initialEngine.setProperty("voice", voices[1].id)
            else:
                self.__initialEngine.setProperty("voice", voices[2].id)
        elif self.__speech_language == 'ru':
            self.__recognition_language = "ru-RU"
            self.__initialEngine.setProperty("voice", voices[0].id)

    def say_current_text(self, current_text):
        self.__initialEngine.say(str(current_text))
        self.__initialEngine.runAndWait()

    def assistant_work(self):
        while True:
            voice_input = self.__rec_rec.recognize_audio(self.__rec_rec.record_audio())
            print(voice_input)

            intention = self.__response_filter.filter_voice_input(voice_input)

            if intention:
                if intention[len(intention) - 1] == 'greeting':              #intetion[0] - list of answers
                    self.say_current_text(choice(intention[0]))
                elif intention[len(intention) - 1] == 'weather_today':
                    self.say_current_text(choice(intention[0]))
                    WeatherDefinition().say_weather('Санкт-Петербург', self)
                elif intention[len(intention) - 1] == 'weather_tomorrow':
                    self.say_current_text(choice(intention[0]))
            else:
                pass