#pragma once

#include <AFMotor.h>

class Motors {
public:
  void init();

  //Code - 00, Params - 2(motorIDX, speed)
  void moveMotor(int params[]);

  //Code - 01, Params - 1 (speed)
  void goForward(int params[]);

  //Code - 02, Params - 0
  void stopMotors(int params[]);

  //Code - 03, Params - 0
  void stopAllMotors(int params[]);

private:
  void moveMotor(AF_DCMotor*, int speed);
};