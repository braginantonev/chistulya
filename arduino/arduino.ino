#include "libs/serialCommands.h"
#include "libs/modules.h"

using namespace modules;

void (*pcommands[]) (int[]) {

};

void setup() {
  Serial.begin(9600);

  scomm::motors.init();

  //Initialize servos
  for (int i = 0; i < SERVOS_COUNT; i++)
    pservos[i]->attach(i+3); //3 4 5
}

void loop() {
}
