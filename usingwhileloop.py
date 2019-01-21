'''a=int(input("enter the value of a"))
while a>0:
    print("value of a is ",a)
    a=a-2
print("loop is complete")

# SUM of the cosecutive digits for ex 123 is 6
num=153
sum=0
while num>0:
    rem=num%10
    sum=sum+int(rem)
    num=num/10
print (sum)
#using break condition in python
for i in range(0,7):
    if i==4:
        print("element found")
        break
    print (i)'''
#using continue condition in python
'''a=0
while a<=5:
    a=a+1
    if a==2:
        print("raja")
        continue # continue reverses the pointer to a=a+1 statement 
    else:
        if a==6:
            print("rani");
            continue
    print(a)'''

#python strings
#1.strings are immutable- strings can change but their adddress cannot
#reverse chararray
'''name="karunesh"
length=len(name)
i=0
for n in range(-1,(0-9),-1):
    print(name[i],"\t",name[n]);
    i=i+1'''
a = [1,2,3,4,5]
reverse_a = a[::-1]
print(reverse_a)
