import random

def guessing_game():
    print("Welcome to Guess the Number game!")
    random_number = random.randint(1,100)

    while True:
        user_guess = int(input("Guess a number (between 1 and 100): "))

        if user_guess < random_number:
            print("Try guessing higher.")
        elif user_guess > random_number:
            print("Try guessing lower.")
        else:
            print(f"Congrats! You guessed the correct number, {random_number}.")
            break

if __name__ == "__main__":
    guessing_game()