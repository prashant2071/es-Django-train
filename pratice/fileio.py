from student import StudentDetails
# for binary file
# with open("student.txt","rb") as file_object:

# for text file
with open("student.txt","r") as file_object:
    file_contents= file_object.read()
    print(file_contents); 

# writing in file
with open("student.txt","w") as file_object:
    file_contents= file_object.write("updated file")
#Appending file
with open("student.txt","a") as file_object:
    file_contents= file_object.write("\nThis is another line")

