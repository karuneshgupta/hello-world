class student:
    def __init__(self,rollno,name):
     self.rollno=rollno
     self.name=name
    def displaystudent(self):
        print("rollno:",self.rollno,"name:",self.name)
emp1=student(121,"RAJ")
emp2=student(122,"ram")
            
emp1.displaystudent()
emp2.displaystudent()
