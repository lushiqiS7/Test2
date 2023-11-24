# Function to display the main menu
def display_main_menu():
    print("Enter some numbers separated by commas 5, 67, 32")


# Function to get user input as a list of floats
def get_user_input():
    user_input = input("Enter a sequence of numbers separated by commas: ")
    input_strings = user_input.split(',')
    try:
        input_floats = [float(value) for value in input_strings]
        return input_floats
    except ValueError:
        print("Invalid input. Please enter numeric values separated by commas.")
        return get_user_input()


# Function to calculate the average of a list of floats
def calc_average(temperature_list):
    if not temperature_list:
        print("The list is empty. Cannot calculate the average.")
    else:
        average = sum(temperature_list) / len(temperature_list)
        print(f"Average: {average:.2f}")


# Function to find the minimum and maximum values in a list of floa
def find_min_max(temperature_list):
    if not temperature_list:
        print("The list is empty. No minimum and maximum values to find.")
    else:
        min_temp = min(temperature_list)
        max_temp = max(temperature_list)
        print(f"Minimum Temperature: {min_temp}")
        print(f"Maximum Temperature: {max_temp}")


# Function to sort a list of floats in ascending order
def sort_temperature(temperature_list):
    if not temperature_list:
        print("The list is empty. Nothing to sort.")
    else:
        sorted_temperatures = sorted(temperature_list)
        print("Sorted Temperatures: ", sorted_temperatures)


# Function to calculate the median temperature from a list of floats
def calc_median_temperature(temperature_list):
    if not temperature_list:
        print("The list is empty. Cannot calculate the median.")
    else:
        sorted_temperatures = sorted(temperature_list)
        n = len(sorted_temperatures)
        if n % 2 == 1:
            median = sorted_temperatures[n // 2]
        else:
            median = (sorted_temperatures[n // 2 - 1] + sorted_temperatures[n // 2]) / 2
        print(f"Median Temperature: {median}")
