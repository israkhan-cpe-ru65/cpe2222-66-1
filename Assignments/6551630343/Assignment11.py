def main():
    print("Making a list of Factorial series of n")
    
    n_input = input("Enter 'n' of Factorial number:")

    if not n_input.isdecimal():
        print("Please enter 'n' as a positive integer number")
        main()
    else:
        n = int(n_input)

        if (n > 0): # Require this condition as the assignment not require 0!
            # Option 1: Using for loop.
            factorial_list = generate_factorial_list(n)
            
            # Option 2: Using recursive function.
            # factorial_list = generate_factorial_recursive(n, list())
            
            factorial_list.remove(1) # This is a workaround as the assignment not require 0!
            
            print(f"A list of Factorial series of {n} is", factorial_list)
        else:
            print("Please enter 'n' > 1")
            main()
            

def generate_factorial_list(n):
    factorial_list = []

    for i in range(0, n + 1):
        if (i == 0 or i == 1):
            factorial_list.append(1)
        else:
            n_factorial = i * factorial_list[i - 1] 
            factorial_list.append(n_factorial)

    return factorial_list


def generate_factorial_recursive(n, factorial_list: list):
    i = len(factorial_list)

    if (i == 0 or i == 1):
        factorial_list.append(1)
    elif (i <= n):
        n_factorial = i * factorial_list[i - 1]
        factorial_list.append(n_factorial)
    else:
        return factorial_list
    
    return generate_factorial_recursive(n, factorial_list)


if __name__ == "__main__":
    main()
