from gpiozero import RGBLED
from time import sleep

class RGBLEDController:
    def __init__(self, config):
        self.led = RGBLED(config['red'], config['green'], config['blue'])
        print("RGB LED initialized.")

    def success(self):
        """
        Sets LED to green to indicate success.
        """
        self.led.color = (0, 1, 0)  # Green
        print("LED: Success (Green)")

    def error(self):
        """
        Sets LED to red to indicate an error.
        """
        self.led.color = (1, 0, 0)  # Red
        print("LED: Error (Red)")

    def neutral(self):
        """
        Sets LED to blue or neutral state.
        """
        self.led.color = (0, 0, 1)  # Blue
        print("LED: Neutral (Blue)")

    def blink(self, color=(1, 0, 0), times=3):
        """
        Blinks the LED with the specified color.
        """
        for _ in range(times):
            self.led.color = color
            sleep(0.5)
            self.led.off()
            sleep(0.5)
        print(f"LED: Blinked {times} times.")
