class StudentContact:
    # if we don't use super in child class
    # mobile=981
    def __init__(self):   
      self.mobile=981
    # self.phone = 015

class StudentDetails(StudentContact):
    def _init_(self):
        self.name=None
        self.age=None
        self.marks=None
        # define only when parent class initailize
        super(StudentContact, self).__init__()
    def set_name(self,name):
        self.name=name
    def get_name(self) :
        return self.name
    def set_age(self,age):
        self.age=age
    def get_age(self) :
        return self.age
    def set_attribute(self,name,age,mobile):
        self.name=name
        self.age= age
        self.mobile=mobile


class StudentMark:
    def _init_(self):
        self.math_mark=0
        self.science=0
    def set_marks(self,math_mark,science_mark):
        self.math_mark=math_mark
        self.science_mark=science_mark
    def get_total_mark(self) :
        total= self.math_mark+self.science_mark
        return total

stu1= StudentDetails()
stu1.set_name("ram")
stu1.set_age(22)
print(stu1.get_age())
print(stu1.get_name())

class Student:
    @staticmethod
    def main(name,age,math_mark,science_mark,mobile):
        sd= StudentDetails()
        sd.set_attribute(name,age,mobile)
        sm= StudentMark()
        sm.set_marks(math_mark,science_mark)
        total= sm.get_total_mark()


        info=f"""
            Name:{sd.get_name()},
            Age:{sd.get_age()},
            mobile:{sd.mobile}
            Marks:{total},
              """
        
        with open(f"{name}.txt","a") as file_object:
           file_object.write(info)
# Student.main("ram",22,60,45)

students=[{"name":"ram","age":22,"math_mark":40,"science_mark":60,"mobile":983},{"name":"shyam","age":12,"math_mark":50,"science_mark":90,"mobile":983},{"name":"haha","age":22,"math_mark":44,"science_mark":91,"mobile":9834}]
for student in students:
    Student.main(student["name"],student["age"],student["math_mark"],student["science_mark"],student["mobile"])