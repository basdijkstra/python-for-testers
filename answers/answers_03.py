# Exercise 3.1
# Create a function square() that takes a parameter and returns its square
# e.g. square(6) returns 36
# Call your function and print its return value to see if it works
def square(number):
    return number * number

square_value = square(6)
print("The square of 6 is " + str(square_value))
# or
print("The square of 6 is " + str(square(6)))

# Exercise 3.2
# Create a function square_and_square_root() that takes a parameter and
# returns both its square and its square root
# Call your function and print their return values to see if it works
def square_and_square_root(number):
    square_value = number * number
    square_root = number ** 0.5
    return square_value, square_root

sqv, sqrt = square_and_square_root(5)
print("The square of 5 is " + str(sqv) + " and the square root of 5 is " + str(sqrt))