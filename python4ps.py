#!/usr/bin/env python3

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
mylist_interator=iter(mylist)
for num in mylist_interator:
	if (num%2)==0:
		print(num)

#evens=[print(value) for value in mylist_interator if value%2=0]


