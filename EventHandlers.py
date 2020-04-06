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

        #TODO this needs a delay so that the recipe tracker doesn't change steps too fast
        #TODO implement real operation detection


        update = False
        if ((int(event['volume']) == 1) and (not self.cutting_board_state.user_cutting)):
            # User started cutting
            self.cutting_board_state.setUserCutting(True)
            update = True
            
        elif((int(event['volume']) == 0) and (self.cutting_board_state.user_cutting)):
            # User has stopped cutting
            self.cutting_board_state.setUserCutting(False)
            update = True

        # Mock up user cooking events..
        elif ((int(event['volume']) == 3) and (not self.cutting_board_state.user_cooking)):
            # Pretend that 'cooking' was detected
            self.cutting_board_state.setUserCooking(True)
            update = True
        
        elif ((int(event['volume']) == 2) and (self.cutting_board_state.user_cooking)):
            # Pretend that 'cooking' was stopped
            self.cutting_board_state.setUserCooking(False)
            update = True
        
        # Singal recipe handler that the state has changed
        if (self.recipe_handler is not None) and update:
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
