
#  Question No. 4 :  Write a code that generates the following pattern based on True or False conditions.


a = input('Enter Condition : ').lower()
print("\n")


if a == 'false':
    for row in range(5):
        print()
        for column in range(9):
            if row==0 and column in (0,1,2,3,4,5,6,7,8):
                print('*',end=' ')
            elif row==1 and column in (1,2,3,4,5,6,7):
                print('*',end=' ')
            elif row==2 and column in (2,3,4,5,6):
                print('*',end=' ')
            elif row==3 and column in (3,4,5):
                print('*',end=' ')
            elif row==4 and column == 4:
                print('*',end=' ')
            else:
                print(end = '  ')
        print()


elif a == 'true':                #Opposite of false...
    for row in range(5):
        print()
        for column in range(9):
            if row==0 and column == 4:
                print('*',end=' ')
            elif row==1 and column in (3,4,5):
                print('*',end=' ')
            elif row==2 and column in (2,3,4,5,6):
                print('*',end=' ')
            elif row==3 and column in (1,2,3,4,5,6,7):
                print('*',end=' ')
            elif row==4 and column in (0,1,2,3,4,5,6,7,8):
                print('*',end=' ')
            else:
                print(end = '  ')
        print()

else:
    print('Please Enter True or False....')

