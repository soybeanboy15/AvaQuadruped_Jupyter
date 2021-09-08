from evdev import InputDevice, categorize, ecodes
import evdev
from numpy import interp

class BluetoothController:
    def __init__(self):
        self.bluetooth_controller = evdev.InputDevice('/dev/input/event2')
        print(self.bluetooth_controller)
        self.button_A = 305
        self.button_B = 304
        self.button_X = 307
        self.button_Y = 306
        self.button_home = 316
        self.button_plus = 313
        self.button_minus = 312
        self.button_L = 308
        self.button_ZL = 310
        self.button_R = 309
        self.button_ZR = 311

        self.button = '0'
        self.LX = 0
        self.LY = 0
        self.RX = 0
        self.RY = 0

    def read_controller(self):
        self.button = '0'
        event = self.bluetooth_controller.read_one()
        if event != None:
            if event.type == evdev.ecodes.EV_KEY:
                if event.value == 1:
                    if event.code == self.button_A:
                        self.button = 'A'
                    elif event.code == self.button_B:
                        self.button = 'B'
                    elif event.code == self.button_X:
                        self.button = 'X'
                    elif event.code == self.button_Y:
                        self.button = 'Y'
                    elif event.code == self.button_home:
                        self.button = 'H'
                    elif event.code == self.button_plus:
                        self.button = '+'
                    elif event.code == self.button_minus:
                        self.button = '-'
                    elif event.code == self.button_L:
                        self.button = 'L'
                    elif event.code == self.button_ZL:
                        self.button = 'ZL'
                    elif event.code == self.button_R:
                        self.button = 'R'
                    elif event.code == self.button_ZR:
                        self.button = 'ZR'
            elif event.type == evdev.ecodes.EV_ABS:
                if event.code == 0:
                    mapped_LX = interp(event.value, [7900, 56000], [-100, 100])
                    if mapped_LX > -5 and mapped_LX < 5:
                        self.LX = 0
                    else:
                        self.LX = mapped_LX
                if event.code == 1:
                    mapped_LY = interp(event.value, [9500, 60000], [100,-100])
                    if mapped_LY > -5 and mapped_LY < 5:
                        self.LY = 0
                    else:
                        self.LY = mapped_LY
                if event.code == 3:
                    mapped_RX = interp(event.value, [8500, 56000], [-100, 100])
                    if mapped_RX > -10 and mapped_RX < 10:
                        self.RX = 0
                    else:
                        self.RX = mapped_RX                    
                if event.code == 4:
                    mapped_RY = interp(event.value, [9800, 59000], [100,-100])
                    if mapped_RY > -5 and mapped_RY < 5:
                        self.RY = 0
                    else:
                        self.RY = mapped_RY

        return [self.button, self.LX, self.LY, self.RX, self.RY]
