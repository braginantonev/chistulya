#include "libs/serialCommands.h"
#include "libs/modules.h"

using namespace modules;
using namespace scomm;

void (*pcommands[])(int[]) = {
  motors::runMotor,           //0
  motors::goForward,          //1
  motors::goRound,            //2
  motors::stopMotors,         //3
  motors::stopBrush,          //4
  motors::stopAllMotors,      //5
  nullptr,                    //6 - reserved
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
  delay(50);
}
