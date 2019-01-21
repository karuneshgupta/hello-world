#count fn
schoolname ="universal academy"
letter ="a";
print(schoolname.count(letter))
#startswith and endswith
string1="Welcome SSSIT to";
substring1="Welcome";
substring2="to";
substring3="of";
print(string1.startswith("Welcome"));
print(string1.endswith(substring2,2,16));
print(string1.endswith(substring3,2,19));
print(string1.endswith(substring3));
#find output will denote the first index only
str="Welcome to SSSIT";  
substr1="come";  
substr2="to";  
print(str.find("come"));
#to check whether the string is alpha numeric
str="Welcome to sssit";  
print (str.isalnum());  
str1="Python47";  
print (str1.isalnum());
# to check whether the string is digit
string1="HelloPython";   
print (string1.isdigit());  
string2="98564738"  
print (string2.isdigit());  
