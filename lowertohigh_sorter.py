print "Enter number of elements you want to sort lower to higher: "


ary = []
cup = 0

while 1:

	n = input()

	if (n > 0):

		print "Enter elements :"

		for x in range(n):

			ary.append( input() )


		break

for x in range(n-1):

	x=0


	for xx in range(n-1):


		if ary[x] > ary[x+1]:

			cup = ary[x+1]

			ary[x+1] = ary[x]

			ary[x] = cup

		x= x+1






print(ary)
