def is_right_triangle(a, b, c)
    # Check if the triangle is a right-angled triangle using Pythagorean theorem
    sides = [a, b, c]
    sides.sort()

    if sides[0]  2 + sides[1]  2 == sides[2]  2
        return True
    else
        return False

def calculate_area(a, b, c)
    # Calculate the area of the triangle using Heron's formula
    s = (a + b + c)  2
    area = (s  (s - a)  (s - b)  (s - c))  0.5
    return area

def get_positive_float_input(prompt)
    while True
        try
            value = float(input(prompt))
            if value  0
                return value
            else
                print(Please enter a positive number.)
        except ValueError
            print(Invalid input. Please enter a valid number.)

def main()
    print(Welcome to the Triangle Analysis Program!)
    
    # Input lengths of the triangle sides
    print(nEnter the lengths of the triangle sides)
    a = get_positive_float_input(Side a )
    b = get_positive_float_input(Side b )
    c = get_positive_float_input(Side c )

    # Check if it's a right-angled triangle
    if is_right_triangle(a, b, c)
        print(The triangle is a right-angled triangle.)
    else
        print(The triangle is not a right-angled triangle.)

    # Calculate and display the area of the triangle
    area = calculate_area(a, b, c)
    print(fThe area of the triangle is {area.2f})

if __name__ == __main__
    main()
