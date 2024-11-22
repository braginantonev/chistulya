#pragma once

#include <Servo.h>

namespace servos {
  void init();

  //Code - 10, Params - 2 (servoIDX, angle)
  void rotateServo(int params[]);
}