# MODULES
# You can import functions and variables from another module
from helper import validate_and_execute, user_input_message
import os
import logging

print(os.name)
logger = logging.getLogger("MAIN")
logger.info("THIS IS A LOGGER")

# DATA TYPES
print("200 is a number in string")  # string
print(2)  # integer
print(29.99)  # float


# CONCAT
print("20 days are " + str(20 * 24 * 60) + " minutes")  # concat


# VARIABLES
calculationToUnits = 24
nameOfUnit = "hours"
print(f"25 days are {25 * calculationToUnits} {nameOfUnit}")  # elegant concat
print(f"30 days are {30 * calculationToUnits} {nameOfUnit}")


# ENCAPSULATE
def days_to_units(days, message):
    print(f"--- {message} ---")
    print(f"{days} days are {days * calculationToUnits} {nameOfUnit}")
    print("--- Finish this encapsulate ---")


days_to_units(35, "First encapsulate")
days_to_units(30, "Second encapsulate")


# SCOPE
def scope_check(days):
    my_var = "variable inside a function"
    print(nameOfUnit)
    print(days)
    print(my_var)


scope_check(2)


# WHILE LOOP
user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    # print(user_input.split(", "))
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_units_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_units_dictionary)
    print(type(days_and_units_dictionary))
    # this function is from helper.py
    validate_and_execute(days_and_units_dictionary)
    # LIST AND FOR LOOPS
    # for num_of_days_element in set(user_input.split(", ")):
    #    validate_and_execute()


# BUILT-IN FUNCTIONS
print("some text")
input("enter value")
# set([1, 2, 3])
int("20")

"2, 3".split()
"text".upper()

# my_var_def = days_to_units_def(20)
# print(my_var_def)
