from Weather.Views.menu import display_menu
from Weather.Controllers.handlechoice import handle_choice
from Weather.Valids.choice_valid import valid_choices
def main():

    while True:
        display_menu()
        choice = input("Enter your choice:")
        valid_choice = valid_choices
        if choice == '0':
            print("Exiting program.")
            break
        elif choice in valid_choice:
            handle_choice(choice)
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()