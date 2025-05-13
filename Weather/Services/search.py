

def get_city():
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

def get_country_code():
    while True:
        try:
            countrycode_input = input("Enter country code: ")
            if not isinstance(countrycode_input , str):
                raise ValueError("Please enter country code")
            if countrycode_input.strip() == "":
                raise ValueError("Can't be empty")
            break
        except ValueError as alert :
            print(f"Error: {alert}!")
    return countrycode_input

