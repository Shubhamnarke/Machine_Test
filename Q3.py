# Question 3  :  Write a code that accepts the 2 lists and generates the following result.


Employee = ['Amit','Manish','Mahi','Kirti','Mafin']
Salary = [20000,30000,20000,40000,25000]

l = len(Employee)
i=0
count = 0
payment = {}
for i in Employee:
	a = Employee[count]
	b = Salary[count]
	payment[a] = b
	count +=1
	
print(payment)