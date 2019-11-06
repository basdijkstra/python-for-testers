# Exercise 5.1
# Create a function filter_the_ones() that creates a string
# variable funny_fruit with value "b1an11a11n1111a". Iterate
# over the characters in this string and only print those characters
# that are not equal to '1'. Use a for loop and an if statement.
def filter_the_ones():
    funny_fruit = "b1an11a11n1111a"
    for character in funny_fruit:
        if character != '1':
            print(character)

filter_the_ones()

# Exercise 5.2
# Create a function separate_numbers_and_letters() that creates
# a string alphanumeric with value "pr0gr4mm1ng". Iterate over
# the characters in this string and for each of them, print whether
# it is a letter (print "letter") or a number (print "number")
# Use isdigit() and an if-else construction
def separate_numbers_and_letters():
    alphanumeric = "pr0gr4mm1ng"
    for character in alphanumeric:
        if character.isdigit():
            print("number")
        else:
            print("letter")

separate_numbers_and_letters()