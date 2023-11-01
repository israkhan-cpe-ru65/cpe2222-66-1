import sys
sys.path.append('../../libs/')

import print_utils as printu
import math

AVAILABLE_SHAPES = ["circle", "square", "triangle"]

def main():
    shape = handle_shape_selection()
    dict_key = handle_dict_key_input()
    
    area = round(select_calculation(shape, dict_key), 2)
    printu.print_repeat_str("-", 50, ending = "\n")
    print(f"The area of {shape.upper()} is {area}")
    printu.print_repeat_str("-", 50, ending = "\n")
    
    main()
    return


def handle_shape_selection():
    print("Enter the geometry shape for an area calculation")
    print("[Circle, Square, Triangle]")

    shape_input = input(
        "[Enter something else to exit this program]:").lower()
    
    if shape_input not in AVAILABLE_SHAPES:
        exit()
    
    return shape_input


def handle_dict_key_input():
    print("Enter the dictionary key")
    
    dict_key_input = input("[1 - 100]:")
    
    if not (dict_key_input.replace('.','', 1).isdigit()
        and dict_key_input.count('.') < 2):
        exit()
    
    dict_key = math.floor(float(dict_key_input))
        
    if dict_key < 1 or dict_key > 100:
        print("!!! The key is out of scope !!!")
        exit()
    
    return dict_key
    

def select_calculation(shape, dict_key):
    match shape:
        case "circle":
            return calc_circle_area(dict_key)
        case "square":
            return calc_square_area(dict_key)
        case "triangle":
            return calc_eq_triangle_area(dict_key)
        case _:
            exit()


def calc_circle_area(radius):
    return math.pi * radius ** 2


def calc_square_area(side):
    return side ** 2


def calc_eq_triangle_area(length):
    return (3 ** 0.5) * (length ** 2) / 4


if __name__ == "__main__":
    main()
