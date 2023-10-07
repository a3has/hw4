import time

def timestamp(text):
    def wrapper():
        print(time.ctime())
        text()
    return wrapper
    