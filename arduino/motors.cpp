#include "libs/motors.h"
#include "libs/modules.h"

using namespace modules;

void motors::turnMotor(AF_DCMotor* motor, int speed) {
  if (speed > 0) {
    motor->setSpeed(speed);
    motor->run(FORWARD);
  }
  else {
    motor->setSpeed(-speed);
    motor->run(BACKWARD);
  }
}

//Code - 0, Params - 2(motorIDX, speed)
void motors::moveMotor(int params[]) {
  AF_DCMotor* motor = pmotors[params[0]];
  int speed = params[1];

  turnMotor(motor, speed);
}

//Code - 1, Params - 1 (speed)
void motors::goForward(int params[]) {
  turnMotor(&rightMotor, params[0]);
  turnMotor(&leftMotor, params[0]);
}

//Code - 2, Params - 0
void motors::stopMotors(int params[]) {
  rightMotor.run(RELEASE);
  leftMotor.run(RELEASE);
}

//Code - 3, Params - 0
void motors::stopAllMotors(int params[]) {
  for (int i = 0; i < MOTORS_COUNT; i++) {
    pmotors[i]->run(RELEASE);
  }
}

void motors::init() {
  for (int i = 0; i < MOTORS_COUNT; i++) {
    pmotors[i]->setSpeed(200);
    pmotors[i]->run(RELEASE);
  }
}