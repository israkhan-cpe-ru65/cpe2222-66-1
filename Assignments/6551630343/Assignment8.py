SCRABBLE = [
#letter,    point,  amount, ratio
    'a',    1,      9,      4.8,
    'b',    3,      2,      3.2,    
    'c',    3,      2,      3.2,    
    'd',    2,      4,      4.3,    
    'e',    1,      12,     6.4,   
    'f',    4,      2,      4.3,    
    'g',    2,      3,      3.2,    
    'h',    4,      2,      4.3,    
    'i',    1,      9,      4.8,    
    'j',    8,      1,      4.3,    
    'k',    5,      1,      2.7,    
    'l',    1,      4,      2.1,    
    'm',    3,      2,      3.2,    
    'n',    1,      6,      3.2,    
    'o',    1,      8,      4.3,    
    'p',    3,      2,      3.2,    
    'q',    10,     1,      5.3,   
    'r',    1,      6,      3.2,    
    's',    1,      4,      2.1,    
    't',    1,      6,      3.2,    
    'u',    1,      4,      2.1,    
    'v',    4,      2,      4.3,    
    'w',    4,      2,      4.3,    
    'x',    8,      1,      4.3,    
    'y',    4,      2,      4.3,    
    'z',    10,     1,      5.3
]

INVERVAL = 4

def main():

    print("The highest point in the scrabble game:")
    print_4_highest_point(SCRABBLE)
    
    print("The highest amount in the scrabble game:")
    print_4_highest_amount(SCRABBLE)
    
    print("The lowest ratio in the scrabble game:")
    print_4_lowest_ratio(SCRABBLE)

    return


def print_4_highest_point(scrabble):

    items = get_4_highest_points(scrabble)

    print("        1)", items[0][0],
          "with", items[0][1], "points.")
    print("        2)", items[1][0],
          "with", items[1][1], "points.")
    print("        3)", items[2][0],
          "with", items[2][1], "points.")
    print("        4)", items[3][0],
          "with", items[3][1], "points.")


def print_4_highest_amount(scrabble):
    items = get_4_highest_amounts(scrabble)

    print("        1)", items[0][0],
          "with", items[0][1], "pieces.")
    print("        2)", items[1][0],
          "with", items[1][1], "pieces.")
    print("        3)", items[2][0],
          "with", items[2][1], "pieces.")
    print("        4)", items[3][0],
          "with", items[3][1], "pieces.")


def print_4_lowest_ratio(scrabble):
    items = get_4_lowest_ratios(scrabble)

    print("        1)", items[0][0],
          "with", items[0][1], "points.")
    print("        2)", items[1][0],
          "with", items[1][1], "points.")
    print("        3)", items[2][0],
          "with", items[2][1], "points.")
    print("        4)", items[3][0],
          "with", items[3][1], "points.")

        
def get_4_highest_points(scrabble):
    start_pos = 1
    sorting = "asc"
    return get_four_letter_selection_pairs(scrabble, start_pos, sorting)


def get_4_highest_amounts(scrabble):
    start_pos = 2
    sorting = "asc"
    return get_four_letter_selection_pairs(scrabble, start_pos, sorting)


def get_4_lowest_ratios(scrabble):
    start_pos = 3
    sorting = "desc"
    return get_four_letter_selection_pairs(scrabble, start_pos, sorting)


def get_four_letter_selection_pairs(scrabble, start_pos, sorting = "asc"):
    scrabble_length = len(scrabble)
    is_reverse = False if (sorting == "desc") else True

    interested_cols = scrabble[start_pos:scrabble_length:INVERVAL]
    sorted_interested_cols = sorted(interested_cols, reverse=is_reverse)
    four_selected_items = sorted_interested_cols[0:4]

    index_of_selected_items = []

    #1st
    index_of_selected_items.append(
        interested_cols.index(
            four_selected_items[0]))
    
    #2nd
    index_of_selected_items.append(
        interested_cols.index(
            four_selected_items[1],
                0 if (four_selected_items[1] != four_selected_items[0])
                else index_of_selected_items[0] + 1))
    #3rd
    index_of_selected_items.append(
        interested_cols.index(
            four_selected_items[2],
                0 if (four_selected_items[2] != four_selected_items[1])
                else index_of_selected_items[1] + 1))
    #4th
    index_of_selected_items.append(
        interested_cols.index(
            four_selected_items[3],
                0 if (four_selected_items[3] != four_selected_items[2])
                else index_of_selected_items[2] + 1))
    
    index_of_letters = map_item_index_to_letter(
        index_of_selected_items, INVERVAL)

    return [ #[[letter, point]]
        [f'"{scrabble[index_of_letters[0]]}"', 
                    four_selected_items[0]],
        [f'"{scrabble[index_of_letters[1]]}"', 
                    four_selected_items[1]],
        [f'"{scrabble[index_of_letters[2]]}"', 
                    four_selected_items[2]],
        [f'"{scrabble[index_of_letters[3]]}"', 
                    four_selected_items[3]]
    ]


def map_item_index_to_letter(indice, step, offset = 0):
    indice[:] = map(lambda index: (index * step) + offset, indice)
    return indice


if __name__ == "__main__":
    main()
