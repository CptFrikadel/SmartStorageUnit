from .recipe import Recipe, operations


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
        self.step_ops = {} 

        self.onStepChange()


    def printCurrStep(self):
        print("[Recipe step", self.curr_step, "]", self.recipe.steps[self.curr_step]['text'])

    def onStepChange(self):

        self.printCurrStep()
        self.step_ops = {}

        for op in operations:
            # Check if operation is required and add to step_ops
            if self.recipe.steps[self.curr_step][op]:
                self.step_ops[op] = False

        print(self.step_ops)

        # Notify oocsi that the step has changed
        self.stor_state.oocsi.send('recipeChannel', {'step' : self.curr_step})


    def nextStep(self):
        # TODO: implement recipe end..
        self.curr_step += 1
        self.onStepChange()


    def prevStep(self):
        self.curr_step -= 1


    def updateState(self):
        """
        Callback to be called whenever the system state has changed. Checks whether or not the step has to be advanced or not

        """

        if ('cutting' in  self.step_ops) and (self.cut_state.user_cutting):
            self.step_ops['cutting'] = True
            
        if ('cooking' in self.step_ops) and (self.cut_state.user_cooking):
            self.step_ops['cooking'] = True


        advance = True

        # Check if ALL operations are complete
        for op in self.step_ops:
            if self.step_ops[op] == False:
                advance = False
                print('User still needs to do:',op)
                break

        if advance:
            self.nextStep()


