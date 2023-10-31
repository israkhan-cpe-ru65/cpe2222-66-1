import sys
sys.path.append('../../libs/')

import print_utils as printu
import string_utils as stringu

TITLE_MESSAGE = " Drawing the square rectangular by \"#\" "
INSTRUCTION_MSG1 = "[To quit this program by pressing \"0\"]"
INSTRUCTION_MSG2 = "Please enter the size:"
INSTRUCTION_MSG3 = "Please enter positive integer number or \"0\" to quit."
DASH_REPEAT = 9
TYPE = "outline_sharp"
# TYPE = "outline_dot"
# TYPE = "outline_coord"
# TYPE = "fill_sharp"


def main():
    ending_dash_repeat = len(TITLE_MESSAGE) + (DASH_REPEAT * 2)
    size = -1
    
    printu.print_repeat_str("-", DASH_REPEAT)
    print(TITLE_MESSAGE, end="")
    printu.print_repeat_str("-", DASH_REPEAT, "\n")
    
    print(INSTRUCTION_MSG1)
    printu.print_repeat_str("-", ending_dash_repeat, "\n")

    while size != 0:
        size_input = prompt_user_input()

        if size_input.isdecimal():
            size = int(size_input)

            match TYPE:
                case "outline_coord":
                    print_square_outline_with_coord(size)
                case "outline_dot":
                    print_square_outline_with_dot(size)
                case "fill":
                    print_square(size)
                case _: #outline_sharp
                    print_square_outline_with_sharp(size)
        else:
            print(INSTRUCTION_MSG3)

            continue


def prompt_user_input():
    return input(INSTRUCTION_MSG2)
    

def render_square(func):
    def _func(size):
        for i in range(size):
            for j in range(size):
                func(size, i, j)
            print()
    return _func


@render_square
def print_square(*args):
    print("#", end="")


@render_square
def print_square_outline_with_sharp(size, i, j):
    if ((i == 0 or i == size - 1) 
    or (j == 0 or j == size - 1)):
        print("#", end="")
    else:
        print(" ", end="")


@render_square
def print_square_outline_with_dot(size, i, j):
    if ((i == 0 or i == size - 1) 
    or (j == 0 or j == size - 1)):
        print(".", end="")
    else:
        print(" ", end="")


@render_square
def print_square_outline_with_coord(size, i, j):
    # TODO: Add padding fill
    if ((i == 0 or i == size - 1) 
    or (j == 0 or j == size - 1)):
        print(f'[{i},{j}]', end="")
    else:
        # TODO: Change blank space to padding fill
        print("[   ]", end="")


if __name__ == "__main__":
    main()
