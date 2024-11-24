import random
from time import sleep


class Score:
    def __init__(self):
        self.win = 0
        self.lost = 0

    def updateScore(self, boolean):
        if boolean is True:
            self.win += 1
        elif boolean is False:
            self.lost += 1

    def displayScore(self):
        print(f"Win: {self.win} Lost: {self.lost}")


class HangMan:
    def __init__(self):
        self.hangManLimit = 6
        self.hangManScore = 0

    def updateHangMan(self):
        self.hangManScore += 1

    def drawHangMan(self):
        currentScore = self.hangManScore

        if currentScore == 0:
            print(
                "   ______\n   |    |\n        |\n        |\n        |\n _______|\n|_HANG__|        \n"
            )
        elif currentScore == 1:
            print(
                "   ______\n   |    |\n   o    |\n        |\n        |\n _______|\n|_HANG__|        \n"
            )
        elif currentScore == 2:
            print(
                "   ______\n   |    |\n   o    |\n   |    |\n        |\n _______|\n|_HANG__|        \n"
            )
        elif currentScore == 3:
            print(
                "   ______\n   |    |\n   o    |\n  /|    |\n        |\n _______|\n|_HANG__|        \n"
            )
        elif currentScore == 4:
            print(
                "   ______\n   |    |\n   o    |\n  /|\\   |\n        |\n _______|\n|_HANG__|        \n"
            )
        elif currentScore == 5:
            print(
                "   ______\n   |    |\n   o    |\n  /|\\   |\n  /     |\n _______|\n|_HANG__|        \n"
            )
        elif currentScore == 6:
            print(
                "   ______\n   |    |\n   o    |\n  /|\\   |\n  / \\   |\n _______|\n|_HANG__|        \n"
            )

        # print(f"Try Left: {self.hangManLimit - currentScore}\n")

    def checkIfManHanged(self):
        if self.hangManScore == self.hangManLimit:
            return True
        return False


class WordEngine:
    def __init__(self, hangMan):
        self.wordList = ["elephant", "rabbit", "dinosaurs"]
        self.guessedLetters = []
        self.allGuessedLetters = []
        self.activeWord = self.chooseWord()
        self.hangMan = hangMan

    def chooseWord(self):
        word = random.choice(self.wordList)
        return word

    def checkIfGuessIsRight(self, guess):
        if (len(guess) == 1) and (guess not in self.allGuessedLetters):
            self.allGuessedLetters.append(guess)
            self.allGuessedLetters.sort()

        if guess == self.activeWord:
            return 2

        if guess in self.activeWord:
            if guess not in self.guessedLetters:
                self.guessedLetters.append(guess)
            return 1

        return 0

    def displayWord(self):
        for i in self.activeWord:
            if i in self.guessedLetters:
                print(i.upper(), end="")
            else:
                print("_", end="")
        print(f" ({len(self.activeWord)})")

    def displayGuessedLetters(self):

        if len(self.allGuessedLetters) == 0:
            return
        print("Guessed: [", end=" ")
        for letter in self.allGuessedLetters:
            print(letter.upper(), end=" ")
        print("]")


class Main:
    def __init__(self):
        self.score = Score()

    def main(self):
        while True:
            command = input("Press enter to continue!")
            if command == "":
                hangMan = HangMan()
                engine = WordEngine(hangMan)

            elif command in ["/quit", "/q"]:
                self.exitTheGame()

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
        exit()


main = Main()
main.main()
