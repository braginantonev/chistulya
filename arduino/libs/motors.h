#pragma once

#include <AFMotor.h>

namespace motors {
  void init();
  void runMotor(AF_DCMotor*, int speed);

  //Code - 0, Params - 2(motorIDX, speed)
  void runMotor(int params[]);

  //Code - 1, Params - 1 (speed)
  void goForward(int params[]);

  //Code - 2, Params - 1 (speed)

  //Code - /, Params - 0
  void stopMotors(int params[]);

  //Code - /, Params - 0
  void stopAllMotors(int params[]);
}