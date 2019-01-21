n=10
def contalpha(n):
#ascii value
    num=65
    for i in range(0,n):
        #num=65
        for j in range(0,i+1):
            #converting number to char from ascii code
            ch=chr(num);
            print(ch,end=" ")
            num=num+1;
        print("\r")
contalpha(n)

