#include "libs/servos.h"
#include "libs/modules.h"

using namespace modules;

void Servos::init() {
  for (int i = 0; i < SERVOS_COUNT; i++)
    pservos[i]->attach(i+3); //3 4 5
}