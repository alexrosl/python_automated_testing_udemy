my_variable = "hello"
grades = [77, 80]
tuple_grades = (77, 80, 90)
set_grades = {77, 80, 90}

# print(sum(grades)/len(grades))

# print(grades)
# print(tuple_grades)
# print(set)

grades.append(100)
# print(grades)

tuple_grades = tuple_grades + (101,)
# print(tuple_grades)

grades[0] = 60
# print(grades[0])

set_grades.add(60)
set_grades.add(80)
# print(set)


# Set operations

set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9, 11}

# print(set_one.intersection(set_two))
print(set_one.union(set_two))
print(set.union(set_two))
print(set_one.difference(set_two))
