#include "libs/servos.h"
#include "libs/modules.h"

using namespace modules;

void servos::init() {
  for (int i = 0; i < SERVOS_COUNT; i++)
    pservos[i]->attach(10-i); //3 4 5
}

//Code - 10, Params - 2 (servoIDX, angle)
void servos::rotateServo(int params[]) {
  pservos[params[0]]->write(params[1]);
}