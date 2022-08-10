from recognition import RecorderRecognizer
from json import load
from json import dump
from os import path

def translate(key):
    if key == 'greeting': return 'Приветствие'
    elif key == 'goodbye': return 'Прощание'
    else: pass

def translate_reverse(key):
    if key == 'Приветствие': return 'greeting'
    elif key == 'Прощание': return 'goodbye'
    else: pass

class IntentsTraining:
    def __init__(self):
        self.__recorder_recognizer = RecorderRecognizer()

    def train_responses(self, assistant, intent_type):
        assistant.say_current_text('Начинаем разговор. Я вас слушаю')
        assistant.say_current_text('Скажите стоп, чтобы закончить тренировку')

        while (True):
            listened_audio = self.__recorder_recognizer.record_audio()
            recognized_data = self.__recorder_recognizer.recognize_audio(listened_audio)

            if recognized_data == 'Стоп':
                assistant.say_current_text('Отлично! Будет скучно, возвращайся')
                break

            if path.exists('../json/intents.json'):
                with open('../json/intents.json', encoding='utf-8') as file:
                    json_data = load(file)

            elif path.exists('json/intents.json'):
                with open('json/intents.json', encoding='utf-8') as file:
                    json_data = load(file)

                if recognized_data not in json_data[intent_type]["response"] and recognized_data:
                    json_data[intent_type]["response"].append(recognized_data)
                    print(recognized_data + " added to 'intents.json' [responses]")

                else:
                    continue

            if path.exists('../json/intents.json'):
                with open('../json/intents.json', mode='w', encoding='utf-8') as file:
                    dump(json_data, file, ensure_ascii=False, indent=2)

            elif path.exists('json/intents.json'):
                with open('json/intents.json', mode='w', encoding='utf-8') as file:
                    dump(json_data, file, ensure_ascii=False, indent=2)

            else:
                break

    def train_answers(self, assistant, intent_type):
        assistant.say_current_text('Начинаем разговор. Я вас слшуаю')

        while (True):
            listened_audio = self.__recorder_recognizer.record_audio()
            recognized_data = self.__recorder_recognizer.recognize_audio(listened_audio)

            if recognized_data == 'Стоп':
                break

            if path.exists('../json/intents.json'):
                with open('../json/intents.json', encoding='utf-8') as file:
                    json_data = load(file)

            elif path.exists('json/intents.json'):
                with open('json/intents.json', encoding='utf-8') as file:
                    json_data = load(file)


                if recognized_data not in json_data[intent_type]["answer"] and recognized_data:
                    json_data[intent_type]["answer"].append(recognized_data)
                    print(recognized_data + " added to 'intents.json' [answers]")

                else:
                    continue

            if path.exists('../json/intents.json'):
                with open('../json/intents.json', mode='w', encoding='utf-8') as file:
                    dump(json_data, file, ensure_ascii=False, indent=2)

            elif path.exists('json/intents.json'):
                with open('json/intents.json', mode='w', encoding='utf-8') as file:
                    dump(json_data, file, ensure_ascii=False, indent=2)

            else:
                break

    @staticmethod
    def now_available_intents(assistant):
        assistant.say_current_text('На данный момент в моём разуме приисутсвует понимание следующих вещей:')
        with open('json/intents.json', encoding='utf-8') as file:
            json_data = load(file)

        for index, key in enumerate(json_data.keys(), 1):
            assistant.say_current_text('Номер ' + str(index) + '... ' + translate(key))