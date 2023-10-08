def allcaps(text):
    def wrapper():
        temp = text()
        cap = temp.upper()
        print(cap)
    return wrapper