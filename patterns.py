#squares
for row in range (1,5):
    for column in range (1,5):
        print("*",end=" ")
    print()
#triangle pyramid
for row in range (1,5):
    for column in range(1,row+1):
        print("*",end=" ")
    print()
# reverse triangle pyramid
for row in range(1,5):
    for column in range(row,5):
        print("*",end=" ")
    print()
#hollow square
for row in range(1,5):
    for column in range(1,5):
        if(row==1 or row==4 or column==1 or column==4 ):
                 print("*",end=" ")
        else:
            print(" ",end=" ")

    print()
#plus
for row in range(1,6):
    for column in range(1,6):
        if(row==3 or column==3 ):
                 print("*",end=" ")
        else:
            print(" ",end=" ")

    print()
#right angle triangle
for row in range(1,4):
    for column in range(1,4):
        if(row==3 or column==1 ):
                 print("*",end=" ")
        else:
            print(" ",end=" ")

    print()
# reverse right angle triangle
for row in range(1,4):
    for column in range(1,4):
        if(row==1 or column==1 ):
                 print("*",end=" ")
        else:
            print(" ",end=" ")

    print()
# cross
for row in range(1,6):
    for column in range(1,6):
        if( row==column or row+column==6):
                 print("*",end=" ")
        else:
            print(" ",end=" ")

    print()
# reverse pyramid
k=1
for row in range(1,7):
    for column in range(1,k):
        print(end=" ")
    for column in range(1,7-row):
            print("*",end=" ")
    k=k+1;
    print()
pyramid

    


  
    

