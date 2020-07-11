
# Question No 1 : Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.


import random     #for genarating random values

outer = []   

def result(x,y):
    if x == 0:
        print(outer)
    else:
        inner = []
        for num in range(y):
            a = random.randint(1,15)
            inner.append(a)
     
        outer.append(inner)
      
        return (result(x-1,b))


a = int(input('Enter the value of x : '))
b = int(input('Enter the value of y : '))

result(a,b)

