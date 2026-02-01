import random

def play_game():
    user_wants_to_play = "yes"

    while user_wants_to_play == "yes":
        number_to_guess = random.randint(1, 20)
        attempts = 0

        print("\nI am thinking of a number between 1 and 20")

        while attempts < 5:
            user_input = int(input("Take your guess: "))
            difference = user_input - number_to_guess

            if difference == 0:
                print("That's it! You won 🎉")
                break
            elif difference == 1:
                print("High (close)")
            elif difference == -1:
                print("Low (close)")
            elif difference > 1:
                print("Very High")
            else:
                print("Very Low")

            attempts += 1
            print("Attempts left:", 5 - attempts)

        if attempts == 5:
            print("You lost 😢 The number was:", number_to_guess)

        user_wants_to_play = input("Play again? (yes/no): ").lower()

    print("Thanks for playing!")
