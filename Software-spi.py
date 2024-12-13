import time
import board
import digitalio
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import adafruit_bitbangio as bitbangio

# Define the software SPI pins
SCLK = board.D11  # GPIO 11
MOSI = board.D10  # GPIO 10
MISO = board.D9   # GPIO 9
CS = digitalio.DigitalInOut(board.D22)  # GPIO 22

# Create the SPI bus
spi = bitbangio.SPI(SCLK, MOSI, MISO)

# Create the MCP3008 object
mcp = MCP.MCP3008(spi, CS)

# Create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

try:
    while True:
        voltage = chan.voltage
        print("Reading=%d\tVoltage=%f" % (chan.value, voltage))
        time.sleep(1)
except KeyboardInterrupt:
    pass
