from intents_training import IntentsTraining
from intents_training import translate_reverse
from recognition import RecorderRecognizer
from synthesis import EvaAssistant

def lin_rec(recorder_recognizer):
    listened_audio = recorder_recognizer.record_audio()
    recognized_data = recorder_recognizer.recognize_audio(listened_audio)
    print(recognized_data)

    return recognized_data

if __name__ == '__main__':
    recorder_recognizer = RecorderRecognizer()
    eva = EvaAssistant()
    eva.say_current_text('О чём поговорим на этот раз?')
    eva.say_current_text('Как насчёт поговорить о намерениях?')
    recognized_data = lin_rec(recorder_recognizer)

    if recognized_data == 'Намерение' or recognized_data == 'Намерения':
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