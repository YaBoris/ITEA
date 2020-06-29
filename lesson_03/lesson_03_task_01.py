from datetime import datetime
import time

number = 20
maximum = 100


def counter(numbers):

    def statistic_timer(func):

        def shell(*args):
            full_time_execution = datetime.now()
            for i in range(numbers):
                start_time = datetime.now()
                func(*args)
                end_time = datetime.now()
                full_time_execution += (end_time - start_time)
            print('Result: {}'.format(full_time_execution))
            return full_time_execution
        return shell
    return statistic_timer


@counter(number)
def computer(max_digit):
    for index in range(max_digit):
        index ** max_digit
    return print("Function executed")


computer(maximum)
