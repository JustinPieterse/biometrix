import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
from PIL import Image, ImageDraw, ImageFont

class LCD:
    def __init__(self, config):
        self.dc = config['dc']
        self.rst = config['rst']
        self.ce = config['ce']

        # Initialize LCD
        self.lcd = LCD.PCD8544(self.dc, self.rst, self.ce, spi=SPI.SpiDev(0, 0))
        self.lcd.begin(contrast=60)
        self.clear()
        print("LCD initialized.")

    def display_message(self, message):
        """
        Displays a message on the LCD.
        """
        self.clear()
        image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()

        draw.text((0, 0), message, font=font, fill=255)
        self.lcd.image(image)
        self.lcd.display()
        print(f"LCD Message: {message}")

    def clear(self):
        """
        Clears the LCD screen.
        """
        self.lcd.clear()
        self.lcd.display()
