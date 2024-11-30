class ErrorHandler:
    def __init__(self, lcd, led):
        self.lcd = lcd
        self.led = led

    def handle_error(self, error_code, message):
        """
        Handles an error by logging and displaying it.
        """
        print(f"Error {error_code}: {message}")
        self.lcd.display_message(f"Error {error_code}")
        self.led.error()
