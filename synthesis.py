from pyttsx3 import init
from recognition import RecorderRecognizer
from response_filter import ResponseFilter
from random import choice
from weather import WeatherDefinition
from train.intents_training import IntentsTraining
from train.intents_training import translate_reverse
from re import compile
from multiprocessing import Process
from ui.ui_call import call_ui

def lin_rec(recorder_recognizer):
    listened_audio = recorder_recognizer.record_audio()
    recognized_data = recorder_recognizer.recognize_audio(listened_audio)
    print(recognized_data)

    return recognized_data

def training_mode_start(eva, response_filter):
    recorder_recognizer = RecorderRecognizer()
    eva.say_current_text('О чём поговорим на этот раз?')
    eva.say_current_text('Как насчёт поговорить о намерениях?')
    recognized_data = lin_rec(recorder_recognizer)

    if recognized_data in response_filter.speaking_suggestion_intents:
        intents_training = IntentsTraining()
        intents_training.now_available_intents(eva)

        eva.say_current_text('Итак, выберите тему для моего обучения:')
        intent_type = lin_rec(recorder_recognizer)
        intent_type = translate_reverse(intent_type)

        if intent_type == 'greeting' or intent_type == 'goodbye':
            eva.say_current_text('Поговорим о вопросах или стало быть, об ответах?')

            while recognized_data != 'О вопросах' or recognized_data != 'Об ответах':
                recognized_data = lin_rec(recorder_recognizer)

                if recognized_data == 'О вопросах':
                    intents_training.train_responses(eva, intent_type)
                elif recognized_data == 'Об ответах':
                    intents_training.train_answers(eva, intent_type)
                else:
                    eva.say_current_text("Извините, не совсем вас поняла. Попробуйте сказать по другому")

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

    def synth_eva(self, voice_input):
        voice_input = voice_input[4:len(voice_input)].capitalize()
        intention = self.__response_filter.filter_voice_input(voice_input)  # threading soon
        action = self.__response_filter.filter_action(voice_input)

        if intention:
            if intention[len(intention) - 1] == 'greeting':  # intetion[0] - list of answers
                self.say_current_text(choice(intention[0]))
            elif intention[len(intention) - 1] == 'weather_today':
                self.say_current_text(choice(intention[0]))
                WeatherDefinition().say_weather('Санкт-Петербург', self)
            elif intention[len(intention) - 1] == 'weather_tomorrow':
                self.say_current_text(choice(intention[0]))
        elif action:
            if action[len(action) - 1] == 'training':
                self.say_current_text(choice(action[0]))
                training_mode_start(self, self.__response_filter)
        else:
            pass

    def assistant_work(self):
        while True:
            voice_input = self.__rec_rec.recognize_audio(self.__rec_rec.record_audio())
            print(voice_input)

            if voice_input and compile(r'\w+').findall(voice_input)[0] in \
                    [line.rstrip('\n') for line in open('res/approximately_words', encoding='utf-8')]:
                call_ui_process = Process(target=call_ui)
                call_ui_process.start()
                self.synth_eva(voice_input)
            else:
                print('Say my name please')
                pass