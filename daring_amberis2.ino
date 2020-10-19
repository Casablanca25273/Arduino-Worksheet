#include <Wire.h>

void setup()
{
  Wire.begin(); // join i2c bus (address optional for master)
}

byte x = 1;

void loop()
{
  Wire.beginTransmission(4); 	// transmit to device #4
  Wire.write(x);              	// sends one byte  
  Wire.endTransmission();    	// stop transmitting
  delay(5000);
  Wire.beginTransmission(4); 	// transmit to device #4
  Wire.write(x);              	// sends one byte  
  Wire.endTransmission();    	// stop transmitting
  delay(2000);
  Wire.beginTransmission(4); 	// transmit to device #4
  Wire.write(x);              	// sends one byte  
  Wire.endTransmission();    	// stop transmitting
  delay(1000);
}
