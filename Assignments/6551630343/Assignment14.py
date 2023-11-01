def main():
    
    degree_input = input("Please Enter Degree of Pascal Triangle: ")
    
    if not degree_input.isdigit():
        print("Please enter number from 0 only")
        return main()
    
    degree = int(degree_input)
    pascal_triangle = create_pascal_triangle(degree)
    
    degree_level_row = pascal_triangle[degree]
    
    print(degree_level_row)
    
    return


def create_pascal_triangle(degree):
    triangle = [[1]]

    # n is n-row
    for n in range(1, degree + 1):
        triangle.append([])

        # k is k-column
        for k in range(n + 1):
            if k == 0 or k == n:
                triangle[n].append(1)
            else:
                triangle[n].append(triangle[n - 1][k - 1] + triangle[n - 1][k])

    return triangle


if __name__ == "__main__":
    main()
