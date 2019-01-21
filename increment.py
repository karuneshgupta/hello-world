''''for i in range(5,0,-2):
    print(i)
a=int(input("enter a number"))
if (a%2!=0):
        print("the no. is odd")
else:
    print("no. is even")
n=int(input("enter the year"))
if (n%4==0):
    print("year is leap")'''
c = int(input("enter marks"))
if (100>c>90):
    print("a1")
elif(c<0):
    print("not possible")
elif(80<c<90):
        print("a2")
elif(70<c<80):
        print("b1")
elif(60<c<70):
        print("b2")
elif(50<c<60):
        print("c1")
elif(40<c<50):
        print("c2")
elif(c<40):
        print("passed on edge")
elif(c>100):
        print("enter the right value")
else:
        print("fail")
        
