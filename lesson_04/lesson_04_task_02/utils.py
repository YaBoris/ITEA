def check_input_option():
    while True:
        try:
            option = input()
            int(option)
            if 4 > int(option) > 0:
                return int(option)
            else:
                raise ValueError
        except ValueError:
            print("Error! Enter correct option!\n")
