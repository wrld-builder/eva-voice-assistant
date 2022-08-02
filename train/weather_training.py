from recognition import RecorderRecognizer
from json import load
from json import dump
from os import path

class WeatherTraining:
    def __init__(self):
        self.__recorder_recognizer = RecorderRecognizer()

    def train_responses(self):
        while(True):
            listened_audio = self.__recorder_recognizer.record_audio()
            recognized_data = self.__recorder_recognizer.recognize_audio(listened_audio)

            if path.exists('../json/weather.json'):
                with open('../json/weather.json', encoding='utf-8') as file:
                    json_data = load(file)

                if recognized_data not in json_data["greeting"]["response"]:
                    json_data["greeting"]["response"].append(recognized_data)
                    print(recognized_data + " added to 'weather.json' [responses]")

                else:
                    continue

                with open('../json/weather.json', mode='w', encoding='utf-8') as file:
                    dump(json_data, file, ensure_ascii=False, indent=2)

            else:
                break