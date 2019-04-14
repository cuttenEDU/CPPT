# coding:UTF-8
from __future__ import division

groupmates = [
    {
        "name": u"Василий",
        "group": "912-2",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": u"Анна",
        "group": "912-1",
        "age": 18,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": u"Георгий",
        "group": "912-2",
        "age": 19,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": u"Валентина",
        "group": "912-1",
        "age": 18,
        "marks": [5, 5, 5, 4, 5]

    }
]


def filter_by_grade(grade):
    good_groupmates = []
    for groupmate in groupmates:
        total_mark = 0
        marks = groupmate.get("marks")
        for mark in marks:
            total_mark = total_mark + mark
        if total_mark / len(marks) > grade:
            good_groupmates.append(groupmate)
    return good_groupmates



def print_students(students):
    print u"Имя студента".ljust(15), \
        u"Группа".ljust(8), \
        u"Возраст".ljust(8), \
        u"Оценки".ljust(20)
    for student in students:
        print \
            student["name"].ljust(15), \
            student["group"].ljust(8), \
            str(student["age"]).ljust(8), \
            str(student["marks"]).ljust(20)
    print "\n"


print_students(filter_by_grade(4))
