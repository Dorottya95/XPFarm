def greet(name):
    if check_string(name):
        message = "Hello, " + name + " how are you doing today?"
        return message


def check_string(input):
    return isinstance(input, str)


