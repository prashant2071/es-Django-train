name ="prashant"
print(name)
print(f"name is {name}")
print("name is %s"%name)
print("name is "+name)
print("name is ",name)

# integer
age=29
if age > 22 and age < 30:
    print("start thinking about carrier")
if age < 22 or age >18:
    print("develop your skills")

# lists
fruits =["apple", "banana", "mango", "strawberry"]
print(fruits)
print(fruits[0])
print (type(fruits))
print (fruits[-1]) #last ko linxa as string
print (fruits[-2]) #secondlast ko linxa as string

print (fruits[-1:]) #last ko linxa as array
print (fruits[1:3]) #return index 1 to index (3-1)

print([fruit for fruit in fruits if fruit=="banana"])

for fruit in fruits:
    if fruit=="banana":
        print(fruit)

# Dictionary
students1_info ={
    "name":"prashanta",
    "age":22
}
print("the student info is ",students1_info["name"])
students =[{
    "name":"hello","age":18,"marks":80
},
{
    "name":"ramesh ","age":21,"marks":20
},{
    "name":"rakesh","age":29,"marks":50
}]
print("length of students is ",len(students))
name_with_age_greater_then_20=[]
for student in students:
    if student['age'] > 20:
        print("age greater then 20",name_with_age_greater_then_20.append(student))
pass_student=[]
for student in students:
    if student['marks'] > 40:
       print(f"{student} is pass")


def sum (a,b):
    s= a+b
    return s


print(sum(100,200))
#sum os marks
def sumofmarks(value):
    s=0
    for student in value:
        s=s+student['marks']
    return s
print(sumofmarks(students))

def averagemarks(value):
    s=0
    # for student in value:
    #     s=s+student['marks']
    s=sumofmarks(value);
    return s/len(value)
print(averagemarks(students))

x=1 
y=0
try:
    print(x/y)
except Exception as ex:
    print("Error:",ex)

# Object oriented programmings
