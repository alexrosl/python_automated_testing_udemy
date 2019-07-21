# should_continue = True
# if should_continue:
# 	print("hello")

known_people = ["John", "Anna", "Mary"]
person = input("Enter the person you know: ")

if person in known_people:
	print("You know the person {}".format(person))
else:
	print("you don't know the person {}".format(person))


# Exercise

def who_do_you_know():
	people = input("Enter the names of people you know: ")
	people_list = people.split(",")
	people_without_spaces = []
	for person in people_list:
		people_without_spaces.append(person.strip())
	return people_without_spaces


def ask_user():
	person = input("Enter the person you know: ")
	if person in who_do_you_know():
		print("You know this person")


ask_user()
