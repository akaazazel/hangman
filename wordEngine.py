import random


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

        if (len(guess) == 1) and guess in self.activeWord:
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
