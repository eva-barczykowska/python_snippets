# Create an object-oriented number guessing class for numbers in the range 1 to 100,
# with a limit of 7 guesses per game. The game should play like this:
import random


class GuessingGame:
    def __init__(self):
        self.target = random.choice(list(range(1, 101)))
        self.guesses = 7

    def play(self):
        while True:
            if self.guesses == 0:
                print("You have no more guesses. You lost!")
                break
            print(f"You have {self.guesses} guesses remaining.")
            user_answer = (int(input("Enter a number between 1 and 100:")))

            if user_answer not in range(1, 101):
                user_answer = int(input("Invalid guess. Enter a number between 1 and 100: "))

            if user_answer != self.target:
                if user_answer < self.target:
                    print("Your guess is too low.")
                    self.guesses -= 1
                elif user_answer > self.target:
                    print("Your guess is too high.")
                    self.guesses -= 1
            else:
                print("That's the number!")
                print("You won!")
                break


game = GuessingGame()
game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 104
# Invalid guess. Enter a number between 1 and 100: 50
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 75
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 85
#


# You have 4 guesses remaining.
# Enter a number between 1 and 100:
# Invalid guess. Enter a number between 1 and 100: 80
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 81
# That's the number!

# You won!

# game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 50
# Your guess is too high.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 25
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 37
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 31
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 34
# Your guess is too high.

# You have 2 guesses remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have 1 guess remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have no more guesses. You lost!
# Note that a game object should start a new game with a new number to guess with each call to play.