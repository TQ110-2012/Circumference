def calculate_circumference(radius):
    return 2 * 3.14 * radius


radius = float(input("Enter the radius of the circle: "))
circumference = calculate_circumference(radius)
print("The circumference of the circle is:", circumference)