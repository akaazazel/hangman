from time import sleep

import wordEngine as we
import hangman as hm
import score


class Main:
    def __init__(self):
        self.score = score.Score()

    def main(self):
        print("--HANGMAN--")
        print("use -help for help and commands.\n")
        # Main loop continues until user exits the program
        while True:
            command = input("Press enter to continue!")
            # if user presses enter, create a new hangman and create a new word
            if command == "":
                hangMan = hm.HangMan()  # create a new hangman
                engine = we.WordEngine(hangMan)  # create a new word

            elif command in ["-quit", "-q"]:
                self.exitTheGame()
                return

            elif command == "-help":
                self.openHelp()
                continue

            else:
                print("Try again")
                continue

            # Game loop asks for user guess
            self.gameLoop(hangMan, engine)

            self.score.displayScore()  # display the score

    def gameLoop(self, hangMan, engine):
        """Main game loop.
        Chooses a random word and asks the user for guess.
        Evaluates the answers"""
        while True:
            hangMan.drawHangMan()  # draw hangman
            engine.displayGuessedLetters()  # display letters that are guessed
            engine.displayWord()  # display the current word
            guess = (input("Enter your guess: ")).lower()

            # if guess is empty or a digit, continue the loop
            if guess == "" or guess.isdigit():
                print("Try again!\n")
                continue

            if guess in ["-quit", "-q"]:
                self.exitTheGame()
                return
            elif guess in ["-restart", "-r"]:
                break
            elif guess in ["-newgame", "-ng"]:
                self.startNewGame()
                break
            elif guess in ["-hint", "-h"]:
                engine.displayHint()
                continue

            # if user guess is the complete word, or if user guessed all letters, display user won
            if (engine.checkIfGuessIsRight(guess) == 2) or (
                self.checkIfGuessedAllLetters(engine)
            ):
                print("You guessed the word!\n")
                self.score.updateScore(True)
                break
            # if the user guess is a character, and it's right, display correct
            elif engine.checkIfGuessIsRight(guess) == 1:
                print("Correct!\n")
                continue
            # else the user is wrong
            else:
                hangMan.updateHangMan()
                print("Wrong!\n")
            self.delay()  # a slight delay for wrong answers

            # check if hangman is hanged (no tries left), and if no tries left, print the user is lost
            if hangMan.checkIfManHanged():
                hangMan.drawHangMan()
                print("You lost!\n")
                self.delay()
                print(f"The word was {(engine.activeWord).upper()}")
                self.score.updateScore(False)
                self.delay()
                break

    def checkIfGuessedAllLetters(self, engine):
        """Returns True if the user guessed all letters in the word. Or it will return False."""
        for letter in engine.activeWord:
            if letter not in engine.guessedLetters:
                return False
        return True

    def openHelp(self):
        commands = {
            "-quit, -q": "quit the game",
            "-restart, -r": "restart the game with current score",
            "-newgame, -ng": "start a new game with no score",
            "-hint, -h": "displays the first letter of the word",
        }

        for command, desc in commands.items():
            print(f"{command}\t: {desc}")
        print("")

    def startNewGame(self):
        """Resets the score"""
        self.score = score.Score()

    def delay(self, duration=0.5):
        sleep(duration)

    def exitTheGame(self):
        print("Bye!")


main = Main()
main.main()
