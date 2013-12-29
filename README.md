skipTest
========

A simple python script that will generate gcode to test stepper motor skipped steps on a delta configuration.

The script generated will code that moves the print head between a z minimum value and a z maximum value for an extended period of time.  After the full execution of the gcode, initiate a home command to see if all three caraiges hit the end stops at the same time.  Any carraige that touches behind the others has lost steps during the course of the test.  Increasing the speed on each test will give you an idea of the maximum supported speeds for your printer.

minimum Z value /zMin = This is the lowest value you want your hotend to travel and should be reasonably above the build plate

maximum Z value / zMax = This is the highest value you want the hotend to travel

mm/s speed / mmsSpeed = Enter the speed for the moves in mm/s.  We'll use this to calculate how long it takes to make one move from zMax to zMin and also convert it to mm/min to set the G0 feed rate

How many minutes to test / testTime = Longer test may yield better chances of finding missed steps

autoHome = On shorter tests, when you're watching the printer, we can add G28 to the end of the script.  For longer test times, when you may walk away from the printer, you can manually home the carraiges to see if they all hit at the same time.

