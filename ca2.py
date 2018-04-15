import random 

NUMBER_OF_SCHEDULES = 10

def convertListToInt(li):
	newli = []
	for x in li:
		newli.append(int(x))
	return newli

class Course:
	def __init__(self, courseId, prof):
		self.courseId = courseId
		self.prof = prof

	def getProf(self):
		return self.prof

	def getCourseId(self):
		return self.courseId

class Schedule:
	def __init__(self, days, timeSlots, courses=[]):
		self.plan = []
		self.days = days
		self.timeSlots = timeSlots
		self.courses = courses[:]
		self.makeEmptyPlan()
		self.createPlan()

	def makeEmptyPlan(self):		
		for _ in range(self.days):
			line = []
			for _ in range(self.timeSlots):
				line.append([-1])
			self.plan.append(line)

	def PlaceInFirstEmptySpace(self, index):
		for day_ in range(len(self.plan)):
			for timeSlot_ in range(len(self.plan[0])):
				if self.plan[day_][timeSlot_]==[-1]:
					self.plan[day_][timeSlot_][0] = self.courses[index].getCourseId()
					return 1
		return -1


	def hasConflict(self, index, courseList = []):
		for item in courseList:
			if item.getProf() == self.courses[index].getProf():
				return True
		return False 


	def putInRandomPossiblePlace(self, index):
		try_times = 0
		while try_times<10:
			day_ = int((random.random())*100)%(self.days)
			timeSlot_ = int((random.random())*100)%(self.timeSlots)
			if hasConflict(index, self.courses[day_][timeSlot_])==False:
				self.courses[day_][timeSlot_].append(self.courses[index].getCourseId())
				return 1
			try_times +=1

		return -1 
			

	def createPlan(self):
		while len(self.courses)>0:
			index = int((random.random())*100)%(len(self.courses))
			emptySpace = self.PlaceInFirstEmptySpace(index)
			if emptySpace==-1:
				break
			del self.courses[index]

		while len(self.courses)>0:
			index = int((random.random())*100)%(len(self.courses))
			emptySpace = self.putInRandomPossiblePlace(index)
			if emptySpace==-1:
				print("Can't Have Course "+str(self.courses[index].getCourseId())+" This Semester") 
			del self.courses[index]

	def printPlan(self):
		print("Plan: {}".format(self.plan))


class AllSchedules:
	def __init__(self, count, days, timeSlots, courses=[]):
		self.count = count
		self.schedules = []
		self.days = days
		self.timeSlots = timeSlots
		self.courses = courses

	def createSchedules(self):
		for i in range(self.count):
			sch = Schedule(self.days, self.timeSlots, self.courses)
			self.schedules.append(sch)


	def printInfo(self):
		print("All Plans:")
		for i in range(self.count):
			self.schedules[i].printPlan()

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
		self.courses_by_profs = []
		self.all_courses = []
		self.sadness = []
		self.valueofHappiness = []
		# c
		self.NUMBER_OF_COURSES = 0 
		# p 
		self.NUMBER_OF_PROFS = 0
		# t
		self.TIME_SLOT = 0
		# d
		self.DAY_SLOT = 0

		self.schedules = ""
		

	def printInfo(self):
		print("Professors: {}".format(self.profs))
		print("Courses: {}".format(self.courses_by_profs))
		print("Sadness: {}".format(self.sadness))


	def readInput(self):	
		self.DAY_SLOT, self.TIME_SLOT = map(int, input().split())
		self.NUMBER_OF_COURSES = int(input())
		self.valueofHappiness = input().split()
		self.NUMBER_OF_PROFS = int(input())
		for numP in range(self.NUMBER_OF_PROFS):
			profCourses = input().split()
			profCourses = convertListToInt(profCourses)
			numOFCourses = profCourses[0]
			del profCourses[0]
			self.profs.append(Professor(numP, numOFCourses,profCourses))
			self.courses_by_profs.append(profCourses)
		for i in range(self.NUMBER_OF_COURSES):
			sadnessLine = input().split()
			sadnessLine = convertListToInt(sadnessLine)
			self.sadness.append(sadnessLine)

		self.makeAllCourses()

	def makeAllCourses(self):
		profID = -1;		
		for profCourse in self.courses_by_profs:
			profID +=1
			if len(profCourse)>1:
				for course in profCourse:
					self.all_courses.append(Course(course, profID))
			else:
				self.all_courses.append(Course(profCourse[0], profID))

	def createPopulation(self):
		self.schedules = AllSchedules(NUMBER_OF_SCHEDULES , self.DAY_SLOT, self.TIME_SLOT, self.all_courses)
		self.schedules.createSchedules()
		self.schedules.printInfo()



def test():
	profCourses = input().split()
	print (convertListToInt(profCourses))

def test2():
	print("1{}".format([1, 2, 3]))

def mainFunc():
	uni = University()
	uni.readInput()
	uni.createPopulation()

if __name__ == '__main__':
	mainFunc()




