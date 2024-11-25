class Score:
    def __init__(self):
        self.win = 0
        self.lost = 0

    def updateScore(self, boolean):
        """For true argument, increments the Win.
        For False argument, increments the Lost."""
        if boolean is True:
            self.win += 1
        elif boolean is False:
            self.lost += 1

    def displayScore(self):
        print(f"Win: {self.win} Lost: {self.lost}")
