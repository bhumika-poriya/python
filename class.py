# class student:
#     def stu(self):
#         self.name=input()
#         self.rollno=int(input())
#         self.percentage=eval(input())
#     def display(self):
#         print(self.name)
#         print(self.rollno)
# p1=student()
# p1.stu()
# p1.display()
# class college:
#     def __init__(course,f1,f2):
#         course.f1=f1
#         course.f2=f2
# a=college("vineeta","28")
# print(a.f1)
# print(a.f2)
class college:
    def __init__(course,name,age):
        course.name=name
        course.age=age
    def __str__(course):
        return f"{course.name}({course.age})"
p1=college("vineeta",18)
print(p1)

