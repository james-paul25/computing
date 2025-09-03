student = {"name" : "alice", "age" : 20, "major" : "bs in ultinig"}
student_updates = {"age": 26, "gpa": 3.8}
student.update(student_updates)

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))