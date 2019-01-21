#simple pyramid

'''num=4;
for i in range(0,num):
        #this loop for printing spaces
        for j in range(0,num-i-1):
            print(end=" ");
        #this loop for printing stars
        for j in range(0,i+1):
            print("*",end=" ");
        print();'''    
'''def pyramid(n):
        k=2*n-6
        for i in range(0,n):
                for j in range(0,k):
                        print(end=" ")
                for j in range(0,i+1):
                        print("*",end=" ")
                k=k-1
                print()
n=5
pyramid(n)'''
def pyramid2(n):
        k=1
        for i in range(0,n):
                for j in range(0,k):
                        print(end=" ")
                for j in range(0,4-i):
                        print("*",end=" ")
                k=k+1
                print()
n=4
pyramid2(n)
