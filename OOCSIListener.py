
from oocsi import OOCSI

class Listener:
    """
    Wrapper class for the OOCSI network
        
    Attributes: 
        channels (dict): A dictionary of channel names and function pointers to their event handlers.
    """

    def __init__(self, oocsi_instance, channels):
        """
        Class constructor
        
        Parameter:
        channels (dict): Dict of { channel name (str) : event handler (func)}
        """
        self.channels = channels

        for channel in self.channels:
            oocsi_instance.subscribe(channel, self.globalEventHandler)


    def globalEventHandler(self, sender, recipient, event):

        #print('[Listener]', recipient, ':', sender, '->', event)

        # Call respective channel event handler
        self.channels[recipient](sender, event)


