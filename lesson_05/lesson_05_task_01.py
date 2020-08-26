from threading import Thread

MAX_VALUE = 50


def work_with_threads():
    print(f"This thread is daemon? Yes/No")
    while True:
        daemon_status = input()
        if daemon_status == "Yes":
            return True
        elif daemon_status == "No":
            return False
        else:
            print("Enter correct option - \'Yes\' or \'No\'\n")


def check_is_daemon(is_daemon):
    def decorator_thread(func):
        def wrapper(upper_limit):
            t = Thread(target=func, args=(upper_limit, ), daemon=is_daemon)
            if is_daemon:
                print(f"Thread \"{t.name}\" started as daemon with parameter: {upper_limit}.\n")
                t.start()
            else:
                print(f"Thread \"{t.name}\" started as regular with parameter: {upper_limit}.\n")
                t.start()
        return wrapper
    return decorator_thread


@check_is_daemon(work_with_threads())
def some_function(upper_limit):
    print("Function started\n")
    for index in range(upper_limit):
        print(f"index {index} = {index ** upper_limit}")
    print("Function completed\n")


if __name__ == "__main__":
    some_function(MAX_VALUE)
