#!/usr/bin/env python3
import sys

count=int(sys.argv[1])
if count > 0:
	print('positive')
	if count <50:
		print('less than 50')
		if (count%2)==0:
			print('it is an even number that is smaller than 50')
	if count >50:
		print('more than 50')
		if (count%3)==0:
			print('it is larger than 50 and divisible by 3')
	else:
		print('number is 50')
elif count < 0:
	print('negative')
else:
	print('zero')
