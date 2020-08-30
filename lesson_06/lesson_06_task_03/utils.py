import requests
import datetime
from bs4 import BeautifulSoup
from lesson_06.lesson_06_task_03 import constants


def set_weather_data():
    getter_weather_current = constants.WEATHER_CHECK_URL + str(constants.city_data["lat"]) + \
                             "&lon=" + str(constants.city_data["lon"]) + "&appid=" + constants.API_KEY + \
                             "&lang=ru&units=metric"
    temp_data_weather = requests.get(getter_weather_current, constants.HEADER, timeout=5)
    if str(temp_data_weather) == "<Response [200]>":
        constants.weather_data = dict(temp_data_weather.json())
    else:
        return 0


def interpretator(type_weather_request=1):
    if type_weather_request == 1:
        value = datetime.datetime.fromtimestamp(constants.weather_data["current"]["dt"])
        today = value.strftime('%d.%m.%Y')
        now_time = value.strftime('%H:%M:%S')
        print(f"Город: {constants.city_data['city']}\n"
              f"Сегодня: {today}, {now_time}. {constants.weather_data['current']['weather'][0]['description']}\n"
              f"Температура воздуха: {constants.weather_data['current']['temp']:.0f} Цельсия\n"
              f"Давление: {constants.weather_data['current']['pressure']/1.333:.0f} мм рт.ст.\n"
              f"Скорость ветра: {constants.weather_data['current']['wind_speed']} м/с\n")
    if type_weather_request == 2:
        value = datetime.datetime.fromtimestamp(constants.weather_data["daily"][1]["dt"])
        day = value.strftime('%d.%m.%Y')
        print(f"Город: {constants.city_data['city']}\n"
              f"Погода на: {day}. {constants.weather_data['daily'][1]['weather'][0]['description']}\n"
              f"Температура воздуха днем: {constants.weather_data['daily'][1]['temp']['day']:.0f} Цельсия\n"
              f"Температура воздуха ночью: {constants.weather_data['daily'][1]['temp']['night']:.0f} Цельсия\n"
              f"Давление: {constants.weather_data['daily'][1]['pressure']/1.333:.0f} мм рт.ст.\n"
              f"Скорость ветра: {constants.weather_data['daily'][1]['wind_speed']} м/с\n")
    if type_weather_request == 3:
        value = datetime.datetime.fromtimestamp(constants.weather_data["daily"][2]["dt"])
        day = value.strftime('%d.%m.%Y')
        print(f"Город: {constants.city_data['city']}\n"
              f"Погода на: {day}. {constants.weather_data['daily'][2]['weather'][0]['description']}\n"
              f"Температура воздуха днем: {constants.weather_data['daily'][2]['temp']['day']:.0f} Цельсия\n"
              f"Температура воздуха ночью: {constants.weather_data['daily'][2]['temp']['night']:.0f} Цельсия\n"
              f"Давление: {constants.weather_data['daily'][2]['pressure'] / 1.333:.0f} мм рт.ст.\n"
              f"Скорость ветра: {constants.weather_data['daily'][2]['wind_speed']} м/с\n")
    if type_weather_request == 4:
        value = datetime.datetime.fromtimestamp(constants.weather_data["daily"][3]["dt"])
        day = value.strftime('%d.%m.%Y')
        print(f"Город: {constants.city_data['city']}\n"
              f"Погода на: {day}. {constants.weather_data['daily'][3]['weather'][0]['description']}\n"
              f"Температура воздуха днем: {constants.weather_data['daily'][3]['temp']['day']:.0f} Цельсия\n"
              f"Температура воздуха ночью: {constants.weather_data['daily'][3]['temp']['night']:.0f} Цельсия\n"
              f"Давление: {constants.weather_data['daily'][3]['pressure'] / 1.333:.0f} мм рт.ст.\n"
              f"Скорость ветра: {constants.weather_data['daily'][3]['wind_speed']} м/с\n")
    if type_weather_request == 5:
        value = datetime.datetime.fromtimestamp(constants.weather_data["daily"][4]["dt"])
        day = value.strftime('%d.%m.%Y')
        print(f"Город: {constants.city_data['city']}\n"
              f"Погода на: {day}. {constants.weather_data['daily'][4]['weather'][0]['description']}\n"
              f"Температура воздуха днем: {constants.weather_data['daily'][4]['temp']['day']:.0f} Цельсия\n"
              f"Температура воздуха ночью: {constants.weather_data['daily'][4]['temp']['night']:.0f} Цельсия\n"
              f"Давление: {constants.weather_data['daily'][4]['pressure'] / 1.333:.0f} мм рт.ст.\n"
              f"Скорость ветра: {constants.weather_data['daily'][4]['wind_speed']} м/с\n")
    if type_weather_request == 6:
        value = datetime.datetime.fromtimestamp(constants.weather_data["daily"][5]["dt"])
        day = value.strftime('%d.%m.%Y')
        print(f"Город: {constants.city_data['city']}\n"
              f"Погода на: {day}. {constants.weather_data['daily'][5]['weather'][0]['description']}\n"
              f"Температура воздуха днем: {constants.weather_data['daily'][5]['temp']['day']:.0f} Цельсия\n"
              f"Температура воздуха ночью: {constants.weather_data['daily'][5]['temp']['night']:.0f} Цельсия\n"
              f"Давление: {constants.weather_data['daily'][5]['pressure'] / 1.333:.0f} мм рт.ст.\n"
              f"Скорость ветра: {constants.weather_data['daily'][5]['wind_speed']} м/с\n")
    if type_weather_request == 7:
        value = datetime.datetime.fromtimestamp(constants.weather_data["daily"][6]["dt"])
        day = value.strftime('%d.%m.%Y')
        print(f"Город: {constants.city_data['city']}\n"
              f"Погода на: {day}. {constants.weather_data['daily'][6]['weather'][0]['description']}\n"
              f"Температура воздуха днем: {constants.weather_data['daily'][6]['temp']['day']:.0f} Цельсия\n"
              f"Температура воздуха ночью: {constants.weather_data['daily'][6]['temp']['night']:.0f} Цельсия\n"
              f"Давление: {constants.weather_data['daily'][6]['pressure'] / 1.333:.0f} мм рт.ст.\n"
              f"Скорость ветра: {constants.weather_data['daily'][6]['wind_speed']} м/с\n")
    if type_weather_request == 8:
        value = datetime.datetime.fromtimestamp(constants.weather_data["daily"][7]["dt"])
        day = value.strftime('%d.%m.%Y')
        print(f"Город: {constants.city_data['city']}\n"
              f"Погода на: {day}. {constants.weather_data['daily'][7]['weather'][0]['description']}\n"
              f"Температура воздуха днем: {constants.weather_data['daily'][7]['temp']['day']:.0f} Цельсия\n"
              f"Температура воздуха ночью: {constants.weather_data['daily'][7]['temp']['night']:.0f} Цельсия\n"
              f"Давление: {constants.weather_data['daily'][7]['pressure'] / 1.333:.0f} мм рт.ст.\n"
              f"Скорость ветра: {constants.weather_data['daily'][7]['wind_speed']} м/с\n")


def get_city():
    full_page = requests.get(constants.CITY_CHECK_BY_IP_URL, constants.HEADER, timeout=5)
    if str(full_page) == "<Response [200]>":
        soup: BeautifulSoup = BeautifulSoup(full_page.content, 'html.parser')
        coordinates = soup.find("table", {"style": "font-size: small;"})
        stri = str(coordinates)
        dirty_list = list(stri.split("</td></tr><tr><td>"))
        dirty_string = str(dirty_list[2])
        city = dirty_string.split("Ваш регион:</td><td>")
        return city[1]
    else:
        return 0


def set_coordinates_for_city(some_city):
    general_weather_current = constants.GENERAL_URL + str(
        some_city) + "&appid=" + constants.API_KEY + "&lang=ru&units=metric"
    temp_data_weather = requests.get(general_weather_current, constants.HEADER, timeout=5)
    if str(temp_data_weather) == "<Response [200]>":
        temp_json = dict(temp_data_weather.json())
        constants.city_data["city"] = temp_json["name"]
        constants.city_data["lat"] = temp_json["coord"]["lat"]
        constants.city_data["lon"] = temp_json["coord"]["lon"]
    else:
        return 0
