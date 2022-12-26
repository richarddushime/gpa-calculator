def calculate_gpa():
  courses = []
  total_credit_hours = 0
  total_grade_points = 0
  
  while True:
    print("Enter course name (or 'done' to finish):")
    course_name = input()
    if course_name.lower() == "done":
      break
    
    print("Enter credit hours:")
    credit_hours = int(input())
    total_credit_hours += credit_hours
    
    print("Enter grade (A, B, C, D, or F):")
    grade = input().upper()
    grade_points = 0
    if grade == "A":
      grade_points = 4
    elif grade == "B":
      grade_points = 3
    elif grade == "C":
      grade_points = 2
    elif grade == "D":
      grade_points = 1
    else:
      grade_points = 0
    total_grade_points += grade_points * credit_hours
    
    courses.append((course_name, credit_hours, grade_points))
  
  gpa = total_grade_points / total_credit_hours
  print(f"Your GPA is {gpa:.2f}")

calculate_gpa()
