class Student:
    pass
s1=Student()
s2=Student()
s3=Student()
print(s1)
print(type(s1))
s1.name="Pradeep"
s2.age=24
s3.name="Rohan"
s3.age=25


print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)



print(hasattr(s1,"name"))
print(hasattr(s1,"age"))


print(getattr(s1,"name"))
