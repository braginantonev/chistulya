#include "libs/serialCommands.h"
#include "libs/modules.h"

using namespace modules;
using namespace scomm;

void (*pcommands[])(int[]) = {
  motors::moveMotor,
  motors::goForward,
  motors::stopMotors,
  motors::stopAllMotors
};

void setup() {
  Serial.begin(9600);

  motors::init();
  servos::init();
}

void loop() {
}
