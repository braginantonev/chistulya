#include "libs/serialCommands.h"
#include "libs/modules.h"

using namespace modules;
using namespace scomm;

void (*pcommands[])(int[]) = {
  motors::runMotor,           //1
  motors::goForward,          //2
  motors::goRound,            //3
  motors::stopMotors,         //4
  motors::stopBrush,          //5
  motors::stopAllMotors,      //6
  nullptr,                    //7 - reserved
  nullptr,                    //8 - reserved
  nullptr,                    //9 - reserved
  servos::rotateServo         //10
};

void setup() {
  Serial.begin(9600);

  motors::init();
  servos::init();
}

void loop() {
}
