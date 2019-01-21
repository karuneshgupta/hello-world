def pyramid(n):
        k=0
        for i in range(0,n):
                for j in range(0,k):
                        print(end=" ")
                for j in range(0,5-i):
                        print("*",end=" ")
                k=k+1
                print()
n=5;
pyramid(n)
