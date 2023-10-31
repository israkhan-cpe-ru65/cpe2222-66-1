import sys
sys.path.append('../../libs/')

import print_utils as printu
import string_utils as stringu

LINE_LENGTH = 50
COL1_LENGTH = 30
COL2_LENGTH = 10
COL3_LENGTH = 10


def main():
    products = get_products_input(3)
    print_inventory(products) 


def get_products_input(repeat = 1):
    products = []
    
    for i in range(repeat):
        ordinal_number = stringu.make_ordinal_number(i + 1)
        product_name = input(
            "Enter The " + ordinal_number + " Product Name:")
        product_price = float(input("Enter Price of Product:"))
        product_quantity = int(input("Enter Quantity of Product:"))

        product = [
            tuple([product_name, product_price, product_quantity])
        ]
        products += product

    return products


def print_inventory(products: tuple):
    printu.print_repeat_str("-", LINE_LENGTH, "\n")
    printu.print_centered("Inventory", LINE_LENGTH, "\n")    
    printu.print_repeat_str("-", LINE_LENGTH, "\n")
    
    printu.print_centered("Item", COL1_LENGTH, "")
    printu.print_centered("Price", COL2_LENGTH, "")
    printu.print_centered("Quantity", COL3_LENGTH, "\n")
    printu.print_repeat_str("-", LINE_LENGTH, "\n")

    total_quantity = sum_products_quantity(products)

    print_product_list(products)

    printu.print_repeat_str("-", LINE_LENGTH, "\n")
    printu.print_right(
        "Total Quantity = " + str(total_quantity), LINE_LENGTH, "\n")
    printu.print_repeat_str("-", LINE_LENGTH, "\n")


def sum_products_quantity(products):
    sum = 0

    for product in products:
        (name, price, quantity) = product
        sum += quantity
        
    return sum


def print_product_list(products):
    for product in products:
        (name, price, quantity) = product

        printu.print_left(name, COL1_LENGTH)
        printu.print_right(str(price) + "  ", COL2_LENGTH)
        printu.print_right(str(quantity), COL3_LENGTH)
        print()


if __name__ == "__main__":
    main()
