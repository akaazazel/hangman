from time import sleep

import wordEngine as we
import hangman as hm
import score


class Main:
    def __init__(self):
        self.score = score.Score()

    def main(self):
        while True:
            command = input("Press enter to continue!")
            if command == "":
                hangMan = hm.HangMan()
                engine = we.WordEngine(hangMan)

            elif command in ["/quit", "/q"]:
                self.exitTheGame()
                return

            else:
                print("Try again")
                continue

            while True:
                hangMan.drawHangMan()
                engine.displayGuessedLetters()
                engine.displayWord()
                guess = (input("Enter your guess: ")).lower()

                if guess == "" or guess.isdigit():
                    print("Try again!\n")
                    continue

                if guess in ["/quit", "/q"]:
                    self.exitTheGame()
                    return
                elif guess in ["/restart", "/r"]:
                    break
                elif guess in ["/hint", "/h"]:
                    engine.displayHint()
                    continue

                if (engine.checkIfGuessIsRight(guess) == 2) or (
                    self.checkIfGuessedAllLetters(engine)
                ):
                    print("You guessed the word!\n")
                    self.score.updateScore(True)
                    break
                elif engine.checkIfGuessIsRight(guess) == 1:
                    print("Correct!\n")
                    continue
                else:
                    hangMan.updateHangMan()
                    print("Wrong!\n")
                self.delay()

                if hangMan.checkIfManHanged():
                    hangMan.drawHangMan()
                    print("You lost!\n")
                    self.delay()
                    print(f"The word was {(engine.activeWord).upper()}")
                    self.score.updateScore(False)
                    self.delay()
                    break

            self.score.displayScore()

    def checkIfGuessedAllLetters(self, engine):
        for letter in engine.activeWord:
            if letter not in engine.guessedLetters:
                return False
        return True

    def delay(self, duration=0.5):
        sleep(duration)

    def exitTheGame(self):
        print("Bye!")


main = Main()
main.main()
