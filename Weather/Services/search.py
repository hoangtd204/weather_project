import requests

def search():
    while True:
        try:
            city_input = input("Enter City: ")
            if not isinstance(city_input , str):
                raise ValueError("Please enter city name")
            if city_input.strip() == "":
                raise ValueError("Can't be empty")
            break
        except ValueError as alert :
            print(f"Error: {alert}!")

    return city_input


