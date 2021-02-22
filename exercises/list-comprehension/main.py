# To create a list comprehension we can take for example the following lists. We want to add all the items in [numbers] to [new_list] but with a +1 added.

# numbers = [1, 2, 3, 4]
# new_list = []
#
# for i in numbers:
#     add_one = i + 1
#     new_list.append(add_one)

# A list comprehension would be done like this, to achieve the same as the above example.
#
# new_list = [i + 1 for i in numbers]
#
# # So basically we create it like this => new_list = [new_item for item in list]

# Double the values in a range
# new_list = [i * 2 for i in range(1, 5)]

# Conditional list comprehension
# new_list = [new_item for item in list if test]

# Uppercase the names into a new list but only names that are len() > 5
names = ["Bob", "John", "beth", "Jennifer", "Yunus", "Fatima", "Hikram", "Mohamed"]
new_list = [name.upper() for name in names if len(name) > 5]

print(new_list)
