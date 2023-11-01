def main():
    number_input = input("Enter a number for roman number conversion:")
    
    if number_input.isdecimal():
        number = int(number_input)
        
        if number > 39 or number < 1:
            return
        else:
            roman_numeral = match_int_to_roman_numeral(number)
            
            print(f"The roman number of {number} is \" {roman_numeral} \"")
            main()



def create_roman_numeral_dict():
    return {
        "M" : 1000, 
        "CM": 900, 
        "D" : 500, 
        "CD": 400, 
        "C" : 100, 
        "XC": 90, 
        "L" : 50, 
        "XL": 40,
        "X" : 10,
        "IX": 9,
        "V" : 5,
        "IV": 4,
        "I" : 1
    }


def match_int_to_roman_numeral(number: int):
    roman_numeral_dict = create_roman_numeral_dict()
    roman_numeral = ""
    
    for key, value in roman_numeral_dict.items():
        while number >= value:
            roman_numeral += key
            number -= value
    
    return roman_numeral


if __name__ == "__main__":
    main()
