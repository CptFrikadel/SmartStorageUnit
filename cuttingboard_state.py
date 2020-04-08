

class CuttingBoardState:
    """
    Class to represent the current state of the cutting board and the user

    Attributes:

    user_cutting (Bool): user is cutting something
    user_cookig (Bool): user is cooking something
    kitchen_timer (Bool): Ringing of the kitchen timer

    cutting_speed (float): speed of cutting per sec
    cutting_type (str): type of product being cut
    weight_on_board (int): weight on the cutting board in grams
    """

    def __init__(self):
        self.user_cutting = False
        self.user_cooking = False
        self.kitchen_timer = False
        self.cutting_speed = 0
        self.cutting_type = ''
        self.weight_on_board = 0

    def setUserCutting(self, val):
        self.user_cutting = val

        if val == True:
            print('User is cutting something!')
        elif val == False:
            print('User stopped cutting something!')

    def setUserCooking(self, val):
        self.user_cooking = val

        if val == True:
            print('User is cooking something!')
        elif val == False:
            print('User stopped cooking something!')

    def setKitchenTimer(self, val):
        self.kitchen_timer = val

    def setCuttingSpeed(self, val):
        self.cutting_speed = val

        if val > 0:
            self.user_cutting = True
        elif val == 0:
            self.user_cutting = False

    def setCuttingType(self, val):
        self.cutting_type = val

    def setWeightOnBoard(self, val):
        self.weight_on_board = val
