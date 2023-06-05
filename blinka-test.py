import board
import digitalio
import busio

print("Hello blinka!")

# Try to great a Digital input
try:
    pin = digitalio.DigitalInOut(board.D4)
except:
    print("Digital IO not available on this board!")
else:
    print("Digital IO ok!")

# Try to create an I2C device
try:
    i2c = busio.I2C(board.SCL, board.SDA)
except:
    print("I2C not available on this board!")
else:
    print("I2C ok!")

# Try to create an SPI device
try:
    spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
except:
    print("SPI not available on this board!")
else:
    print("SPI ok!")

print("done!")
