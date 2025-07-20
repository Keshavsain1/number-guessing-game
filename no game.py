import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_feedback(guess, number):
    diff = abs(guess - number)
    if guess == number:
        return "Correct! You got it! 🏆"
    elif diff <= 3:
        return "Too close but a bit high 🔥" if guess > number else "Too close but a bit low 🔥"
    elif diff <= 7:
        return "Little bit high 🔺" if guess > number else "Little bit low 🔻"
    else:
        return "Too high 📈" if guess > number else "Too low 📉"

def game():
    ft = True
    username = input("Enter your name: ")

    mode = 'easy'
    while True:
        if ft:
            print("🎮 Welcome To No. Guessing Gaming 🎮")
            ft = False

        change = input("Do you want to change difficulty? (yes/no): ").lower()
        if change == 'yes':
            mode = input("Choose mode: easy / medium / hard: ").lower()

        if mode == 'easy':
            tries, limit = 10, 100
        elif mode == 'medium':
            tries, limit = 20, 500
        elif mode == 'hard':
            tries, limit = 50, 1000
        else:
            print("Invalid mode. Defaulting to easy.")
            tries, limit = 10, 100

        number = random.randint(1, limit)
        print(f"\nAlright {username}, let's begin!\n")

        attempt = 0
        while attempt < tries:
            try:
                guess = int(input(f"Guess a number between 1 and {limit}: "))
                attempt += 1
                msg = get_feedback(guess, number)
                print(msg)

                if guess == number:
                    break
                if attempt == tries:
                    print(f"\nGame Over ❌😞 The correct number was {number}")
            except:
                print("Please enter a valid number.")

        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != 'yes':
            print(f"\nThanks for playing, {username}! Goodbye 👋")
            break
        else:
            clear()

game()
