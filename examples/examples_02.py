def this_is_a_function():
    print("My function works")

this_is_a_function()

def this_is_a_function_with_a_parameter(parameter):
    print("The value of the parameter is " + parameter)

this_is_a_function_with_a_parameter("parameter_value")

def this_is_a_function_with_multiple_parameters(parameter_one, parameter_two):
    print("Parameter one is " + parameter_one + " and parameter two is " + parameter_two)

this_is_a_function_with_multiple_parameters("one", "two")

def this_is_a_function_with_a_default_value_for_a_parameter(parameter_one, parameter_two="two"):
    print("Parameter one is " + parameter_one + " and parameter two is " + parameter_two)

this_is_a_function_with_a_default_value_for_a_parameter("one")

def you_can_refer_to_parameters_by_name_too(parameter_one, parameter_two):
    print("Parameter one is " + parameter_one + " and parameter two is " + parameter_two)

you_can_refer_to_parameters_by_name_too(parameter_two="two", parameter_one="one")
