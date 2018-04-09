def convertListToInt(li):
	newli = []
	for x in li:
		newli.append(int(x))
	return newli


class Course:
	def __init__(self , value):
		self.course_id = -1
		self.time = -1
		self.day = -1
		# for course number i ci is value of happiness
		self.happiness_value = value
		self.offer = False
		self.conflictCourses = []
		self.has_conflict = False

	# def conflict(self , Course course):
	# 	conflict_course = list()
	# 	if self.time == course.time and self.day == course.day:
	# 		self.conflictCourses.append(course.course_id)
	# 		course.has_conflict = 0
	# 		self.has_conflict = 0


class Students:
	def __init__(self):
		# ci 
		self.hapiness = []
		# k i j 
		self.sadness = []
		self.ownCourse = []
	
	def readHappiness():
		
		self.hapiness.append(valueofHappiness)

	# def calHappiness(self , Course courses =[]):
	# 	totalValue = 0
	# 	for i in range (0 , len(courses)):
	# 		if courses[i].offer != 1 :
	# 			totalValue += courses[i].happiness_value
	# 	return totalValue
	
	#def calSadness():







class Professor:
	def __init__(self, prof_id, number_of_courses, my_courses=[]):
		self.prof_id = prof_id
		self.my_courses = my_courses
		self.number_of_courses = number_of_courses

	def printInfo(self):
		print("prof_id: "+ str(self.prof_id))



class University:
	def __init__(self):
		#list of course and prof
		self.profs = []
		self.courses = []
		self.sadness = []
		# c
		self.NUMBER_OF_COURSES = 0 
		# p 
		self.NUMBER_OF_PROFS = 0
		# t
		self.TIME_SLOT = 0
		# d
		self.DAY_SLOT = 0
		self.students = []
		

	def printInfo(self):
		print("Professors: {}".format(self.profs))
		print("Courses: {}".format(self.courses))
		print("Sadness: {}".format(self.sadness))


	def readInput(self):	
		self.DAY_SLOT, self.TIME_SLOT = map(int, input().split())
		self.NUMBER_OF_COURSES = int(input())
		valueofHappiness = input().split()
		self.NUMBER_OF_PROFS = int(input())
		for numP in range(self.NUMBER_OF_PROFS):
			profCourses = input().split()
			profCourses = convertListToInt(profCourses)
			numOFCourses = profCourses[0]
			del profCourses[0]
			self.profs.append(Professor(numP, numOFCourses,profCourses))
			self.courses.append(profCourses)
		for i in range(self.NUMBER_OF_COURSES):
			sadnessLine = input().split()
			sadnessLine = convertListToInt(sadnessLine)
			self.sadness.append(sadnessLine)





def test():
	profCourses = input().split()
	print (convertListToInt(profCourses))

def test2():
	print("1{}".format([1, 2, 3]))

def mainFunc():
	uni = University()
	uni.readInput()
	uni.printInfo()

if __name__ == '__main__':
	mainFunc()




