def print_dots_on_a_die():
    dots = 1
    while dots < 7:
        print("".join("." * dots))
        dots += 1


print_dots_on_a_die()


def print_list_of_fruits():
    fruits = ["apple", "banana", "pear"]
    for fruit in fruits:
        print(fruit)


print_list_of_fruits()


def print_fruits_and_colors():
    fruits_and_colors = dict()
    fruits_and_colors["bananas"] = "yellow"
    fruits_and_colors["pears"] = "green"
    for fruit in fruits_and_colors:
        print(fruit + " are " + fruits_and_colors[fruit])
        print(f"{fruit} are {fruits_and_colors[fruit]}")


print_fruits_and_colors()
