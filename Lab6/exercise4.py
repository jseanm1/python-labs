# Lab 6 Exercise 4 by Janindu

subject = ["I", "We"]
verb	= ["play", "watch"]

object = raw_input("Enter two sports you love: ")
object = object.split()

for sub in subject:
	for ver in verb:
		for obj in object:
			print sub,ver,obj + ".",
