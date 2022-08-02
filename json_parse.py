from json import load

class JsonParse:
    def __init__(self):
        self.__commands = ""

    def get_commands_by_classification(self, classification):
        with open('json/' + str(classification) + '.json', 'r', encoding='utf-8') as file:
            self.__commands = load(file)
        return self.__commands