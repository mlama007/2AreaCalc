"""This program is to calculate the area of different shapes:  circles and triangles"""

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print "Calculator is booting up"

print "Current time: %s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)

sleep(1)

hint = "Don't forget to include the correct units! \nExiting..."

option = raw_input("Enter C for Circle or T for Triangle: ")

option = option.upper()



#Area of Circle
if option == "C":
  radius = float(raw_input("Enter the radius of the cirle: "))
  area = pi * radius**2
  print "The pie is baking..."
  sleep(1)
  print "Area: %.2f  \n%s" % (area, hint)
  
#Area of Triangle
elif option == "T":
  base = float(raw_input("Enter base of triangle: "))
  height = float(raw_input("Enter height: "))
  area = .5 * base * height
  print "Uni Bi Tri..."
  sleep (1)
  print "Area: %.2f \n%s" % (area, hint)
  
#If user enters something other than T/C
else:
  print "Error! We only calculate areas of circles and triangles! \nExiting now..."
  
  
  
  
  
  
  
  