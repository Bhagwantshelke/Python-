# class TripToNepal:
#     budget=5000
#     Mode = "car"
#
#     def eat_someting_new(self,cost):
#         self.budget = self.budget-cost
#
#     def change_mode(self,new_mode):
#         self.Mode = new_mode
#
#     def look_at_current_situation(self):
#         print("Hello your remaining Budget is : " ,self.budget)
#
#
# trip = TripToNepal()
# trip.eat_someting_new(500)
# trip.change_mode('bus')
# trip.look_at_current_situation()



# class Cal():
#     def add(self,a,b):
#         print(f"Addition is :  ",a+b)
#     def sub(self,a,b):
#         print(f"Substraction is :  ",a-b)
#     def mul(self,a,b):
#         print(f"Multiplication is :  ",a*b)
#     def div(self,a,b):
#         print(f"Division is :  ",a/b)
# calculate = Cal()
# calculate.add(3,5)
# calculate.sub(10,3)
# calculate.mul(4,6)
# calculate.div(20,5)


# class Student:
#     def __init__(self, name, branch):
#         self.name = name
#         self.branch  = branch
#
#     def get_name(self):
#         print(self.name)
#     def get_branch(self):
#         print(self.branch)
# s = Student("Bhagwant","Big data")
# s.get_name()
# s.get_branch()



# class Student:
#     def __init__(self,name,USN,branch):
#         self.name = name
#         self.USN = USN
#         self.branch = branch
#
#     def update_branch(self,new_branch):
#         self.branch = new_branch
#     def display(self):
#         print("Student Name: ", self.name)
#         print("Student USN: ", self.USN)
#         print("Student Branch: ", self.branch)
#
# student_db = [Student("Bhagwant Shelke","001","Copm"),
#            Student("Akash","003","Bigdata"),
#            Student("Omkar","002","ML")]
# search = input("Enter Searching name: ")
# filtered_data = [x for x in student_db if search in x.name]
# if len(filtered_data)>=1:
#     filtered_data[0].display()
# else:
#     print("No Data")



# from math import pi
#
# class Shape:
#     def __init__(self,*args):
#         print("len of argumnte is : ", len(args))
#         self.args = args
#         if len(args) == 1:
#             print("Area of circle is : ",pi*args[0]*args[0])
#             print("circumference of circle is : ",2*pi*args[0])
#         else:
#             print("Area : ", args[0]*args[1] )
#             print("Perimeter : ", 2*(args[0]+args[1]) )
#
# # s1 = Shape(10)
# s1 = Shape(10,20)




