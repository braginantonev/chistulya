#include <Servo.h>
#include <AFMotor.h>

//--- Motors ---//
AF_DCMotor leftMotor(1);
AF_DCMotor rightMotor(2);
AF_DCMotor brushMotor(3);
AF_DCMotor* pmotors[3] = {&leftMotor, &rightMotor, &brushMotor};

//--- Servos ---//
Servo leftServo;
Servo rightServo;
Servo batteryServo;
Servo* pservos[3] = {&leftServo, &rightServo, &batteryServo};

void setup() {
  //Initialize motors
  for (byte i = 0; i < 3; i++) {
    (*pmotors[i]).setSpeed(200);
    (*pmotors[i]).run(RELEASE);
  }

  //Initialize servos
  for (byte i = 0; i < 3; i++)
    (*pservos[i]).attach(i+3); //3 4 5
}

void loop() {
  // put your main code here, to run repeatedly:

}
