lotter_player_dict = {
	'name': 'Rolf',
	'numbers': (5, 9, 12, 3, 1, 21)
}


class LotteryPlayer:
	def __init__(self, name):
		self.name = name
		self.numbers = (5, 9, 12, 3, 1, 21)

	def total(self):
		return sum(self.numbers)


player_one = LotteryPlayer('Rolf')
player_two = LotteryPlayer('John')

print(player_one == player_two)


##

class Student:
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average(self):
		return sum(self.marks) / len(self.marks)

	@classmethod
	def go_to_school(cls):
		print("I'm going to school")


anna = Student("anna", "MIT")
anna.marks.append(56)
anna.marks.append(71)
print(anna.marks)
print(anna.average())
Student.go_to_school()
