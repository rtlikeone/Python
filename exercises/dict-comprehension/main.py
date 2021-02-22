import random

## Dictionary comprehension
# Based on values in a list
# new_dict = {new_key: new_value for item in list}
# e.g. =>
names = ["Jonas", "Hailey", "Sammy", "Hakeem", "Mileena", "Hatiche"]
new_dict = {student: random.randint(1, 100) for student in names}

## Conditional Dictionary comprehension
# Based on values in existing dict.
# new_dict = { new_key: new_value for (key, value) in dict.items() }
# e.g. =>
# Based on values created in new_dict created above
passed_students = {student: score for (student, score) in new_dict.items() if score >= 60}

# print(new_dict)
# print(passed_students)
