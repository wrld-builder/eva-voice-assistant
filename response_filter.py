from json_parse import JsonParse

class ResponseFilter:
    def __init__(self):
        self.__json_parser = JsonParse()
        self.__intents = self.__json_parser.get_commands_by_classification('intents')
        self.__weather = self.__json_parser.get_commands_by_classification('weather')
        self.__action = self.__json_parser.get_commands_by_classification('action')
        self.__speaking_suggestion = self.__json_parser.get_commands_by_classification('speaking_suggestion')

    def filter_voice_input(self, voice_input):
        if voice_input in self.__intents["greeting"]["response"]:
            return [self.__intents["greeting"]["answer"], "greeting"]     #second - location
        elif voice_input in self.__weather["weather_today"]["response"]:       #threading soon
            return [self.__weather["weather_today"]["answer"], "weather_today"]        #second - response type
        elif voice_input in self.__weather["weather_tomorrow"]["response"]:
            return [self.__weather["weather_tomorrow"]["answer"], "weather_tomorrow"]

    def filter_action(self, voice_input):
        if voice_input in self.__action["training"]["response"]:
            return [self.__action["training"]["answer"], "training"]

    @property
    def speaking_suggestion_intents(self):
        return self.__speaking_suggestion['suggest']['intention']

    @property
    def sepaking_suggestion_weather(self):
        return self.__speaking_suggestion['suggest']['weather']