class HangMan:
    def __init__(self):
        self.MAX_TRIES = 6
        self.currentTries = 0

    def updateHangMan(self):
        self.currentTries += 1

    def drawHangMan(self):
        currentScore = self.currentTries

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

        # print(f"Try Left: {self.MAX_TRIES - currentScore}\n")

    def checkIfManHanged(self):
        if self.currentTries == self.MAX_TRIES:
            return True
        return False
