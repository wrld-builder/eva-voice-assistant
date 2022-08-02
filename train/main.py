from intents_training import IntentsTraining

def training_mode_initialize():
    print('''
        Training mode started...
        Choose the intention:
        1. intents
        2. weather
        3. site
        4. video
        5. music

        Please, type the number of your intention:''')

def activity_q():
    print('''
    What activity do you want to upgrade?
    1. Responses
    2. Answers
    
    Please, type the number of your intention:''')

def weather_q():
    print('''
        Do you want to know the weather for tomorrow or today?
        1. Today
        2. Tomorrow

        Please, type the number of your intention:''')

def wrong_intention():
    print('Wrong code of intention')

if __name__ == '__main__':
    training_mode_initialize()

    intention_code = int(input())
    if intention_code == 1:
        intents_training = IntentsTraining()
        intents_training.now_available_intents()

        activity_q()
        activity_code = int(input())
        if activity_code == 1:
            intents_training.train_responses()

        elif activity_code == 2:
            intents_training.train_answers()

        else:
            wrong_intention()

    elif intention_code == 2:
        weather_q()
        today_tomorrow = int(input())

        activity_q()
        activity_code = int(input())

        if today_tomorrow == 1:
            if activity_code == 1:
                pass

            elif activity_code == 2:
                pass

            else:
                wrong_intention()

        elif today_tomorrow == 2:
            pass

        else:
            wrong_intention()

    elif intention_code == 3:
        pass

    elif intention_code == 4:
        pass

    elif intention_code == 5:
        pass

    else:
        wrong_intention()