from json_parse import JsonParse

class ResponseFilter:
    def __init__(self):
        self.__json_parser = JsonParse()
        self.__intents = self.__json_parser.get_commands_by_classification('intents')
        self.__action = self.__json_parser.get_commands_by_classification('weather')

    def filter_voice_input(self, voice_input):
        if voice_input in self.__intents["greeting"]["response"]:
            return [self.__intents["greeting"]["answer"], "greeting"]     #second - location
        elif voice_input in self.__action["weather_today"]["response"]:
            return [self.__action["weather_today"]["answer"], "weather_today"]        #second - response type
        elif voice_input in self.__action["weather_tomorrow"]["response"]:
            return [self.__action["weather_tomorrow"]["answer"], "weather_tomorrow"]