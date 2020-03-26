import RecipeStuff

class EventHandler:
    """
    Wrapper class for the event handlers. 

    Attributes:

    global_state (StorageUnitState): reference to the global state
    cutting_board_state (CuttingBoardState): reference to the board state
    recipe_handler (recipeHandler): reference to the recipe handler
    
    """

    def __init__(self, _global_state, _cutting_board_state, _recipe_handler):
        self.global_state = _global_state
        self.cutting_board_state = _cutting_board_state
        self.recipe_handler = _recipe_handler

    def onCuttingVolume(self, sender, event):

        if ((int(event['volume']) > 0) and (not self.cutting_board_state.user_cutting)):
            
            # set user cutting in board state
            self.cutting_board_state.setUserCutting(True)
            if self.recipe_handler is not None:
                self.recipe_handler.updateState()
            
        elif((int(event['volume']) <= 0) and (self.cutting_board_state.user_cutting)):
            # User has stopped cutting
            # Set user_cutting back to false if this applies
            self.cutting_board_state.setUserCutting(False)
            if self.recipe_handler is not None:
                self.recipe_handler.updateState()
            
   #send all messages for each event
    def onSoundSpectrum(self, sender, event):
        print('Sound Spectrum event!')

    def onBoardWeight(self, sender, event):
        self.cutting_board_state.setWeightOnBoard(int(event['weight']))
        print('Board Weight event!')

    def onCuttingSpeed(self, sender, event):
        self.cutting_board_state.setCuttingSpeed(float(event['speed']))
        print('Cutting Speed event!')

    def startRecipe(self, filename):
        
        if self.recipe_handler is not None:
            pass
        else:
            self.recipe_handler = RecipeStuff.RecipeHandler(filename, self.cutting_board_state, self.global_state)
