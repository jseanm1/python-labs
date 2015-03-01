# Lab 6 Excercise 1 by Janindu

sum = 0

list = raw_input("Enter 10 integers: ")
list = list.split()

for x in range (0,10):
	sum += int(list[x])

print "Total = ", sum
print "Average = ", sum*1.0/len(list)	
