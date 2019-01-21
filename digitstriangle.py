#number triangle
#output will be
'''1
2 3
4 5 6
7 8 9 10'''
def digitstriangle(n):
    num=1
    for i in range (0,n):
            for j in range(0,i+1):
                print(num,end=" ")
                num=num+1;
            print("\r")
n=5
digitstriangle(n)
#2.number starting from same digit
#output will be
'''1
1 2
1 2 3
1 2 3 4'''
def digitstriangle2(n):
    num=1
    for i in range (0,n):
        num=1
        for j in range(0,i+1):
                print(num,end=" ")
             
        print("\r")
n=5
digitstriangle2(n)
