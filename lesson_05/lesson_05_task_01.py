from threading import Thread

thread_data = []
MAX_VALUE = 500


def check_is_daemon(thr_data):
    def decorator_thread(func):
        def wrapper():
            thr_data[0][0].daemon = thr_data[0][1]
            if thr_data[0][1]:
                print(f"Thread \"{thr_data[0][0].name}\" started as daemon. State {thr_data[0][1]}\n")
                thr_data[0][0].start()
            else:
                print(f"Thread \"{thr_data[0][0].name}\" started as regular. State {thr_data[0][1]}\n")
                thr_data[0][0].start()
        return wrapper
    return decorator_thread


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


@check_is_daemon(thread_data)
def nothing_to_do():
    pass


def some_function():
    print("Function started\n")
    for index in range(MAX_VALUE):
        print(f"index {index} = {index ** MAX_VALUE}")
    print("Function completed\n")


if __name__ == "__main__":
    is_daemon = work_with_threads()
    thread_data.append((Thread(target=some_function), is_daemon))
    nothing_to_do()
