# Import necessary modules
import time
from modules.fingerprint import FingerprintSensor
from modules.lcd_display import LCD
from modules.led_control import RGBLED
from modules.timesheet import Timesheet
from modules.error_handling import ErrorHandler
from config import CONFIG

# Initialize components
def initialize_system():
    print("Initializing system...")
    try:
        fingerprint_sensor = FingerprintSensor(CONFIG['fingerprint'])
        lcd = LCD(CONFIG['lcd'])
        led = RGBLED(CONFIG['led'])
        timesheet = Timesheet(CONFIG['database'])
        error_handler = ErrorHandler(lcd, led)
        print("System initialized successfully.")
        return fingerprint_sensor, lcd, led, timesheet, error_handler
    except Exception as e:
        print(f"Error during initialization: {e}")
        exit(1)

# Main event loop
def main():
    # Initialize system components
    fingerprint_sensor, lcd, led, timesheet, error_handler = initialize_system()

    # Start main loop
    try:
        while True:
            print("Waiting for fingerprint...")
            lcd.display_message("Place your finger")
            
            # Scan fingerprint
            user_id = fingerprint_sensor.scan()
            
            if user_id:
                print(f"Fingerprint recognized: User ID {user_id}")
                lcd.display_message(f"Welcome, User {user_id}")
                led.success()

                # Log clock-in/clock-out
                timesheet.log_event(user_id)
                time.sleep(2)  # Pause before the next scan
            else:
                print("Fingerprint not recognized")
                lcd.display_message("Try again!")
                led.error()
                time.sleep(2)
    except KeyboardInterrupt:
        print("\nShutting down system...")
        lcd.display_message("System shutting down")
        time.sleep(1)
        lcd.clear()

# Run the program
if __name__ == "__main__":
    main()
