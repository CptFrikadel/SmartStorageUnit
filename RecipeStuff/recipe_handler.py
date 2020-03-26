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

        print("[Recipe step", self.curr_step, "]", self.recipe.steps[0]['text'])

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
        
        print("Updating recipe state!")

        # Check whether or not the current step needs to be advanced







