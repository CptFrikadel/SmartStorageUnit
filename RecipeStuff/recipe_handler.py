
class RecipeHandler:
    """
    Handler class for keeping track of an active recipe

    Attributes:

    recipe (Recipe): The currently active recipe
    curr_step (int): The current step of the recipe the user is on
    """

    def __init__(self, recipe):
        self.recipe = _recipe
        self.curr_step = 0

    def startNewRecipe(self, _recipe):
        """
        Starts a new recipe 
        """
        self.recipe = _recipe
        self.curr_step = 0

    def updateState(self):
        """
        Callback to be called whenever the system state has changed. Checks whether or not the step has to be advanced or not

        Arguments:
        cutting (Bool): Whether or not the user is cutting something
        """

        # Check whether or not the current step needs to be advanced
        print("Updating recipe state!")





