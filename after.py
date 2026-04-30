# after.py
def calculate_average(scores):
    total = sum(scores)
    return total / len(scores)

def get_grade(total_score):
    if total_score >= 90:
        return "A"
    elif total_score >= 80:
        return "B"
    elif total_score >= 70:
        return "C"
    else:
        return "D"

def calculate_student_score(homework, exam, project):
    homework_avg = calculate_average(homework)
    total = homework_avg * 0.3 + exam * 0.4 + project * 0.3
    return total, get_grade(total)

def calculate_teacher_score(attendance, test, paper):
    attendance_avg = calculate_average(attendance)
    total = attendance_avg * 0.3 + test * 0.4 + paper * 0.3
    return total, get_grade(total)

if __name__ == "__main__":
    calculate_student_score([80,90,85], 88, 92)
    calculate_teacher_score([95,98,96], 90, 94)
