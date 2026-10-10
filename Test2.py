#Create a program that stores a student's marks out of 100 and determines their grade using conditional statements.
#Award an A grade for marks of 90 or above, a B grade for marks between 80 and 89, a C grade for marks between 70 
# and 79, a D grade for marks between 60 and 69, and an F grade for marks below 60. Extend the program to calculate
#  grades for five students using a loop

students_marks = int(input("Please Enter a Number"))
if students_marks>90:
    print("You were awarded an A grade.")
elif students_marks>80 and students_marks<89:
    print("You were awarded a B grade.")
elif students_marks>70 and students_marks<79:
    print("You were awarded a C grade.")
elif students_marks>60 and students_marks<69:
    print("You were awarded a D grade.")
elif students_marks<60:
    print("You were awarded a F grade.")
