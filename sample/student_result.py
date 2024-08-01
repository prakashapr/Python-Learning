student_dct = {
    "A":
       {
           "Kannada":90,
           "english":30
       },

    "B":
        {
            "Kannada": 60,
            "english": 90
        },
    "C":
        {
            "Kannada": 50,
            "english": 40
        },
}

### Print result for each student (Pass, Fail %)
## Print max %
## print max marks in each subject
## print pass fail after applying grace number for each subject

#min - 40 marks
#total= 100

def calculate_result(student_marks):
    results = {}

    for student, marks in student_marks.items():
        passed_all = True
        for subject, mark in marks.items():
            if mark < 35:
                passed_all = False
                break
        results[student] = "Pass" if passed_all else "Fail"
    return results

results = calculate_result(student_dct)
print("Results for each student (Pass/Fail):")
for student, result in results.items():
    print(f"{student}: {result}")


def calculate_percentage(marks):
    total_marks = sum(marks.values())
    num_subjects = len(marks)
    return (total_marks / (num_subjects * 100)) * 100

max_percentage = 0
top_student = ""
for student, marks in student_dct.items():
    percentage = calculate_percentage(marks)
    if percentage > max_percentage:
        max_percentage = percentage
        top_student = student

print(f"\nMax percentage: {max_percentage}% by student {top_student}")


def max_marks_in_subjects(student_marks):
    subjects = {}
    for marks in student_marks.values():
        for subject, mark in marks.items():
            if subject not in subjects or mark > subjects[subject]:
                subjects[subject] = mark
    return subjects

max_marks = max_marks_in_subjects(student_dct)
print("\nMax marks in each subject:")
for subject, mark in max_marks.items():
    print(f"{subject}: {mark}")

# 4. Print pass/fail after applying grace number to each subject
GRACE_MARKS = 5

def apply_grace_marks_and_calculate_result(student_marks, grace_marks):
    results = {}
    for student, marks in student_marks.items():
        passed_all = True
        for subject, mark in marks.items():
            if mark + grace_marks < 35:
                passed_all = False
                break
        results[student] = "Pass" if passed_all else "Fail"
    return results

grace_results = apply_grace_marks_and_calculate_result(student_dct, GRACE_MARKS)
print("\nResults for each student (Pass/Fail) after applying grace marks:")
for student, result in grace_results.items():
    print(f"{student}: {result}")







