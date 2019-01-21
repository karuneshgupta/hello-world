for row in range (4):
    for col in range(4):
        if(row+col==3 or row+col==0 or row+col==6 or row-col==row ):
            print("*")
    print()
