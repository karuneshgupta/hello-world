n=6
def ultatriangle(n):
    for i in range(n):
        for j in range(5,i-1,-1):
            #5 and -1 are operated on each other 
            print("* ",end="")
        print("\r")
ultatriangle(n)
