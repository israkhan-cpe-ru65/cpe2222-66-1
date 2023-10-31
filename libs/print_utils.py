import string_utils

def print_repeat_str(str, times, ending = ""):
    print(string_utils.make_repeat_str(str, times), end = "")
    print("", end = ending)

def print_centered(message, width, ending = ""):
    paddingLength = (width - len(message)) // 2
    print_repeat_str(" ", paddingLength)
    print(message, end = "")
    print_repeat_str(" ", paddingLength if paddingLength % 2 == 0 else paddingLength + 1, ending)

def print_left(string, width, ending = ""):
    print(string, end = "")
    print_repeat_str(" ", width - len(string), ending)
    
def print_right(string, width, ending = ""):
    print_repeat_str(" ", width - len(string), "")
    print(string, end = ending)
