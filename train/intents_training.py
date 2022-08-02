from recognition import RecorderRecognizer
from json import load
from json import dump
from os import path

class IntentsTraining:
    def __init__(self):
        self.__recorder_recognizer = RecorderRecognizer()

    def train_responses(self):
        while(True):
            listened_audio = self.__recorder_recognizer.record_audio()
            recognized_data = self.__recorder_recognizer.recognize_audio(listened_audio)

            if path.exists('../json/intents.json'):
                with open('../json/intents.json', encoding='utf-8') as file:
                    json_data = load(file)

                if recognized_data not in json_data["greeting"]["response"] and recognized_data:
                    json_data["greeting"]["response"].append(recognized_data)
                    print(recognized_data + " added to 'intents.json' [responses]")

                else:
                    continue

                with open('../json/intents.json', mode='w', encoding='utf-8') as file:
                    dump(json_data, file, ensure_ascii=False, indent=2)

            else:
                break

    def train_answers(self):
        while (True):
            listened_audio = self.__recorder_recognizer.record_audio()
            recognized_data = self.__recorder_recognizer.recognize_audio(listened_audio)

            if path.exists('../json/intents.json'):
                with open('../json/intents.json', encoding='utf-8') as file:
                    json_data = load(file)

                if recognized_data not in json_data["greeting"]["answer"] and recognized_data:
                    json_data["greeting"]["answer"].append(recognized_data)
                    print(recognized_data + " added to 'intents.json' [answers]")

                else:
                    continue

                with open('../json/intents.json', mode='w', encoding='utf-8') as file:
                    dump(json_data, file, ensure_ascii=False, indent=2)

            else:
                break

    @staticmethod
    def now_available_intents():
        print('Now available intents:')
        with open('../json/intents.json', encoding='utf-8') as file:
            json_data = load(file)

        for index, key in enumerate(json_data.keys(), 1):
            print(str(index) + '. ' + key)