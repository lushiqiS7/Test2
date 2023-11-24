def get_user_input():
    while True:
        user_input = input("Enter a sequence of numbers separated by commas: ")
        input_strings = user_input.split(',')
        try:
            input_floats = [float(value) for value in input_strings]
            return input_floats
        except ValueError:
            print("Invalid input. Please enter numeric values separated by commas.")


# Function to display the main menu
def display_main_menu():
    print("1. Calculate Average")
    print("2. Find Min and Max")
    print("3. Sort Temperatures")
    print("4. Calculate Median")
    print("5. Exit")


# Function to calculate the average of a list of floats
def calc_average(temperature_list):
    if not temperature_list:
        print("The list is empty. Cannot calculate the average.")
    else:
        average = sum(temperature_list) / len(temperature_list)
        print(f"Average: {average:.2f}")


# Function to find the minimum and maximum values in a list of floats
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


# Main function
def main():
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            temperature_list = get_user_input()
            calc_average(temperature_list)
        elif choice == '2':
            temperature_list = get_user_input()
            find_min_max(temperature_list)
        elif choice == '3':
            temperature_list = get_user_input()
            sort_temperature(temperature_list)
        elif choice == '4':
            temperature_list = get_user_input()
            calc_median_temperature(temperature_list)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
