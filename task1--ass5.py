# Create dictionary of student Marks

#Create dictionary with student names and marks

student_marks = {
    "Alice": 85, "Bob": 90, "Carol": 70, "David": 92}

#Ask user for student name

name = input("Enter the student's name: ")

#retrieve marks or show error if not found

if name in student_marks:
    print(f"{name}'s marks:{student_marks[name]}")
else:
    print ("student not found.")


