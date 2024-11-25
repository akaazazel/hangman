class HangMan:
    def __init__(self):
        self.MAX_TRIES = 6
        self.currentTries = 0

    def updateHangMan(self):
        """Updates the user tries"""
        self.currentTries += 1

    def drawHangMan(self):
        """Draws hangman depending on the tries left"""
        currentTries = self.currentTries

        if currentTries == 0:
            print(
                "   ______\n   |    |\n        |\n        |\n        |\n _______|\n|_HANG__|        \n"
            )
        elif currentTries == 1:
            print(
                "   ______\n   |    |\n   o    |\n        |\n        |\n _______|\n|_HANG__|        \n"
            )
        elif currentTries == 2:
            print(
                "   ______\n   |    |\n   o    |\n   |    |\n        |\n _______|\n|_HANG__|        \n"
            )
        elif currentTries == 3:
            print(
                "   ______\n   |    |\n   o    |\n  /|    |\n        |\n _______|\n|_HANG__|        \n"
            )
        elif currentTries == 4:
            print(
                "   ______\n   |    |\n   o    |\n  /|\\   |\n        |\n _______|\n|_HANG__|        \n"
            )
        elif currentTries == 5:
            print(
                "   ______\n   |    |\n   o    |\n  /|\\   |\n  /     |\n _______|\n|_HANG__|        \n"
            )
        elif currentTries == 6:
            print(
                "   ______\n   |    |\n   o    |\n  /|\\   |\n  / \\   |\n _______|\n|_HANG__|        \n"
            )

        # print(f"Try Left: {self.MAX_TRIES - currentTries}\n")

    def checkIfManHanged(self):
        """Returns True if there is no tries left, or it will return False."""
        if self.currentTries == self.MAX_TRIES:
            return True
        return False
