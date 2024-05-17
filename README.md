# Connecting TJCTM24028-SPI to Raspberry PI:

TFT Display connection accorting to : https://learn.adafruit.com/adafruit-1-14-240x135-color-tft-breakout/python-wiring-and-setup
TOUCH connection according to: https://github.com/humeman/xpt2046-circuitpython/tree/main?tab=readme-ov-file

| Raspberry Pi       | TJCTM24028-SPI   | Function          |
|--------------------|------------------|-------------------|
| 1 (3.3v)           | VCC              | VCC               |
| 6 (GND)            | GND              | GND               |
| 24 (GPIO8, CE0)    | CS               | TFT CS            |
| 18 (GPIO24)        | RESET            | TFT Reset         |
| 22 (GPIO25)        | D/C              | TFT D/C           |
| 19 (GPIO10, MOSI)  | SDI(MOSI) & T_DIN| TFT MOSI          |
| 23 (CPIO11, SCLK)  | SCK & T_CLK      | TFT SCLK          |
| 1 (3.3v)           | LED              | TFT LED BACKLIGHT |
| 37 (GPIO26)        | T_IRQ            | TOUCH IRQ         |
| 31 (GPIO6)         | T_CS             |                   |
| 21 (GPIO9)         | T_DO             |                   |

