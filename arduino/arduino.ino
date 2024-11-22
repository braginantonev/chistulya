#include "libs/serialCommands.h"
#include "libs/modules.h"

using namespace modules;

void (*pcommands[]) (int[]) {

};

void setup() {
  Serial.begin(9600);

  scomm::motors.init();
  scomm::servos.init();
}

void loop() {
}
