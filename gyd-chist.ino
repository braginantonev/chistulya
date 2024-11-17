#include <Servo.h>
#include <AFMotor.h>

#define MOTORS_COUNT 3
#define SERVOS_COUNT 3

////--- Variables ---////
//--- Motors ---//
AF_DCMotor leftMotor(1);
AF_DCMotor rightMotor(2);
AF_DCMotor brushMotor(3);
AF_DCMotor* pmotors[MOTORS_COUNT] = {&leftMotor, &rightMotor, &brushMotor};

//--- Servos ---//
Servo leftServo;
Servo rightServo;
Servo batteryServo;
Servo* pservos[SERVOS_COUNT] = {&leftServo, &rightServo, &batteryServo};

////--- Raspberry functions ---////
//-- -Motors ---//
void moveMotor(AF_DCMotor motor, int speed) {
  motor.setSpeed(abs(speed));
  if (speed > 0)
    motor.run(FORWARD);
  else
    motor.run(BACKWARD);
}

//Code - 0, Params - 1 (speed)
void goForward(int params[]) {
  moveMotor(rightMotor, params[0]);
  moveMotor(leftMotor, params[0])
}

//Code - 1, Params - 0
void stopMotors(int params[]) {
  rightMotor.run(RELEASE);
  leftMotor.run(RELEASE);
}

//Code - 2, Params - 0
void stopAllMotors(int params[]) {
  for (int i = 0; i < MOTORS_COUNT; i++) {
    (*pmotors[i]).run(RELEASE)
  }
}

void (*pcommands[]) (int[]) {
  goForward
}



void setup() {
  //Initialize motors
  for (int i = 0; i < MOTORS_COUNT; i++) {
    (*pmotors[i]).setSpeed(200);
    (*pmotors[i]).run(RELEASE);
  }

  //Initialize servos
  for (int i = 0; i < SERVOS_COUNT; i++)
    (*pservos[i]).attach(i+3); //3 4 5
}

void loop() {

}
