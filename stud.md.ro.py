from os import system
# Create dict student
student_score ={
    'firstname': 'James',
    'lastname'  : 'Smith',
    'age'   : 20,
    'grade_1'  : 10,
    'grade_2'  : 8.79,
    'grade_3'  : 4.129
}

# print dict elements, for grades display 2 decimals
for i, j in student_score.items():
    if i in('grade_1', 'grade_2', 'grade_3'):
        print(f"{i:>8} : {j:.2f}")
    else:    
        print(f"{i:>8} : {j}")

# calculate the average:

avg_grade = (student_score['grade_1'] + student_score['grade_2'] + student_score['grade_3'])/3
print(round(avg_grade,2))

# Check if the student passed the exam (avg>5.00)

if avg_grade >= 5:
    print("Congratulations you have passed the exam")
else:
    print(" You didn't pass the exam, please register for the next one!")