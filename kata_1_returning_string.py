def greet(name):
    if check_string(name):
        return print("Hello, " + name + " how are you doing today?")


def check_string(input):
    return print(isinstance(input, str))