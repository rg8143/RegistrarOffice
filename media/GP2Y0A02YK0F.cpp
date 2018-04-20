/*
 *	Sharp GP2Y0A02YK0F IR Distance Sensor 20-150 cm 
 *	(Parallax Part Number: #28997) 
 *	IR Distance Sensor Library
 */

/*
 *	Sharp GP2Y0A02YK0F IR Distance Sensor 20-150 cm 
 *	(Parallax Part Number: #28997) 
 *	IR Distance Sensor Library
 *
 *  Written By:	David Such (Reefwing Software - http://www.reefwing.com.au/)
 *  Version: 	1.0
 *  Date:    	1st November 2015
 *
 *	Version History:
 *		1.0		01/11/15	Original release
 *
 *  Instructions:
 *    - Create a directory called GP2Y0A02YK0F within the libraries sub directory where your Arduino sketches are saved.
 *    - Copy GP2Y0A02YK0F.h, GP2Y0A02YK0F.cpp and keywords.txt into the GP2Y0A02YK0F directory.
 *    - Within the GP2Y0A02YK0F directory, create a sub directory called examples.
 *    - Copy DisplayCM.ino into the examples sub directory.
 *    - Restart the Arduino IDE to see the new library.
 *
 *  Read More:
 *    - Visit http://reefwingrobotics.blogspot.com.au/
 */

#ifndef GP2Y0A02YK0F_h
#define GP2Y0A02YK0F_h

#if defined(ARDUINO) && ARDUINO >= 100
  #include "Arduino.h"
#else
  #include "WProgram.h"
  #include <pins_arduino.h>
#endif

class GP2Y0A02YK0F
{
	public:
		GP2Y0A02YK0F();
		void begin();
		void begin(int sensorPin);
		int getDistanceRaw();
		int getDistanceVolt();
		int getDistanceCentimeter();

		boolean isCloser(int threshold);
		boolean isFarther(int threshold);

	private:
		int _sensorPin;
};
#endif

// Constructor

GP2Y0A02YK0F::GP2Y0A02YK0F() {

}

// Default Begin method: sensorPin = A0.

void GP2Y0A02YK0F::begin() {
	begin (A0);
}

// Begin method - assign sensorPin as the analog sensor input
// When you use begin() without variables the default input A0 is assumed.

void GP2Y0A02YK0F::begin(int sensorPin) {
  	pinMode(sensorPin, INPUT);
	_sensorPin = sensorPin;
}

// getDistanceRaw() Method: Returns the distance as a raw value: ADC output: 0 -> 1023

int GP2Y0A02YK0F::getDistanceRaw() {
		return (analogRead(_sensorPin));
}

// getDistanceCentimeter() Method: Returns the distance in centimeters

int GP2Y0A02YK0F::getDistanceCentimeter() {
	float sensorValue = analogRead(_sensorPin);
  	float cm = 10650.08 * pow(sensorValue,-0.935) - 10;
  	return roundf(cm);
}

// isCloser Method: check whether the distance to the detected object is smaller than a given threshold

boolean GP2Y0A02YK0F::isCloser(int threshold) {
	if (threshold>getDistanceCentimeter()) {
		return (true);
	} else {
		return (false);
	}
}

// isFarther Method: check whether the distance to the detected object is smaller than a given threshold

boolean GP2Y0A02YK0F::isFarther(int threshold) {
	if (threshold<getDistanceCentimeter()) {
		return true;
	} else {
		return false;
	}
}
