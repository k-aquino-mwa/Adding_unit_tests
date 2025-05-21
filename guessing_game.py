import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
    
        if guess < number_to guess:
            print("Too low! Try Again.")
        elif guess > number_to guess:
            print("Too high! Try Again.")
        else 
            print("Congratulations! You guessed the number in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid integer.")

if __name__ ==  "__main__":
    guessing_game()
