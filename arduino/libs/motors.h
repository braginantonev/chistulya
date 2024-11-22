#pragma once

#include <AFMotor.h>

namespace motors {
  void init();
  void turnMotor(AF_DCMotor*, int speed);

  //Code - 0, Params - 2(motorIDX, speed)
  void moveMotor(int params[]);

  //Code - 1, Params - 1 (speed)
  void goForward(int params[]);

  //Code - 2, Params - 0
  void stopMotors(int params[]);

  //Code - 3, Params - 0
  void stopAllMotors(int params[]);
}