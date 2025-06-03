# **Activity: Create a `Student` Class**

# Your task is to:
# 1.  Define a class named `Student`.
# 2.  Implement the `__init__` method. It should take `name` and `age` as arguments and store them as attributes `self.name` and `self.age`.
# 3.  Add a method named `introduce()` that prints a message like: "Hi, my name is [Name] and I am [Age] years old."
# 4.  Create at least two different `Student` objects with different names and ages.
# 5.  Call the `introduce()` method on each of your student objects.

class Student:
    def __init__(self,name,age,gpa,phonenumber):
        
        self.name=name
        self.age=age
        self.gpa=gpa
        self.phonenumber=phonenumber
        print(f"Object of {name} has been created.. ")

    def introduce(self):
        print(f"Student Introduction of Student \nname = {self.name} \nage = {self.age} \nphonenumber = {self.phonenumber} \nGPA = {self.gpa}")      

i=int(input(("Enter the number of students: ")  ))
students=[]

for j in range(i):

    name = input(f"Enter name of student {j+1}: ")
    age = int(input(f"Enter age of student {j+1}: "))
    gpa = float(input(f"Enter gpa of student {j+1}: "))
    phonenumber = int(input(f"Enter phonenumber of student {j+1}: "))
    student= Student(name, age, gpa, phonenumber)
    students.append(student)


print("-----Student informations-----")
for i,student in enumerate(students,start=1):
    print(f"--- Student Introductions for student {i} ---")
    student.introduce()