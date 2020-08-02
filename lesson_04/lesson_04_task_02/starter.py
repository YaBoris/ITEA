import datetime
import getpass
from abc import abstractmethod
from constant_data import MIN_PASS_LENGTH, MAX_PASS_LENGTH
from utils import check_input_option


user_dict = {}
messages_db = {}
user_message_list = []


class Registration:
    def __init__(self):
        self.user_login = 'None'
        self.user_pass = 'None'
        self.user_pass_again = 'None'

    def is_correct_login(self):
        while True:
            print("Enter login(letters and digits only):")
            self.user_login = input()
            if not self.user_login.isalnum():
                print("Username must contain letters and digits only!")
                continue
            if user_dict.get(self.user_login) is not None:
                print("Current name is busy. Select other login.")
                continue
            else:
                return True

    def is_correct_password(self):
        while True:
            self.user_pass = getpass.getpass('Enter password(minimum 8 characters. Digits and letters only): ')
            self.user_pass_again = getpass.getpass('Enter password again:')
            # print("first pass")
            # self.user_pass = input()
            # print("second pass")
            # self.user_pass_again = input()
            if self.user_pass == self.user_pass_again \
                    and MIN_PASS_LENGTH <= len(self.user_pass) <= MAX_PASS_LENGTH \
                    and self.user_pass.isalnum():
                if(len(user_dict)) == 0:
                    user_dict[self.user_login] = AdminUser(self.user_login, self.user_pass)
                    create_date = datetime.datetime.today().strftime("%Y-%m-%d-%H:%M:%S")
                    messages_db[self.user_login] = [(create_date, "Administrator \'" + self.user_login + "\' created")]
                else:
                    user_dict[self.user_login] = NonAdminUser(self.user_login, self.user_pass)
                    create_date = datetime.datetime.today().strftime("%Y-%m-%d-%H:%M:%S")
                    messages_db[self.user_login] = [(create_date, "User \'" + self.user_login + "\' created")]
                return True
            else:
                print("Enter correct password! Minimum 8 characters. Digits and letters only.\n")


class Authorization(Registration):
    def __init__(self):
        super(Authorization, self).__init__()

    def is_correct_login(self):
        while True:
            print("Enter login(letters and digits only):")
            self.user_login = input()
            if user_dict.get(self.user_login) is None:
                print("Current name is not exist. Enter correct name.")
                continue
            else:
                return True

    def is_correct_password(self):
        while True:
            self.user_pass = getpass.getpass('Enter password: ')
            # print("first pass")
            # self.user_pass = input()
            if self.user_pass == user_dict.get(self.user_login).get_password():
                return self.user_login
            else:
                return False


class User:
    def __init__(self, user_name, user_password):
        self._user_name = user_name
        self._user_password = user_password
        print(f"\nName: {self._user_name}\n"
              f"Password: {self._user_password}\n")

    def get_password(self):
        return self._user_password

    def get_login(self):
        return self._user_name

    @abstractmethod
    def work_in_net(self):
        pass

    @abstractmethod
    def view_all_messages(self, checked_user):
        pass


class NonAdminUser(User):
    def view_all_messages(self, checked_user):
        message_list = messages_db[self.get_login()]
        for message_data in message_list:
            print(f"Message: {message_data[1]}")
            print(f"Date of creating: {message_data[0]}\n")
        return True

    def write_message(self):
        while True:
            try:
                message = input()
                if len(message) > 128:
                    raise ValueError
                else:
                    create_date = datetime.datetime.today().strftime("%Y-%m-%d-%H:%M:%S")
                    message_couple = (create_date, message)
                    messages_db[self.get_login()].append(message_couple)
                    print("Message added success!\n")
                    break
            except ValueError:
                print("Length of message too long. It must be no longer than 128 characters! Try again")

    def work_in_net(self):
        while True:
            print("1.View my messages list\n"
                  "2.Write new message\n"
                  "3.Exit from social network\n")
            temp = check_input_option()
            if temp == 1:
                if self.view_all_messages(self):
                    continue
            elif temp == 2:
                print("\nEnter message. No longer than 128 characters.\n")
                self.write_message()
            elif temp == 3:
                break


class AdminUser(User):
    def view_all_messages(self, checked_user):
        message_list = messages_db[checked_user]
        for message_data in message_list:
            print(f"Message: {message_data[1]}")
            print(f"Date of creating: {message_data[0]}\n")
        return True

    @abstractmethod
    def view_all_users(self):
        index = 1
        temp_user_list = []
        for logins in user_dict:
            print(f"{index}. User: {logins[0]}")
            temp_user_list.append((index, logins[0]))
            index += 1
        print("Select user for show his messages by number")
        while True:
            try:
                select_user = input()
                int(select_user)
                if 1 > int(select_user) > len(user_dict):
                    raise ValueError
                else:
                    self.view_all_messages(temp_user_list[int(select_user)-1][1])
                    return True
            except ValueError:
                print("Select right value from showed userlist")

    def work_in_net(self):
        while True:
            print("1.View user list\n"
                  "2.Exit from network")
            try:
                option = input()
                int(option)
                if 3 > int(option) > 0:
                    if int(option) == 1:
                        if self.view_all_users():
                            continue
                    if int(option) == 2:
                        break
                else:
                    raise ValueError
            except ValueError:
                print("Error! Enter correct option!\n")


while True:
    print("1.New user? Registration\n"
          "2.Enter to social network\n"
          "3.Exit")
    try:
        selected_option = input()
        int(selected_option)
        if int(selected_option) == 1:
            start_registration = Registration()
            while True:
                if start_registration.is_correct_login():
                    if start_registration.is_correct_password():
                        print(f"Congratulation! User created! You can to enter to social network now")
                    break
        elif int(selected_option) == 2:
            enter_user = Authorization()
            if enter_user.is_correct_login():
                active_user = enter_user.is_correct_password()
                if active_user:
                    print("Welcome to best of the best social network 'SOCINET'")
                    user_dict.get(active_user).work_in_net()
                else:
                    print("Wrong password. Try again.")
        elif int(selected_option) == 3:
            break
        else:
            raise ValueError
    except ValueError:
        continue
