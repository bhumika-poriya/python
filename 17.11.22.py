class school:
    def __init__(self,f1,f2):
        self.f1=f1
        self.f2=f2
#     def display(self):
#         print(self.f1,self.f2)
# class std(school):
#     pass
# x=std("vineeta",26)
# x.display()
class student(school):
    def __init__(self,f1,f2):
        school.__init__(self,f1,f2)
        print(self,f1,f2)
x=student("hazel grace lancaster",88)