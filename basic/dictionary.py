# dictionary is inclose with {}

student = {
    "name" : "james",
    "course" : "bscs",
    "age" : 20
}

# add f if you want to print an variable or dict inside of qoutes
print(f'student information: {student["name"]}') # print only the name
print(f'student information: {student}') # print all 

#print key with loops
for key in student:
    print(key)
    
#print values
for val in student.values():
    print(val)