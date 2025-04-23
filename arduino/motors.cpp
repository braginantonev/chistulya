#include "libs/motors.h"
#include "libs/modules.h"

using namespace modules;

void motors::init() {
  for (int i = 0; i < MOTORS_COUNT; i++) {
    pmotors[i]->setSpeed(200);
    pmotors[i]->run(RELEASE);
  }
}

void motors::runMotor(AF_DCMotor* motor, int speed) {
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
void motors::runMotor(int params[]) {
  runMotor(pmotors[params[0]], params[1]);
}

//Code - 1, Params - 1 (speed)
void motors::goForward(int params[]) {
  runMotor(&rightMotor, params[0]);
  runMotor(&leftMotor, params[0]);
}

//Code - 2, Params - 2 (right motor speed, left motor speed)
void motors::goRound(int params[]) {
  runMotor(&rightMotor, params[0]);
  runMotor(&leftMotor, params[1]);
}

//Code - 3, Params - 0
void motors::stopMotors(int params[]) {
  rightMotor.run(RELEASE);
  leftMotor.run(RELEASE);
}

//Code - 4, Params - 0
void motors::stopBrush(int params[]) {
  brushMotor.run(RELEASE);
}

//Code - 5, Params - 0
void motors::stopAllMotors(int params[]) {
  for (int i = 0; i < MOTORS_COUNT; i++) {
    pmotors[i]->run(RELEASE);
  }
}

// Code - 6, Params - 1
void motors::backward(int params[]) {
  runMotor(&rightMotor, -params[0]);
  runMotor(&leftMotor, -params[0]);
}