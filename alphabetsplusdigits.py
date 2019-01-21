def rightangleandalphabets(n):
    num=65
    k=2*n-2;
    for i in range (0,n):
        for j in range(0,k):
            ch=chr(num)
            print(ch,end="");
            num=num+1
        
        for j in range(0,i+1):
            print("* ",end="")
        k=k-2;
        print();
            
n=5;
rightangleandalphabets(n)
