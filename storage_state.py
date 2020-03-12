from recipe import Recipe

class StorageUnitState:
    """
    Class to represent the global state of the storage unit

    Attributes:

    oocsi (OOCSI): the oocsi network handle
    items (dict): Items currently stored in the unit with amounts
    curr_recipe (Recipe): The active recipe
    pressure (int): value of the pressure sensor

    """
    
    def __init__(self, _oocsi):
        self.oocsi = _oocsi
        self.items = {}
        self.curr_recipe = Recipe('example_recipe.json')
        self.pressure = 0

    def updateOOCSI(self):
        self.oocsi.send('itemListChannel', self.items)
        self.oocsi.send('storagePressureChannel', self.pressure)


    def addItem(self):
        self.items = {'something' : 1}
        self.updateOOCSI()

    def removeItem(self):
        self.items = {}
        self.updateOOCSI()
        
