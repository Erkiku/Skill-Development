marks = int(input("Enter marks of Student:"))

if(marks>90 and marks<=100):
  print("Student Pass With A+ Grade:")
  
elif (marks>80 and marks < 90):
  print("Stdudent Pass With A Grade")
  
elif (marks > 70 and marks < 80):
  print("Student Pass with B Grade")
  
elif (marks >60 and marks < 70):
  print("Student Pass with C Grade")
else:
  if(marks<60):
    print("Better Luck Next Time")
  else: 
    print("Better Luck Next Time!")