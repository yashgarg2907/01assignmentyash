# Task : Students interview eligibility cheker:
academic_score=float(input("Enter Academim score percentage :"))
attendance_percentage=float(input("Enter Attendance percentage :"))
extracurricular_input=input("participate Extracurricular in extracurricular one activity ?(yes/no) :")
if academic_score >= 60 and attendance_percentage >= 75 and extracurricular_input=="yes" :
    print("Eligible for interview")
# elif extracurricular_input == "yes" :
#     print("Extracurricular : {extracuricular}")
else:
    print("Not eligible for interview") # this is doubt question