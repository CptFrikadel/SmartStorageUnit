import RPi.GPIO as GPIO
import time
import threading


class PressureSensorThread:
    """
    Class that starts a thread to continully poll a pressure sensor

    Attributes:
    input_pin (int): Pin number of to which the pressure sensor is connected
    thread (Thread): Thread object for the polling thread

    state (int): Wheter or not sensor is under pressure use getState() to obtain
    new (bool): set whenever new value is read. 

    global_state (StorageUnitState): copy of the global state
    """

    def __init__(self, pin, _global_state):
        self.input_pin = pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN)
        
        self.thread = threading.Thread(target=self.pollSensor)
        self.thread.start()

        self.global_state = _global_state


    def pollSensor(self):

        prev_state = 0

        while True:
            state = GPIO.input(self.input_pin)

            if ((not prev_state) and state):
                self.global_state.setPressure(True)
            elif ((not state) and prev_state):
                self.global_state.setPressure(False)

            prev_state = state

            time.sleep(0.10)

    def getState(self):

        self.new = False
        return self.state


