# ACCEPTING USER INPUT
def days_to_units_def(days, conversion_unit):
    if conversion_unit == "hours":
        return f"{days} days are {days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{days} days are {days * 24 * 60} minutes"
    else:
        return "Unsupported unit"


def validate_and_execute(days_and_units_dictionary):
    try:
        user_input_number = int(days_and_units_dictionary["days"])
        if user_input_number > 0:
            value_input_def = days_to_units_def(user_input_number, days_and_units_dictionary["unit"])
            print(value_input_def)
        elif user_input_number == 0:
            print("You entered a 0, please enter a positive number")
        else:
            print(f"You entered a negative number {user_input_number}, please enter a positive number")
    except ValueError:
        print("Your input is not a valid number")


user_input_message = "Hello user, enter a number of days as a comma separated list and I will convert it to hours\n"
