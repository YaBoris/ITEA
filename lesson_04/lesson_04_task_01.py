from abc import abstractmethod
import datetime


class Person:

    def __init__(self, *args):
        self.surname = args[0]
        self.birthday = args[1]
        self.faculty = args[2]

    @abstractmethod
    def get_info(self):
        pass

    def how_old(self):
        date_now = datetime.date.today()
        if self.birthday[1] < date_now.month:
            return date_now.year - self.birthday[2]
        elif self.birthday[1] == date_now.month:
            if self.birthday[0] < date_now.day:
                return date_now.year - self.birthday[2]
            else:
                return date_now.year - self.birthday[2] - 1
        else:
            return date_now.year - self.birthday[2] - 1

    def get_age(self):
        return self.birthday[2]


class Enrollee(Person):

    def __init__(self, *args):
        super(Enrollee, self).__init__(*args)
        print(f"New enrollee {self.surname} added\n\n")

    def get_info(self):
        print(f"Enrollee surname: {self.surname}\n"
              f"Birthday: {self.birthday}\n"
              f"Faculty: {self.faculty}\n"
              f"Age: {self.how_old()}\n\n")


class Student(Person):

    def __init__(self, *args):
        super(Student, self).__init__(*args)
        self.course = args[3]
        print(f"New student {self.surname} added\n\n")

    def get_info(self):
        print(f"Student surname: {self.surname}\n"
              f"Birthday: {self.birthday}\n"
              f"Faculty: {self.faculty}\n"
              f"Course: {self.course}\n"
              f"Age: {self.how_old()}\n\n")


class Teacher(Person):

    def __init__(self, *args):
        super(Teacher, self).__init__(*args)
        self.position = args[3]
        self.expirience = args[4]
        print(f"New teacher {self.surname} added\n\n")

    def get_info(self):
        print(f"Teacher surname: {self.surname}\n"
              f"Birthday: {self.birthday}\n"
              f"Faculty: {self.faculty}\n"
              f"Course: {self.position}\n"
              f"Expirience: {self.expirience}\n"
              f"Age: {self.how_old()}\n\n")


year = ''
month = ''
day = ''
course = ''
experience = ''
db_list = []
LOWER_AGE_LIMIT = 18
UPPER_AGE_LIMIT = 65
MONTH_COUNT = 12
days_check = {
    '1': 31,
    '2': 29,
    '3': 31,
    '4': 30,
    '5': 31,
    '6': 30,
    '7': 31,
    '8': 31,
    '9': 30,
    '10': 31,
    '11': 30,
    '12': 31
    }


def search_age(range_numbers):
    if range_numbers[0] > range_numbers[1]:
        wright_range = (range_numbers[1], range_numbers[0])
    else:
        wright_range = (range_numbers[0], range_numbers[1])
    for index in range(len(db_list)):
        print(db_list[index].how_old())
        if wright_range[0] <= db_list[index].how_old() <= wright_range[1]:
            db_list[index].get_info()


def check_year(x_string):
    date_now = datetime.date.today()
    try:
        int(x_string)
        if LOWER_AGE_LIMIT > (date_now.year - int(x_string)) or (date_now.year - int(x_string)) > UPPER_AGE_LIMIT:
            raise ValueError
        return False
    except ValueError:
        print("Enter correct value for the year of birthday")
        return True


def check_month(x_string):
    try:
        int(x_string)
        if 1 > int(x_string) or int(x_string) > MONTH_COUNT:
            raise ValueError
        return False
    except ValueError:
        print("Month must to be number from 1 to 12")
        return True


def check_day(x_string, curr_month):
    try:
        int(x_string)
        if 1 > int(x_string) or int(x_string) > days_check[curr_month]:
            raise ValueError
        return False
    except ValueError:
        print("Enter correct value of the day of the month")
        return True


def check_experience(x_string, birthday_year):
    date_now = datetime.date.today()
    try:
        int(x_string)
        if date_now.year < (int(birthday_year) + LOWER_AGE_LIMIT + int(x_string)) or int(x_string) < 1:
            raise ValueError
        return False
    except ValueError:
        print("Enter correct value of the day of the month")
        return True


while True:
    print("1.Add new person\n"
          "2.Search by age in range\n"
          "3.View all information\n"
          "4.Exit\n\n"
          "Select option(1-4): ")
    try:
        selected_option = input()
        int(selected_option)
        if int(selected_option) > 4 or int(selected_option) < 1:
            raise ValueError
    except ValueError:
        continue

    if int(selected_option) == 1:
        while True:
            print("1.Enrollee\n"
                  "2.Student\n"
                  "3.Teacher\n")
            try:
                selected_option = input()
                int(selected_option)
                if int(selected_option) > 3 or int(selected_option) < 1:
                    raise ValueError
            except ValueError:
                continue

            if int(selected_option) == 1:
                print("Enter surname: ")
                surname = input()

                circle_value = True
                while circle_value:
                    print("Enter year of birth: ")
                    year = input()
                    circle_value = check_year(year)

                circle_value = True
                while circle_value:
                    print("Enter month of birth(1-12): ")
                    month = input()
                    circle_value = check_month(month)

                circle_value = True
                while circle_value:
                    print("Enter day of birth(): ")
                    day = input()
                    circle_value = check_day(day, month)

                birthday = (int(day), int(month), int(year))
                print("Enter faculty: ")
                faculty = input()
                db_list.append(Enrollee(surname, birthday, faculty))
                break
            elif int(selected_option) == 2:
                print("Enter surname: ")
                surname = input()

                circle_value = True
                while circle_value:
                    print("Enter year of birth: ")
                    year = input()
                    circle_value = check_year(year)

                circle_value = True
                while circle_value:
                    print("Enter month of birth(1-12): ")
                    month = input()
                    circle_value = check_month(month)

                circle_value = True
                while circle_value:
                    print("Enter day of birth(): ")
                    day = input()
                    circle_value = check_day(day, month)

                birthday = (int(day), int(month), int(year))
                print("Enter faculty: ")
                faculty = input()
                while True:
                    print("Enter course(from 1 to 6): ")
                    try:
                        course = input()
                        int(course)
                        if int(course) > 6 or int(course) < 1:
                            raise ValueError
                        else:
                            break
                    except ValueError:
                        continue
                db_list.append(Student(surname, birthday, faculty, int(course)))
                break
            elif int(selected_option) == 3:
                print("Enter surname: ")
                surname = input()

                circle_value = True
                while circle_value:
                    print("Enter year of birth: ")
                    year = input()
                    circle_value = check_year(year)

                circle_value = True
                while circle_value:
                    print("Enter month of birth(1-12): ")
                    month = input()
                    circle_value = check_month(month)

                circle_value = True
                while circle_value:
                    print("Enter day of birth(): ")
                    day = input()
                    circle_value = check_day(day, month)

                birthday = (int(day), int(month), int(year))
                print("Enter faculty: ")
                faculty = input()
                print("Enter position: ")
                position = input()
                while circle_value:
                    print("Enter experience: ")
                    experience = input()
                    circle_value = check_experience(experience, year)

                db_list.append(Teacher(surname, birthday, faculty, position, experience))
                break
    elif int(selected_option) == 2:
        age = []
        print("Enter first number of age range:")
        age.append(int(input()))
        print("Enter first number of age range:")
        age.append(int(input()))
        search_age(age)
    elif int(selected_option) == 3:
        for i in range(len(db_list)):
            db_list[i].get_info()
    elif int(selected_option) == 4:
        break
