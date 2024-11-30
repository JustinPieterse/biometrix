import serial
from time import sleep

class FingerprintSensor:
    def __init__(self, config):
        self.serial = serial.Serial(
            port='/dev/serial0',  # Default UART on Raspberry Pi
            baudrate=57600,
            timeout=1
        )
        print("Fingerprint sensor initialized.")

    def scan(self):
        """
        Simulates scanning a fingerprint.
        Returns a user ID if recognized, or None if not recognized.
        """
        print("Scanning fingerprint...")
        # Send a command to the fingerprint sensor (replace with actual sensor logic)
        self.serial.write(b'\x01')  # Example command
        sleep(1)
        response = self.serial.read(8)  # Example response length
        print(f"Sensor response: {response}")
        if response:
            return 1  # Simulate returning a user ID
        else:
            return None

    def enroll(self):
        """
        Enrolls a new fingerprint (placeholder).
        """
        print("Enrolling a new fingerprint...")
        # Add logic to enroll a fingerprint
        pass
