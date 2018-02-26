class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s: %s' % (self.name, self.score))
print(Student)

bart = Student('Bart haha', 99)
print(bart.name)

bart.age = 13
print(bart.age)

bart.print_score()

class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print('%s: %s' % (self.name, self.score))

bart = Student('bh', 33)
print(bart._Student__name)