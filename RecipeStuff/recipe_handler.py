from .recipe import Recipe

class RecipeHandler:
    """
    Handler class for keeping track of an active recipe

    Attributes:

    recipe (Recipe): The currently active recipe
    curr_step (int): The current step of the recipe the user is on
    cut_state (CuttingBoardState): state structure of the cuttingboard
    stor_state (StorageUnitState): state structure of the storage unit
    """

    def __init__(self, _recipe, _cut_state, _stor_state):
        self.recipe = Recipe(_recipe)
        self.cut_state = _cut_state
        self.stor_state = _stor_state
        self.curr_step = 0

        self.printCurrStep()

    def printCurrStep(self):
        print("[Recipe step", self.curr_step, "]", self.recipe.steps[self.curr_step]['text'])

    def startNewRecipe(self, _recipe):
        """
        Starts a new recipe 
        """
        self.recipe = Recipe(_recipe)
        self.curr_step = 0

    def updateState(self):
        """
        Callback to be called whenever the system state has changed. Checks whether or not the step has to be advanced or not

        Arguments:
        cutting (Bool): Whether or not the user is cutting something
        """

        # Check whether or not the current step needs to be advanced
        if self.cut_state.user_cutting == self.recipe.steps[self.curr_step + 1]['cutting']:
            print("Next step!!")
            self.curr_step += 1
            self.printCurrStep()







