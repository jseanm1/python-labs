# Lab 6 Excercise 3 by Janindu

list = []

print "Enter the marks of four students, on four rows"

for x in range (0,4):
	temp = raw_input()
	temp = temp.split()
	list.append(temp)

for temp in list:
	sum = 0
	for x in temp:
		sum += int(x)
	print sum


