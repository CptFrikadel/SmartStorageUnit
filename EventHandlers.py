
class EventHandler:
    """
    Wrapper class for the event handlers. 

    Attributes:
    user_cutting (bool): Wether or not the user is cutting

    
    """

    def __init__(self, _global_state):
        self.global_state = _global_state
        #set default on user_cutting on false
        self.user_cutting = False

    def onCuttingVolume(self, sender, event):
        #check if there is feedback from the cuttingboard
        if ((int(event['volume']) > 0) and (not self.user_cutting)):
            
            #set a value for OOCSI
            print('User is cutting something!')
            self.user_cutting = True
            
        #after checking if user_cutting is set to true, check of volume is back to 0
        elif((int(event['volume']) <= 0) and (self.user_cutting)):
            
           #Set user_cutting back to false if this applies
            print('User stopped cutting something!')
            self.user_cutting = False
            
   #send all messages for each event
    def onSoundSpectrum(self, sender, event):
        print('Sound Spectrum event!')

    def onBoardWeight(self, sender, event):
        print('Board Weight event!')

    def onCuttingSpeed(self, sender, event):
        print('Cutting Speed event!')
