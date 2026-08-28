import random
# Number guessing game "Time Pass"
def guess_the_number():
    # Pick a random number between 1 and 20
    secret_number = random.randint(1, 20)
    attempts = 0
    
    print("✨ Welcome to the Guessing Game! ✨")
    print("I am thinking of a number between 1 and 20.")

    # Loop until the player guesses correctly
    while True:
        try:
            # Get input from the user and convert it to an integer
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You found it in {attempts} attempts!")
                break # Exit the loop
                
        except ValueError:
            print("Please enter a valid number.")

# Run the app
if __name__ == "__main__":
    guess_the_number()

