
import smbus # For creating bus instances 
import time

DEVICE = 0x23 # I2C device address
ONE_TIME_HIGH_RES_MODE = 0x20 
 
bus = smbus.SMBus(1)  
 
# Function to read data from device
def readLight(addr=DEVICE):
  reading = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE)
  result = ((reading[1] + (256 * reading[0])) / 1.2)
  return result
 

while True:
   value = readLight()
   print ("Light Intensity: " + str(value) + " lux")

   if(value < 20):
	   print("Too Dark")
   elif(value < 50 and value >= 20):
	   print("Dark")
   elif(value < 100 and value >= 50):
	   print("Medium")
   elif(value < 1000 and value >= 100):
	   print("Bright")
   else:
	   print("Too Bright")

   time.sleep(1.0)

