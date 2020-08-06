from threading import Thread
from time import sleep


def decorator_thread(func):
    def wrapper(thread_name, is_daemon):
        t = Thread(target=func, name=thread_name, daemon=is_daemon)
        print(f"Thread \"{thread_name}\" before sleep")
        t.start()
        print(f"Thread \"{thread_name}\" after sleep")
    return wrapper


@decorator_thread
def some_function():
    sleep(3)
    print("Function is finished")


def work_with_threads():
    print("Call new thread: ")
    thread_name = input()
    print("This thread is daemon? Yes/No")
    while True:
        daemon_status = input()
        if daemon_status == 'Yes':
            is_daemon = True
            break
        elif daemon_status == 'No':
            is_daemon = False
            break
        else:
            print("Enter correct option - \'Yes\' or \'No\'")
    some_function(thread_name, is_daemon)
    print("Process is finished")


if __name__ == "__main__":
    work_with_threads()
