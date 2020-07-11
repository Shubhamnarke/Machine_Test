
# Question No 5 : Write a snippet that resolves ancient Chinese puzzle:

# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

class combinations:

	def __init__(self,heads,legs,c,r):
		self.heads = heads
		self.legs = legs
		self.c = c
		self.r = r
		print('Number of possible conditions are : \n')

	def match(self):
		for i in range(self.heads):
			for j in range(i):
				if ((c*i) + (r*j)==self.legs):
					if (i+j==self.heads):
						print("chickens : ",i,",","rabbits : ",j)



heads = 35
legs = 94
c = 2
r = 4
j = 0

comb = combinations(heads,legs,c,r)
comb.match()