# Lab 6 Excercise 2 by Janindu

min = 0
max = 0

list = raw_input("Enter 10 numbers: ")
list = list.split()

min = list[0]
max = list[0]

for x in range (1,10):
	if (min > list[x]):
		min = list[x]
	if (max < list[x]):
		max = list[x]

print "Maximum = ", max
print "Minimum = ", min
