from CREATURE_BATTLE import *


if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == 1:
            create_creature()
        elif choice == 2:
            view_creatures()
        elif choice == 3:
            start_battle()
        elif choice == 4:
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-4.")
        
        input("\nPress Enter to continue...")

