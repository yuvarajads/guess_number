import random


class NumberGuessingGame:

    def __init__(self):
        ## define the range
        self.LOWER = 1
        self.HIGHER = 100

    ## method to generate the random number
    def get_random_number(self):
        return random.randint(self.LOWER, self.HIGHER)

    ## game start method
    def start(self):
        ## generating the random number
        random_number = self.get_random_number()

        print(
            f"Guess the randomly generated number from {self.LOWER} to {self.HIGHER}")

        ## heart of the game
        chances = 0
        while True:
            user_number = int(input("Enter the guessed number: "))
            if user_number == random_number:
                print(
                    f"-> Hurray! You got it in {chances + 1} step{'s' if chances > 1 else ''}!")
                break
            else:
                print("-> Your guess is wrong ",random_number)
            chances += 1

## instantiating and starting the game
numberGuessingGame = NumberGuessingGame()
numberGuessingGame.start()
