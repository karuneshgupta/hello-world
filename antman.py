'''''x=y=z=50;
print(x);
print(y);
print(z);

a,b,c=5,10,15;
print(a);

print(b); print(c);
# MEANS COMMENT
#1.tuple
#tuple can be added
# note- tuple are always enclosed in normal brackets()
tuple=("raja",100.60,89,"deertfuvg");
kanha=("ram",87,89,"hamir");
tuple3=(tuple+kanha);
print(tuple3);

name1=kanha[0];
height1=kanha[1];
height2=kanha[2];
name2=kanha[3];
print(name1);

#2.dictionary
# dictionaries cannot be added
#data's are stored in  key value pair
#dictionary are always enclosed in curly parenthesis{}
dictionary={"name":"charlie","id":100,"department":"it"};
dictionary1={"name":"charlie chaorisya","id":101,"department":"ibm "};
dictionary2={"name":"kanha"
             ,"class":2,"department":"it",};
print(dictionary2);

#3.LISTS
list=['AMAN',678,'RAM',879];
list2=[456,'RAHUL']
print(list);
print(list[1:3]);
print(list[1:3]+list2);
print(list2*3);

#4.for loop 
#num=2
#for a in range(1,8):
 print(a*num)''''
#sum=0  
#for n in range(1,11):  
# sum+=n  
 #print(sum)  
#55


#5.KEYWORDS
#TRUE FALSE NONE AND
# ASSET DEF CLASS CONTINUE
# ELSE FINALLY ELIF DEL
# GLOBAL FOR IF FROM
# RAISE TRY OR RETURN
# NONLOCAL IN NOT IS'''''

#6 pyramid questions 

#outer loop to handle number of rows
#n in this case
def pypart(n):
  for i in range (0,n):
      for j in range (0,i+1):
        print("*",end=""):
    print("\r");
 

# driver code
n=5
pypart(n)


    

