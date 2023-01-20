# declare

student_name = "Ronnie Colman"
student_roll = 21
student_height = 5.11

# type

print(student_name,type(student_name))
print(student_roll,type(student_roll))
print(student_height,type(student_height))

# address

print("Address of Current Roll : ",id(student_roll))
student_roll = 43
print("Address of Updated Roll : ",id(student_roll))
student_roll = 22
print("Address of Recent Updated Roll : ",id(student_roll))
