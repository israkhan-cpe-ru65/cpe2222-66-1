import sys
sys.path.append('../../libs/')

import string_utils as stringu


def main():
    s1 = "Python is a powerful high-level, \
            object-oriented programming language \
            created by Guido van Rossum."
    s2 = "It has simple easy-to-use syntax,\
            making it the perfect language for someone\
            trying to learn computer programming for the first time." 
    s3 = "Professionally, Python is great for\
            backend web development, data analysis,\
            artificial intelligence, and scientific computing."

    s1_secret_positions = [20, 3, 81]
    s2_secret_positions = [44, 4]
    s3_secret_positions = [31, 9]
    
    string1 = stringu.remove_spaces_to_one(s1)
    string2 = stringu.remove_spaces_to_one(s2)
    string3 = stringu.remove_spaces_to_one(s3)

    str_secret1 = find_secret_char(
        string1, s1_secret_positions, "right", True)
    str_secret2 = find_secret_char(
        string2, s2_secret_positions, "left")
    str_secret3 = find_secret_char(
        string3, s3_secret_positions, "right")
    
    print("Total characters in string s1, s2 and s3 are", 
          count_char_of_strings(string1, string2, string3), "characters")
    print("Total words in string s1, s2 and s3 are", 
          count_word_of_strings(string1, string2, string3), "words")
    print("The secret code is", 
          "".join(str_secret1 + str_secret2 + str_secret3))


def count_char_of_strings(*strings):
    sum = 0

    for string in strings:
        sum += stringu.count_chars(string)

    return sum


def count_word_of_strings(*strings):
    sum = 0

    for string in strings:
        sum += stringu.count_words(string)

    return sum
    

def find_secret_char(
        string, secretChars: tuple, 
        orientation = "left", use_space = False):

    str = string[::-1] if (orientation == "right") else string
    str = str if use_space else str.replace(" ", "")
    secrets = []
    
    for secretIndex in secretChars:
        secrets.append(str[secretIndex - 1])

    return secrets


if __name__ == "__main__":
    main()
    