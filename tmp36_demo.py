from mcp3008 import *
import time

mcp = MCP3008()
TMP36_CHANNEL = 0

while True:
   analog_value = mcp.analog_read(TMP3008_CHANNEL)
   voltage = 3.3 * analog_value / 1024
   temperature_c = (voltage * 1000 - 500) / 10
   temperature_f = 9.0 / 5.0 * temperature_c + 32.0
   print("Temperature: %.1fC (%.1fF)" % (temperature_c , temperature_f)
   time.sleep(1)
