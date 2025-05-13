from Services.search_current_weather import search_current_weather
from  Services.get_history import get_search_history
def handle_choice(choice):
    if choice == '1':
        search_current_weather()
    elif choice == '2':
        print("History Searching")
        for city in get_search_history():

            print("📍", city)
    else:
        print("Invalid choice. Please try again!")

