import threading
import time

welcome_string = '''
    Welcome to the Smart Storage Unit!
    Type 'help' for a list of available commands.

'''

help_string = '''

    Available commands are:

    help                                    print this help

    exit                                    stops oocsi and exits

    add_item [name] [amount]                add 'amount' items of type 'name' 
                                            to the storage unit

    remove_item [name] [amount]             remove 'amount' of item with 'name' 
                                            from the storage unit

    scan_code [EAN code]                    emulate a scan of 'EAN code' 
                                            (use code 'def1' for cookies :)

    add_scan [EAN code] [item] [amount]     Scan and add an item to the storage 
                                            unit

    remove_scan [EAN code] [item] [amount]  Scan and remove an item from the
                                            storage unit

'''

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

        print(welcome_string)
        
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

        elif split_cmd[0] == 'help':
            print(help_string)


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

        print("Ok thanks bye!")
        exit()

    def scanCode(self, arg):

        if arg == 'def2':
            code = 5032227310339
        elif arg == 'def1':
            code = 8710434011016
        else:
            code = arg

        self.storage_state.oocsi.send('barCodeChannel', {'scanned_barcode':code})



