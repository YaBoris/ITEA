from threading import Thread
import requests
from urllib.parse import urlparse
import os
# from threading import enumerate
from lesson_05.lesson_05_task_02.constants import LINKS_COUNT
from lesson_05.lesson_05_task_02.constants import list_urls


def set_urls():
    if not len(list_urls):
        for i in range(LINKS_COUNT):
            print(f"Enter {i+1} link:")
            url_string = input()
            list_urls.append(url_string)
    return list_urls


def get_files(links):
    def decorator_thread(func):
        def wrapper(download_url):
            for url_name in links:
                t = Thread(target=func, args=(url_name, ))
                t.start()
        return wrapper
    return decorator_thread


@get_files(set_urls())
def download_data(download_url):
    parsed_url = urlparse(download_url)
    filename = os.path.basename(parsed_url.path)
    try:
        with open(filename, "wb") as fh:
            print(f"File {filename} start downloading")
            data_thread = requests.get(download_url)
            fh.write(data_thread.content)
            print(f"File {filename} downloaded!")
    except IOError as fh:
        print(f"Error: {fh}! Can't work with file: {filename}\n")
