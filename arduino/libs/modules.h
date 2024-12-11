#pragma once

#include <Servo.h>
#include <AFMotor.h>

namespace modules {
  static const int MOTORS_COUNT = 3;
  static const int SERVOS_COUNT = 3;

  //--- Motors ---//
  static AF_DCMotor leftMotor(1);
  static AF_DCMotor rightMotor(2);
  static AF_DCMotor brushMotor(3);
  static AF_DCMotor* const pmotors[MOTORS_COUNT] = {&leftMotor, &rightMotor, &brushMotor};

  //--- Servos ---//
  static Servo leftServo;
  static Servo rightServo;
  static Servo* const pservos[SERVOS_COUNT] = {&leftServo, &rightServo};
}