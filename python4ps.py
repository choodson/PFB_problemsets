#!/usr/bin/env python3
import sys



#2
#human='sapiens,erectus,neanderthalensis'
#print(human)
#splithuman=human.split(',')
#print(splithuman)
#sorthuman=sorted(splithuman)
#print(sorthuman)
#sorted(splithuman,key=len)


#4
#count=0
#while count <101:
#	print('count is', count)
#	count+=1
#print('Done')



#5
#result=1
#counter=1
#while counter <= 1000:
#	result=counter*result
#	counter+=1
#print(result)


#6
mylist=[101,2,15,22,95,33,2,27,72,15,52]
#mylist_interator=iter(mylist)
#for num in mylist_interator:
#	if (num%2)==0:
#		print(num)

#evens=[print(value) for value in mylist_interator if value%2=0]

#7
#sortlist=sorted(mylist)
#print(sortlist)
#sortlist_i=iter(sortlist)
#resulteven=0
#resultodd=0
#for values in sortlist_i:
#	if (values%2)==0:
#		resulteven=resulteven+values
#	else:
#		resultodd=resultodd+values
#print('Sum of odd numbers:',resultodd)
#print('Sum of even numbers:',resulteven)


#8
#for num in (range(101)):
#	print(num)


#9
#values=[print(value) for value in (range(101))]


#10

value1=sys.argv[1]
value2=sys.argv[2]
value=value1
while value <=value2:
	print(value)
	value+=1
