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
              f"Age: {self.how_old()}\n")


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
              f"Age: {self.how_old()}\n")


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
              f"Age: {self.how_old()}\n")


count_of_person = ''
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


def check_experience(expirience_data, birthday_year):
    date_now = datetime.date.today()
    # print(type(birthday_year))
    # print(birthday_year)
    temp = int(birthday_year) + LOWER_AGE_LIMIT + int(expirience_data)
    print(temp)
    try:
        int(expirience_data)
        if date_now.year < (int(birthday_year) + LOWER_AGE_LIMIT + int(expirience_data)) or int(expirience_data) < 1:
            raise ValueError
        return False
    except ValueError:
        print("Enter correct value of the expirience")
        return True


def decorator_set_general_data(func):
    def wrapper():
        new_day = ''
        new_month = ''
        new_year = ''

        print("Enter surname: ")
        new_surname = input()

        is_continue = True
        while is_continue:
            print("Enter year of birth: ")
            new_year = input()
            is_continue = check_year(new_year)

        is_continue = True
        while is_continue:
            print("Enter month of birth(1-12): ")
            new_month = input()
            is_continue = check_month(new_month)

        is_continue = True
        while is_continue:
            print("Enter day of birth(): ")
            new_day = input()
            is_continue = check_day(new_day, new_month)

        new_birthday = (int(new_day), int(new_month), int(new_year))
        print("Enter faculty: ")
        new_faculty = input()
        added_person_data = func(new_year)
        return new_surname, new_birthday, new_faculty, added_person_data
    return wrapper


@decorator_set_general_data
def enrollee_data(b_year):
    return None


@decorator_set_general_data
def student_data(b_year):
    new_course = ''
    while True:
        print("Enter course(from 1 to 6): ")
        try:
            new_course = input()
            int(new_course)
            if int(new_course) > 6 or int(new_course) < 1:
                raise ValueError
            else:
                break
        except ValueError:
            continue
    return new_course


@decorator_set_general_data
def teacher_data(birhday_year):
    b_year = birhday_year
    new_experience = ''
    print("Enter position: ")
    new_position = input()
    is_continue = True
    while is_continue:
        print("Enter experience: ")
        new_experience = input()
        is_continue = check_experience(new_experience, b_year)
    return new_position, new_experience


while True:
    print("Enter count of new person: ")
    try:
        count_of_person = input()
        int(count_of_person)
        break
    except ValueError:
        continue

selected_option = ''

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
        for i in range(int(count_of_person)):
            while True:
                print("1.Enrollee\n"
                      "2.Student\n"
                      "3.Teacher\n")
                try:
                    selected_option = input()
                    int(selected_option)
                    if int(selected_option) > 3 or int(selected_option) < 1:
                        raise ValueError
                    break
                except ValueError:
                    continue

            if int(selected_option) == 1:
                user_data = enrollee_data()
                db_list.append(Enrollee(user_data[0], user_data[1], user_data[2]))
                # break
            elif int(selected_option) == 2:
                user_data = student_data()
                db_list.append(Student(user_data[0], user_data[1], user_data[2], user_data[3][0]))
                # break
            elif int(selected_option) == 3:
                user_data = teacher_data()
                db_list.append(Teacher(user_data[0], user_data[1], user_data[2], user_data[3][0], user_data[3][1]))
                # break
    elif int(selected_option) == 2:
        age = []
        limit = ''
        while True:
            print("Enter lower limit of age range:")
            try:
                limit = input()
                int(limit)
                break
            except ValueError:
                continue
        age.append(int(limit))
        while True:
            print("Enter upper limit of age range:")
            try:
                limit = input()
                int(limit)
                break
            except ValueError:
                continue
        age.append(int(limit))
        search_age(age)
    elif int(selected_option) == 3:
        for j in range(len(db_list)):
            db_list[j].get_info()
    elif int(selected_option) == 4:
        break
