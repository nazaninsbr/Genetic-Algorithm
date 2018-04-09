class Course:
	def __init__(self , value):
		self.course_id = -1
		self.time = -1
		self.day = -1
		# for course number i ci is value of happiness
		self.happiness_value = value
		self.offer = 1
		self.conflictCourses = []
		self.has_conflict = 1

	def conflict(self , Course course);
		conflict_course = list()
		if self.time == course.time and self.day == course.day:
			self.conflictCourses.append(course.course_id)
			course.has_conflict = 0
			self.has_conflict = 0


class Students:
	def __init__(self):
		# ci 
		self.hapiness = []
		# k i j 
		self.sadness = []
		self.ownCourse = []
	
	def readHappiness():
		valueofHappiness =  map(int, input().split())
		hapiness.append(valueofHappiness)

	def calHappiness(self , Course courses =[]):
		totalValue = 0
		for i in range (0 , len(courses)):
			if courses[i].offer != 1 :
				totalValue += courses[i].happiness_value
		return totalValue
	
	#def calSadness():



class Professor:
	def __init__(self):
		self.prof_id = -1
		self.my_courses = []



class University:
	def __init__(self):
		#list of course and prof
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
		self.students = []
		
	def readInput():	
		self.DAY_SLOT, self.TIME_SLOT = input()
		self.NUMBER_OF_COURSES = input()
		self.students.readHappiness()




if __name__ == '__main__':
	uni = University()
	uni.readInput()




