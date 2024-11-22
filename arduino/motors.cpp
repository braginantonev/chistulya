#include "libs/motors.h"
#include "libs/modules.h"

using namespace modules;

void Motors::moveMotor(AF_DCMotor* motor, int speed) {
  if (speed > 0) {
    motor->setSpeed(speed);
    motor->run(FORWARD);
  }
  else {
    motor->setSpeed(-speed);
    motor->run(BACKWARD);
  }
}

//Code - 00, Params - 2(motorIDX, speed)
void Motors::moveMotor(int params[]) {
  AF_DCMotor* motor = pmotors[params[0]];
  int speed = params[1];

  moveMotor(motor, speed);
}

//Code - 01, Params - 1 (speed)
void Motors::goForward(int params[]) {
  moveMotor(&rightMotor, params[0]);
  moveMotor(&leftMotor, params[0]);
}

//Code - 1, Params - 0
void Motors::stopMotors(int params[]) {
  rightMotor.run(RELEASE);
  leftMotor.run(RELEASE);
}

//Code - 2, Params - 0
void Motors::stopAllMotors(int params[]) {
  for (int i = 0; i < MOTORS_COUNT; i++) {
    pmotors[i]->run(RELEASE);
  }
}

void Motors::init() {
  for (int i = 0; i < MOTORS_COUNT; i++) {
    pmotors[i]->setSpeed(200);
    pmotors[i]->run(RELEASE);
  }
}