#pragma once

#include <AFMotor.h>

namespace motors {
  void init();
  void runMotor(AF_DCMotor*, int speed);

  //Code - 0, Params - 2(motorIDX, speed)
  void runMotor(int params[]);

  //Code - 1, Params - 1 (speed)
  void goForward(int params[]);

  //Code - 2, Params - 2 (right motor speed, left motor speed)
  void goRound(int params[]);

  //Code - 3, Params - 0
  void stopMotors(int params[]);

  //Code - 4, Params - 0
  void stopBrush(int params[]);

  //Code - 5, Params - 0
  void stopAllMotors(int params[]);
}