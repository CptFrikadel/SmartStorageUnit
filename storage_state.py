
class StorageUnitState:
    """
    Class to represent the global state of the storage unit

    Only use the add and set methods to modify the state! Else the OOCSI does not get updated correctly

    Attributes:

    oocsi (OOCSI): the oocsi network handle
    items (dict): Items currently stored in the unit with amounts
    pressure (int): value of the pressure sensor

    """
    
    def __init__(self, _oocsi):
        self.oocsi = _oocsi
        self.items = {}
        self.pressure = 0

    def updateOOCSI(self):
        self.oocsi.send('itemListChannel', self.items)
        self.oocsi.send('storagePressureChannel', {'pressure_val':self.pressure})

    def setPressure(self, val):
        self.pressure = val
        self.updateOOCSI()

    def addItem(self, name, amount):
        
        # If item is already in inventory, add amount to inventory
        if name in self.items:
            self.items[name] += amount
        else:
            self.items[name] = amount

        self.updateOOCSI()

    def removeItem(self, name, amount):
        
        if name not in self.items:
            return

        # Check whether some or all of the item is removed
        if amount >= self.items[name]:
            del self.items[name] 
        else:
            self.items[name] -= amount

        self.updateOOCSI()
    
