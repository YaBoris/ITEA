import datetime
from lesson_06.lesson_06_task_03.informer import utils
from lesson_06.lesson_06_task_03 import constants


def main_menu():
    city_name = utils.get_city()
    if not city_name:
        print("Service temporary anavailable. Try again later.")
        exit(0)
    if utils.set_coordinates_for_city(city_name):
        print("Service temporary anavailable. Try again later.")
        exit(0)
    if utils.set_weather_data():
        print("Service temporary anavailable. Try again later.")
        exit(0)
    utils.interpretator()
    while True:
        print(
            f"1. Show weather today for {constants.city_data['city']}\n"
            f"2. Select other date for weather forecast for {constants.city_data['city']}\n"
            f"3. Show weather for other city. Must be Enter.\n"
            f"4. Show weather today for your city. It's {utils.get_city()}\n"
            f"5. Exit"
        )
        try:
            selected_option = int(input())
            if selected_option == 1:
                utils.interpretator(selected_option)
            elif selected_option == 2:
                other_days_menu()
            elif selected_option == 3:
                print(f"Enter correct city name: ")
                city_name = input()
                if utils.set_coordinates_for_city(city_name) or utils.set_weather_data():
                    print("Service temporary anavailable. Try again later.")
                    break
                utils.interpretator(1)
                other_days_menu()
            elif selected_option == 4:
                if utils.set_coordinates_for_city(city_name) or utils.set_weather_data():
                    print("Service temporary anavailable. Try again later.")
                    break
                utils.interpretator(selected_option)
            elif selected_option == 5:
                break
            else:
                continue
        except TypeError:
            continue


def other_days_menu():
    today_date = datetime.datetime.today()
    while True:
        for index in range(7):
            today_date += datetime.timedelta(1)
            temp_str = today_date.strftime('%d-%m-%Y')
            print(f"{index+1}. {temp_str}")
        try:
            selected_option = int(input())
            if selected_option == 1:
                utils.interpretator(selected_option + 1)
                break
            elif selected_option == 2:
                utils.interpretator(selected_option + 1)
                break
            elif selected_option == 3:
                utils.interpretator(selected_option + 1)
                break
            elif selected_option == 4:
                utils.interpretator(selected_option + 1)
                break
            elif selected_option == 5:
                utils.interpretator(selected_option + 1)
                break
            elif selected_option == 6:
                utils.interpretator(selected_option + 1)
                break
            elif selected_option == 7:
                utils.interpretator(selected_option + 1)
                break
        except ValueError:
            print("Enter correct value:")
            continue
