def make_repeat_str(str, times):
    output = ""
    for i in range(times):
        output += str
    return output

def make_ordinal_number(number):
    if number == 1:
        return "1st"
    elif number == 2:
        return "2nd"
    elif number == 3:
        return "3rd"
    else:
        return str(number) + "th"   
    

def remove_spaces_to_one(string):
    return " ".join(string.split())


def count_chars(string):
    return len(string)


def count_words(string):
    return len(string.split())
