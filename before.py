# before.py
def calculate_student_score(homework, exam, project):
    unused_var = 0
    homework_total = 0
    for score in homework:
        homework_total += score
    homework_avg = homework_total / len(homework)

    total = homework_avg * 0.3 + exam * 0.4 + project * 0.3
    if total >= 90:
        grade = "A"
    elif total >= 80:
        grade = "B"
    elif total >= 70:
        grade = "C"
    else:
        grade = "D"
    return total, grade

def calculate_teacher_score(attendance, test, paper):
    attendance_total = 0
    for score in attendance:
        attendance_total += score
    attendance_avg = attendance_total / len(attendance)

    total = attendance_avg * 0.3 + test * 0.4 + paper * 0.3
    if total >= 90:
        grade = "A"
    elif total >= 80:
        grade = "B"
    elif total >= 70:
        grade = "C"
    else:
        grade = "D"
    return total, grade

if __name__ == "__main__":
    calculate_student_score([80,90,85], 88, 92)
    calculate_teacher_score([95,98,96], 90, 94)
