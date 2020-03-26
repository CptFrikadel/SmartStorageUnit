#! /usr/bin/python3

from oocsi import OOCSI
from OOCSIListener import Listener
from EventHandlers import *
#from PressureSensor.pressure_sensor import PressureSensorThread 
from storage_state import StorageUnitState
from cuttingboard_state import CuttingBoardState
import time
import RecipeStuff



# Obtain oocsi instance and connect to remote server
oocsi = OOCSI('SmartStorageUnit', 'oocsi.id.tue.nl')

# Initialize the global state 
global_state = StorageUnitState(oocsi)

# Initialize the cuttingboard state
cutting_board_state = CuttingBoardState()

evt = EventHandler(global_state, cutting_board_state, None)

# Dictionary of which channels to receive on and their event handlers
receiver_channels = {
        'cuttingVolumeChannel': evt.onCuttingVolume,
        'soundSpectrumChannel' : evt.onSoundSpectrum, 
        'boardWeightChannel' : evt.onBoardWeight, 
        'cuttingSpeedChannel' : evt.onCuttingSpeed
        }

# Start the OOCSI listener
listener = Listener(oocsi, receiver_channels)

# Start the pressure sensor thread with sensor on GPIO 21
#psensor = PressureSensorThread(21, global_state)
psensor = 0 # use for testing without RPi

# Init a recipe for testing
evt.startRecipe('example_recipe.json')
