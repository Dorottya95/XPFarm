def high_and_low(numbers):
    number_list = list(numbers.split(" "))
    print(min(number_list))
    print(str(max(number_list)) + " " + str(min(number_list)))
    return str(max(number_list)) + " " + str(min(number_list))


high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")