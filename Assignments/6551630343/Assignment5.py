import sys
sys.path.append('../../libs/')

import string_utils as stringu
import print_utils as printu


def main():
    str_a = input("Please enter the string A :")
    str_b = input("Please enter the string B :")
    char_set_str_a = set(str_a)
    char_set_str_b = set(str_b)
    char_set_of_a_and_b = make_duplicate_char_set(char_set_str_a, char_set_str_b)
    
    printu.print_repeat_str("-", 50, "\n")
    print(
        "A number of character in A is",
        count_unique_char(str_a))
    print(
        "A number of character in B is",
        count_unique_char(str_b))
    print(
        "A number of character in both A and B is",
        len(char_set_of_a_and_b))
    print(
        "Characters in A but not in B is",
        make_diff_char_set(char_set_str_a, char_set_str_b))
    print(
        "Characters in B but not in A is",
        make_diff_char_set(char_set_str_b, char_set_str_a))
    print(
        "Characters in A or B but not in both A and B is",
        make_symmetric_diff_char_set(char_set_str_b, char_set_str_a))
    print(
        "All Characters in A or B is",
        make_union_char_set(char_set_str_b, char_set_str_a))
    
    return


def make_unique_char_set(string, case_sensitive = True):
    str = string if case_sensitive else string.lower()
    return set(str)


def count_unique_char(string):
    return len(make_unique_char_set(string))


def make_unique_word_set(string, case_sensitive = True):
    str = string if case_sensitive else string.lower()
    return set(str.split())


def count_unique_words(string):
    return len(make_unique_word_set)


def make_duplicate_char_set(*strings_sets: [set]):
    dup = set(strings_sets[0])

    for i in range(len(strings_sets)):
        dup.intersection_update(strings_sets[i])
        
    return dup 


def make_diff_char_set(char_set_a: set, char_set_b: set):
    return char_set_a.difference(char_set_b)


def make_symmetric_diff_char_set(char_set_a: set, char_set_b: set):
    return char_set_a.symmetric_difference(char_set_b)


def make_union_char_set(*strings: [set]):
    union_set = set(strings[0])

    for i in range(1, len(strings)):
        union_set.update(strings[i])
        
    return union_set


if __name__ == "__main__":
    main()
