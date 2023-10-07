def allcaps(text):
    def wrapper():
        temp = text()
        cap = temp.upper()
        return cap
    return wrapper