#include <Wire.h>
int green = 11;
int yellow = 12;
int red = 13;

byte state = 0;	// 0 - Green, 1 - Yellow, 2 - Red
byte counter = 0;

void setup()
{
  pinMode(red,OUTPUT); 
  pinMode(yellow,OUTPUT); 
  pinMode(green,OUTPUT); 
  Wire.begin(4);                // join i2c bus with address #4
  Wire.onReceive(receiveEvent); // register event
  Serial.begin(9600);           // start serial for output
}

void loop()
{
  if (state == 0){
    digitalWrite(green, HIGH);
    digitalWrite(yellow, LOW);
    digitalWrite(red, LOW);
  }
  else if (state == 1){
    digitalWrite(green, LOW);
    digitalWrite(yellow, HIGH);
    digitalWrite(red, LOW);
  }
  else if (state == 2){
    digitalWrite(green, LOW);
    digitalWrite(yellow, LOW);
    digitalWrite(red, HIGH);
  }
  delay(100);
}

void receiveEvent(int howMany)
{
  int x = Wire.read();    	// receive byte as an integer
  counter = counter + x;
  if (counter < 3) {
    state = state + 1;
  }
  counter = counter % 6;
  if (counter == 0){
    state = 0;
  }
  Serial.println(x);         // print the integer
}
