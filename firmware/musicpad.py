import board
import digitalio


from kmk.kmk.kmk_keyboard import KMKKeyboard
from kmk.kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

#pin scanner
class DirectPinScanner:
    """
    returns 2D list
      True = key NOT pressed
      False = key pressed
    """
    def __init__(self, pins):
        self.pins = []
        for p in pins:
            d = digitalio.DigitalInOut(p)
            d.direction = digitalio.Direction.INPUT
            d.pull = digitalio.Pull.UP
            self.pins.append(d)

    def scan(self):
        return [[pin.value for pin in self.pins]]


KEY_PINS = [
    board.D7,
    board.D8,
    board.D9,
    board.D1,
    board.D0,
]


keyboard = KMKKeyboard()
keyboard.matrix = DirectPinScanner(KEY_PINS)


encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    (board.D2, board.D3, None), 
)


encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),), 
]


keyboard.keymap = [
    [KC.F8, KC.F9, KC.F10, KC.F11, KC.F12]
]

if __name__ == '__main__':
    keyboard.go()
