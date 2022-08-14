from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from config.config import OWM_TOKEN

class WeatherDefinition():
    def __init__(self):
        self.__config_dict = get_default_config()
        self.__config_dict['language'] = 'ru'
        self.__owm = OWM(str(OWM_TOKEN), self.__config_dict)
        self.__mgr = self.__owm.weather_manager()

    def get_weather(self, city):
        observation = self.__mgr.weather_at_place(city)
        weather = observation.weather
        temp = weather.temperature('celsius')
        wind = weather.wind()

        return [weather.detailed_status, temp['temp'], temp['feels_like'], wind['speed']]

    def say_weather(self, city, assistant):
        def_weather = self.get_weather(city)
        assistant.say_current_text('В городе ' + city + str(def_weather[0]) +
                              '. Температура воздуха ' + str(def_weather[1]) +
                              ' градусов цельсии. Ощущается, как ' + str(def_weather[2]) +
                              '. Средняя скорость ветра ' + str(def_weather[3]) + ' метров в секунду')
