#!/usr/bin/env python3
import sys
name="Christina"
print(name)

print('My favourite colour: Blue')

activity="hiking"
print('My favourite activity:',activity)

animal="butterflies"
print('My favourite animal:',animal)


#using sys to input variables from command line
name1=sys.argv[1]
colour1=sys.argv[2]
activity1=sys.argv[3]
animal1=sys.argv[4]
print('My name: '+ name1,'\n',
'My favourite colour:', colour1,'\n',
'My favourite activity:', activity1,'\n',
'My favourite animal:',animal1)

