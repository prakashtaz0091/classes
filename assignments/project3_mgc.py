import random

# ------------------- Game Functions -------------------


def number_guessing_game():
    """Random number guessing game"""
    pass


def quiz_game():
    """Simple quiz game"""
    pass


def rock_paper_scissors():
    """Rock, Paper, Scissors game"""
    pass


def show_menu():
    print("""
    1. Number Guessing Game
    2. Quiz Game
    3. Rock, Paper, Scissors
    4. Exit
    """)


# ------------------- Main Program -------------------

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        number_guessing_game()
    elif choice == "2":
        quiz_game()
    elif choice == "3":
        rock_paper_scissors()
    elif choice == "4":
        print("Thanks for playing. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
