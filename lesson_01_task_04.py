def bank(init_deposit, deposit_term, percents):
    i = 0
    final_deposit = init_deposit
    while i < deposit_term:
        final_deposit += (final_deposit / 100) * percents
        i += 1
    return final_deposit


while True:
    while True:
        print("Enter initial deposit amount(UAH): ")
        initial_deposit = input()
        if int(initial_deposit) < 0:
            print("Initial deposit must be greater than \'0\', please enter correct value")
        else:
            break
    while True:
        print("Enter percent(1%-100%): ")
        percent = input()
        if int(percent) <= 0:
            print("Percent must be greater than \'0\', please enter correct value")
        else:
            break
    while True:
        print("Enter the total time of the existence of the deposit(years): ")
        years = input()
        if int(years) <= 1:
            print("Value must be at least \'1\', please enter correct value")
        else:
            break
    final_deposit_amount = bank(int(initial_deposit), int(years), int(percent))
    print("If you put {0} UAH for {1} years with an intereset rate of {2}% per annum, then you will resceive: {3:.2f} UAH".format(initial_deposit, years, percent, final_deposit_amount))
    break
