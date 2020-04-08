# Exercise 4.1
# Create a function count_to_ten that prints the numbers 1 through 10
# Use a while loop
def count_to_ten():
    counter = 1
    while counter < 11:
        print(str(counter))
        counter += 1


count_to_ten()

# Exercise 4.2
# Create a function list_my_cars that creates a list my_cars of car brands
# with three cars in there (e.g. Ford, Alfa Romeo, Maserati)
# Use a for loop to iterate over the list and print each car brand
def list_my_cars():
    my_cars = ["Ford", "Alfa Romeo", "Maserati"]
    for car in my_cars:
        print(car)


list_my_cars()

# Exercise 4.3
# Create a function list_my_cars_with_colors that creates a dictionary
# of cars, where the key-value pairs are car brands and their colors, respectively
# (e.g., Ford - blue, Alfa Romeo - red, Maserati - black)
# Use a for-loop to iterate over this dictionary and print "My <brand> is <color>"
# for each of the cars.
def list_my_cars_with_colors():
    cars_and_colors = dict()
    cars_and_colors["Ford"] = "blue"
    cars_and_colors["Alfa Romeo"] = "red"
    cars_and_colors["Maserati"] = "black"
    for car in cars_and_colors:
        print("My " + car + " is " + cars_and_colors[car])
        print("My %s is %s" % (car, cars_and_colors[car]))


list_my_cars_with_colors()

# Exercise 4.4
# Try and print the same statement again in Exercise 4.3, but now
# use string formatting. Is that simpler or more complex for you?
