from datetime import datetime
import time


def counter(numbers):
    def statistic_timer(func):
        def wrapper(*args):
            full_time_execution = 0
            for i in range(numbers):
                start_time = datetime.now()
                func(*args)
                end_time = datetime.now()
                delta = end_time - start_time
                full_time_execution += delta.microseconds
            full_time_execution /= 1000000
            return full_time_execution, func.__name__
        return wrapper
    return statistic_timer


# number of repetitions
number = 20


@counter(number)
def computer(max_digit):
    for index in range(max_digit):
        index ** max_digit


maximum = 1000
execution_data = computer(maximum)

print(f"Function called \'{execution_data[1]}\' executed in total {execution_data[0]} seconds")
