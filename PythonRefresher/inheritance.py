class Student:
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average(self):
		return sum(self.marks) / len(self.marks)

	@classmethod
	def friend(cls, origin, friend_name, *args, **kwargs):
		return cls(friend_name, origin.school, *args, **kwargs)


##

class WorkingStudent(Student):
	def __init__(self, name, school, salary, job_title):
		super().__init__(name, school)
		self.salary = salary
		self.job_title = job_title

	def work(self):
		print("go to work")


anna = WorkingStudent("anna", "Oxford", 20.00, "qa")
print(anna.salary)
print(anna.name)

friend = WorkingStudent.friend(anna, "Greg", 17.65, job_title="Software developer")
print(friend.name)
print(friend.school)
print(friend.salary)
