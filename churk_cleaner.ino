#include <Servo.h>
#include <AFMotor.h>

//--- Motors ---//
AF_DCMotor leftMotor(1);
AF_DCMotor rightMotor(2);
AF_DCMotor brushMotor(3);
AF_DCMotor* pmotors[3] = {&leftMotor, &rightMotor, &brushMotor};

void setup() {
  //Initialize motors
  for (byte i = 0; i < 3; i++) {
    (*pmotors[i]).setSpeed(200);
    (*pmotors[i]).run(RELEASE);
  }
}

void loop() {
  // put your main code here, to run repeatedly:

}
