'''try:
    a=int(input("enter value"))
    b=int(input("enter value"))
    d=a/b
    c=a+b
    print(d)
except ArithmeticError:
    print("divisin by zero cant be possible");
except NameError:
    print("variable c is not defined ")
finally:
    print("raja");
    print(c)'''
try:  
     a=10
     b=10
     c=a/b
     print(c)  
     raise ArithmeticError("hello")  
except ArithmeticError as e:  
     print("An exception occurred")  
     print(e)  

