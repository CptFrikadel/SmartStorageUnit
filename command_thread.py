import threading
import time

class CommandThread(threading.Thread):
    '''
    Command thread class. Waits for user input, parses the command and executes

    Attributes:
    storage_state (StorageUnitState): reference to the storage state object

    Command general structure:

    <command> <arg1> <arg2> <arg...

    '''

    def __init__(self, _storage_state):
        threading.Thread.__init__(self)
        self.storage_state = _storage_state
        self.start()

    def run(self):
        
        while True:
            cmd = input("> ")
            self.execute(cmd)

    def execute(self, cmd):

        # Split the command into a list of command and arguments
        split_cmd = list(cmd.split())

        # Parse
        if split_cmd[0] == 'add_item':
            self.addItem(split_cmd[1:])
            
        elif split_cmd[0] == 'remove_item':
            self.removeItem(split_cmd[1:])

        elif split_cmd[0] == 'scan_code':
            self.scanCode(split_cmd[1:])
        
        elif split_cmd[0] == 'add_scan':
            self.scanCode(split_cmd[1])
            self.addItem(split_cmd[2:])

        elif split_cmd[0] == 'remove_scan':
            self.scanCode(split_cmd[1])
            self.removeItem(split_cmd[2:])
            
        elif split_cmd[0] == 'exit':
            self.shutDown()


    def addItem(self, args):
        print(args)
        self.storage_state.setPressure(True)
        self.storage_state.addItem(args[0], int(args[1]))


    def removeItem(self, args):
        print(args)
        self.storage_state.setPressure(False)
        self.storage_state.removeItem(args[0], int(args[1]))

    def shutDown(self):
        
        self.storage_state.oocsi.stop()
        exit()

    def scanCode(self, arg):

        if arg == 'def1':
            code = 5032227310339
        elif arg == 'def2':
            code = 8710434011016
        else:
            code = arg

        self.storage_state.oocsi.send('barCodeChannel', {'scanned_barcode':code})



