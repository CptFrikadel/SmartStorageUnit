

class CuttingBoardState:
    """
    Class to represent the current state of the cutting board and the user

    Attributes:

    user_cutting (Bool): user is cutting something
    cutting_speed (float): speed of cutting per sec
    cutting_type (str): type of product being cut
    weight_on_board (int): weight on the cutting board in grams
    """

    def __init__(self):
        self.user_cutting = False
        self.cutting_speed = 0
        self.cutting_type = ''
        self.weight_on_board = 0

    def setUserCutting(self, val):
        pass

    def setCuttingSpeed(self, val):
        pass

    def setCuttingType(self, val):
        pass

    def setWeightOnBoard(self, val):
        pass
