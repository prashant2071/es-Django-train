class StudentContact:
    mobile=None
class studentDetail(StudentContact):
    # constructor initialization and (self act as object)
    def __init__(self) :
        self.name=None
        self.age=None
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name   
    def set_age(self,age):
        self.age=age
    def get_age(self): 
        return self.age
    def set_attribute(self, name, age,mobile):
        self.name=name
        self.age=age
        self.mobile=mobile
    
# std = studentDetail()
# std.set_age(22)
# std.set_name("chandrakala")
# print (std.get_age())
# print (std.get_name())

class StudentMark:
    def __init__(self):
        self.math_mark=0
        self.science_mark=0

    def set_marks(self,math_mark,science_mark):
        self.math_mark=math_mark
        self.science_mark=science_mark

    def get_total_marks(self):
        total= self.math_mark + self.science_mark
        return total

class Student:
    """
    this class sets the details of a student,
    calcuate the total marks and sets the details
    """
    @staticmethod
    def main(name, age,mobile, math_mark, science_mark):
        sd = studentDetail()
        sd.set_attribute(name,age,mobile)
        sm= StudentMark()
        sm.set_marks(math_mark,science_mark)
        total= sm.get_total_marks()

        # print(f"""
        # Name:{sd.get_name()},
        # Age:{sd.get_age()},
        # Mobile:{sd.mobile}
        # Marks:{total}
        # """)
        info = f"""
        Name:{sd.get_name()},
        Age:{sd.get_age()},
        Mobile:{sd.mobile}
        Marks:{total}
        """
        
        with open(f"{name}.txt","a") as file_object:
            file_object.write(info)
                
students = [
	{"name": "hari", "age": 22, "mobile":981, "math_mark": 99, "science_mark": 85},
	{"name": "sita", "age": 21, "mobile":982, "math_mark": 90, "science_mark": 95}
]
for student in students:
    Student.main(
            student["name"],
            student["age"],
            student["mobile"],
            student["math_mark"],
            student["science_mark"]

		)