import random


class WordEngine:
    FILE_PATH = "wordList.txt"

    def __init__(self, hangMan):
        self.wordList = self.loadWords(self.FILE_PATH)  # list of words to choose from

        self.guessedLetters = (
            []
        )  # list of all guessed letters which are present in the word

        self.allGuessedLetters = []  # list of all guessed letters

        self.activeWord = (
            self.chooseWord()
        )  # the new word which is currently in the game

        self.hangMan = hangMan  # new hangman

    def loadWords(self, filepath):
        try:
            with open(filepath, "r") as file:
                wordList = [line.strip().lower() for line in file.readlines()]
                return wordList
        except FileNotFoundError:
            print("Word file not found. Using default word list.")
            wordList = ["elephant", "rabbit", "dinosaur"]
            return wordList

    def chooseWord(self):
        """Return a random word chosen from a list of words."""
        word = random.choice(self.wordList)
        return word

    def checkIfGuessIsRight(self, guess):
        """Checks if user guess is true or false.
        If user guesses the whole word, return 2.
        If user guessed a single character, returns 1.
        Or it will return 0."""

        # If guess is a single character and it is not present in list of all guessed letter, adds it to the list of all guessed letters.
        if (len(guess) == 1) and (guess not in self.allGuessedLetters):
            self.allGuessedLetters.append(guess)
            self.allGuessedLetters.sort()

        # if guess is the whole word, returns 2
        if guess == self.activeWord:
            return 2

        # if guess is a single letter and it is present in the word, returns 1
        if (len(guess) == 1) and guess in self.activeWord:
            # if guessed letter is not in guessed letters (present in the word), adds it to the guessed letters (present in the word).
            if guess not in self.guessedLetters:
                self.guessedLetters.append(guess)
            return 1

        # else return 0
        return 0

    def displayWord(self):
        """Displays the current word with underscore for letters which are not guessed."""
        for i in self.activeWord:
            if i in self.guessedLetters:
                print(i.upper(), end="")
            else:
                print("_", end="")
        print(f" ({len(self.activeWord)} letters)")

    def displayGuessedLetters(self):
        """Displays all guessed letters during a single game"""
        if len(self.allGuessedLetters) == 0:
            return
        print("Guessed: [", end=" ")
        for letter in self.allGuessedLetters:
            print(letter.upper(), end=" ")
        print("]")

    def displayHint(self):
        """Displays the first letter of the word"""
        print(f"First letter is {self.activeWord[0]}")
