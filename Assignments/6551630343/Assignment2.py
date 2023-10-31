import sys
sys.path.append('../../libs/')

import print_utils as printu


def main():
    printu.print_centered("Basic math formulas", 50, "\n")
    printu.print_repeat_str("#", 50, "\n")

    printu.print_centered("Area of Triangle", 50, "\n")
    printu.print_repeat_str("-", 50, "\n")
    get_triangle_area()
    printu.print_repeat_str("-", 50, "\n")

    printu.print_centered("Area of Rectangle", 50, "\n")
    printu.print_repeat_str("-", 50, "\n")
    get_rectangle_area()
    printu.print_repeat_str("-", 50, "\n")
    
    printu.print_centered(
            "The Longest Side of Right Triangle", 50, "\n")
    printu.print_repeat_str("-", 50, "\n")
    get_right_triangle_longest_side()
    printu.print_repeat_str("-", 50, "\n")
    
    printu.print_centered(
            "The Solution of Quadratic Formula", 50, "\n")
    printu.print_repeat_str("-", 50, "\n")
    get_quadratic_root()
    printu.print_repeat_str("-", 50, "\n")
    
    printu.print_centered("Distance of 2 points", 50, "\n")
    printu.print_repeat_str("-", 50, "\n")
    get_distance_of_points()
    printu.print_repeat_str("-", 50, "\n")


def calc_triangle_area(base: float, height: float):
    return round(base * height / 2, 2)


def get_triangle_area():
    b = float(input("Enter Base:"))
    h = float(input("Enter Height:"))

    print("The area is", calc_triangle_area(b, h))


def calc_rectangle_area(length, width):
    return round(length * width, 2)


def get_rectangle_area():
    l = float(input("Enter Length:"))
    w = float(input("Enter Width:"))

    print("The area is", calc_rectangle_area(l, w))


def calc_right_triangle_longest_side(sideA, sideB):
    return round((sideA ** 2 + sideB ** 2) ** 0.5, 2)


def get_right_triangle_longest_side():
    a = float(input("Enter length of the 1st size:"))
    b = float(input("Enter length of the 2nd size:"))

    print(
            "The length of the longest side is", 
            calc_right_triangle_longest_side(a, b))


def calc_quadratic_root(a, b, c):
    x = (b ** 2) - (4 * a * c)
    y = x ** 0.5
    z = (2 * a)
    sol1 = (-b + y) / z
    sol2 = (-b - y) / z

    return (sol1, sol2)


def get_quadratic_root():
    c = float(input("Enter Constant(\"c\"):"))
    b = float(input("Enter Coefficient of Linear Term(\"b\"):"))
    a = float(input("Enter Coefficient of Quadratic Term(\"a\"):"))

    (sol1, sol2) = calc_quadratic_root(a, b, c)

    print("The 1st solution is x =", sol1)
    print("The 2nd solution is x =", sol2)


def calc_distance_of_points(x1, y1, x2, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)


def get_distance_of_points():
    x1 = float(input("Enter x of the 1st point:"))
    y1 = float(input("Enter y of the 1st point:"))
    x2 = float(input("Enter x of the 2nd point:"))
    y2 = float(input("Enter y of the 2nd point:"))

    print(
            "The distance is", 
            calc_distance_of_points(x1, y1, x2, y2))


if __name__ == "__main__":
    main()
