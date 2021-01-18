# hackerrank problem: grading students

import os


def gradingStudents(grades):
    final_result = []

    for grade in grades:
        if grade >= 38 and grade % 5 > 2:
            grade = (grade + 5) - (grade % 5)
            final_result.append(grade)
        else:
            final_result.append(grade)

    return final_result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
