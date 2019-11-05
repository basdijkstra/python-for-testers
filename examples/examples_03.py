def a_function_can_return_a_value():
    return "a_value"

returned_value = a_function_can_return_a_value()
print("The function returned " + returned_value)

def a_function_can_return_multiple_values():
    return "value_one", "value_two"

value_one, value_two = a_function_can_return_multiple_values()
print("The function returned " + value_one + " and " + value_two)

def arithmetic(number):
    print("Addition: " + str(number + 1))
    print("Subtraction: " + str(number - 1))
    print("Multiply: " + str(number * 2))
    print("Exponentials: " + str(number ** 2))
    print("Division: " + str(number / 2))
    print("Modulo: " + str(number % 2))

arithmetic(5)