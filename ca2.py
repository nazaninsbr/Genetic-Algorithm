class Course:
	def __init__(self):
		self.course_id = -1
		self.time = -1
		self.day = -1

class Students:
	def __init__(self):
		# ci 
		self.hapiness = []
		# k i j 
		self.sadness = [][]

	def readHappiness():
		line = input()
		#separate by space 

class Professor:
	def __init__(self):
		self.prof_id = -1
		self.my_courses = []



class University:
	def __init__(self):
		self.profs = []
		self.courses = []
		# c
		self.NUMBER_OF_COURSES = 0 
		# p 
		self.NUMBER_OF_PROFS = 0
		# t
		self.TIME_SLOT = 0
		# d
		self.DAY_SLOT = 0
		self.students = Students()
		
	def readInput():	
		self.DAY_SLOT, self.TIME_SLOT = input()
		self.NUMBER_OF_COURSES = input()
		self.students.readHappiness()






if __name__ == '__main__':
	uni = University()
	uni.readInput()




