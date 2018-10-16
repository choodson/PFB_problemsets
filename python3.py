#!/usr/bin/env python3
import sys
variable=sys.argv[1]
if variable:
	message="is true"
	print(variable,message)
else:
	message='is not true'
	print(variable,message)
