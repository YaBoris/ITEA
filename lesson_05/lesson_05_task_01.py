from threading import Thread
from time import sleep

thread_data = []


def check_is_daemon(thr_data):
    def decorator_thread(func):
        def wrapper():
            t = Thread(target=func, name=thread_data[0], daemon=thr_data[1])
            print(f"Thread \"{thread_data[0]}\" before sleep")
            t.start()
            print(f"Thread \"{thread_data[0]}\" after sleep")
        return wrapper
    return decorator_thread


def work_with_threads():
    print("Call new thread: ")
    thr_name = input()
    print(f"This thread \"{thr_name}\" is daemon? Yes/No")
    while True:
        daemon_status = input()
        if daemon_status == "Yes":
            daemon = True
            break
        elif daemon_status == "No":
            daemon = False
            break
        else:
            print("Enter correct option - \'Yes\' or \'No\'")
    return thr_name, daemon


@check_is_daemon(thread_data)
def some_function():
    sleep(3)
    print("Function is finished")


if __name__ == "__main__":
    thread_info = work_with_threads()
    thread_data.append(thread_info[0])
    thread_data.append(thread_info[1])
    some_function()
