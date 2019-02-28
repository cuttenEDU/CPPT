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


print(filter_by_grade(4.5))
