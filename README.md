skipTest
========

A simple python script that will generate gcode to test stepper motor skipped steps on a delta configuration.

The script generated will code that moves the print head between a z minimum value and a z maximum value for an extended period of time.  After the full execution of the gcode, initiate a home command to see if all three caraiges hit the end stops at the same time.  Any carraige that touches behind the others has lost steps during the course of the test.  Increasing the speed on each test will give you an idea of the maximum supported speeds for your printer.
