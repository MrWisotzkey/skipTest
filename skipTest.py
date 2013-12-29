"""
Generate gcode to test delta printer step skips
by moving in Z direction for given time and then testing
distance to the endstops
"""
import os

#Lets create a file called skipTest.gcode on the current user desktop
userhome = os.path.expanduser('~')
desktop = userhome + '/Desktop/'
os.chdir(desktop)
f = open("skipTest.gcode","w")

#Where do we want the bottom of our Z movements to stop
zMin = input("What is the minimum Z value?: ")

#Where do we want the top of our Z movements to stop
zMax = input("What is the maximum Z value?: ")

#How fast do we want to go
mmsspeed = input("What is mm/s speed?: ")

#How long do we want the testing to run
testTime = (input("How many minutes to test?: "))*60


#Include automatic home when finished
autoHome = raw_input("Would you like to automatically home when finished (Y|N)?: ")


#Convert the mm/s speed to mm/min for the G0 F speed
fSpeed = mmsspeed*60

#calculate how far we move on each travel
d = float(zMax - zMin)

#how long should it take to cover the distance d
t1 = float(d/mmsspeed)

#how many times does the move need to happen to last the tTime
lineCount = int(round((testTime/t1)))

#Print the variables in the top of the file for debugging
f.write (";VARIABLES\n")
f.write (";d= "+ str(d)+"\n")
f.write (";testTime=" + str(testTime)+"\n")
f.write (";fSpeed="+ str(fSpeed)+"\n")
f.write (";t1="+str(t1)+"\n")
f.write (";lineCount=" +str(lineCount)+"\n")
f.write ("autoHome=" +autoHome +"\n")
f.write ("\n")

#GCode generation

#Send all of the axis home
f.write ("G28 ;Home position\n")

#Set the feed rate in mm/min
f.write ("G0 F" + str(fSpeed)+ " ;set feedrate\n")

#Loop to generate the Z moves.  Since we're writing two moves on each loop,
#we'll cut the line count in half to keep the time accurate
for x in range(0,(lineCount/2)):
    f.write ("G0 Z"+str(zMin)+"\n")
    f.write ("G0 Z"+str(zMax)+"\n")

#If we opted to add the autohome at the end, include G28
if autoHome in ['Y', 'y']:
    f.write ("G28")


#close the file properly
f.close()
