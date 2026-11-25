from functools import total_ordering
StudentName="shruti"
StudentAge="18"
StudentAttendance="100%"
print("======================")
print("StudentDashBoard")
print("======================")
print(StudentName)
print(StudentAge)
print(StudentAttendance)
print("StudentDashBoardcreatedSuccesfully")

Studentid= int(input("Enter student ID:"))
Studentname=input("Enter your name:")
Subject1=input("Enter your subject1:")
Subject2=input("Enter your subject2:")
Subject3=input("Enter your subject3:")
NumofHrspersubject1=int(input("Enter your subject1:"))
NumofHrspersubject2=int(input("Enter your subject2:"))
NumofHrspersubject3=int(input("Enter your subject3:"))
totalhrspersubject=NumofHrspersubject1+NumofHrspersubject2+NumofHrspersubject3
averagehrspersubject=totalhrspersubject/3

print("=================================")
print("Student ID:", Studentid)
print("Student Name:", Studentname)
print("Subject 1:", Subject1)
print("Subject 2:", Subject2)
print("Subject 3:", Subject3)
print("NumofHrspersubjecr1:", NumofHrspersubject1)
print("NumofHrspersubject2:", NumofHrspersubject2)
print("NumofHrspersubject3:", NumofHrspersubject3)
print("totalHrspersubject:", NumofHrspersubject1+NumofHrspersubject2+NumofHrspersubject3)
