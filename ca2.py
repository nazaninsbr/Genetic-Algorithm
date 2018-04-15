import random 

NUMBER_OF_SCHEDULES = 20

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
		self.sumHappiness = 0
		self.sumSadness = 0
		# self.happiness = happiness
		# self.sadness = sadness
		self.courses = courses[:]
		self.makeEmptyPlan()
		self.createPlan()
	
	def gettimeSlots(self):
		return self.timeSlots
	
	def getdays(self):
		return self.days

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
					self.plan[day_][timeSlot_][0] = self.courses[index]
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
				self.plan[day_][timeSlot_].append(self.courses[index])
				return 1
			try_times +=1

		return -1 
			

	def createPlan(self):
		while len(self.courses)>0:
			index = int((random.random())*100)%(len(self.courses))
			emptySpace = self.PlaceInFirstEmptySpace(index)
			if emptySpace==-1:
				break
			#self.sumHappiness += self.happiness[self.courses[index].getCourseId()-1]
			del self.courses[index]
		while len(self.courses)>0:
			index = int((random.random())*100)%(len(self.courses))
			emptySpace = self.putInRandomPossiblePlace(index)
			if emptySpace==-1:
				print("Can't Have Course "+str(self.courses[index].getCourseId())+" This Semester")
			# else:
				#self.sumHappiness += self.happiness[self.courses[index].getCourseId()-1]
			del self.courses[index]

	def fitness(self ,happiness = [] , sadness = []):
		self.sumHappiness = 0
		self.sumSadness = 0
		for d in self.plan:
			for t in d:
				for nc in t:
					self.sumHappiness += int(happiness[nc.getCourseId()-1])
					for nr in t:
						if nr.getCourseId() != nc.getCourseId():
							self.sumSadness += int(sadness[nc.getCourseId()-1][nr.getCourseId()-1])
		totalFitness = self.sumHappiness - self.sumSadness 
		return totalFitness

	def printOutput():
		for i in range(0 , len(plan)):
			for j in range(i , len(plan)):
				for k in range(0 , len(self.courses)):
					print("[" + self.plan[i][j].courses[k].getCourseId() + "]" + "[" + self.plan[i][j].courses[k].getProf() + "]" + "[" + self.plan[i][j].getDayAndTime()+"]")

	def printPlan(self):
		print("Plan: {}".format(self.plan))

	def printOutput(self):
		self.printPlan()

	def getPlan(self):
		return self.plan

	def getDayAndTime(self, dayRand1, timeRand1):
		return self.plan[dayRand1][timeRand1]

	def setPlan(self, plan):
		self.plan = plan

	def changedDateAndTime(self, value, day, time):
		temp = self.plan[day][time]
		self.plan[day][time] = value 


class AllSchedules:
	def __init__(self, count, days, timeSlots, courses=[], happiness=[], sadness=[]):
		self.happiness = happiness
		self.sadness = sadness
		self.count = count
		self.schedules = []
		self.days = days
		self.timeSlots = timeSlots
		self.courses = courses

	def createSchedules(self):
		for i in range(self.count):
			sch = Schedule(self.days, self.timeSlots, self.courses)
			self.schedules.append(sch)


	def Calcfitness(self, plan):
		return plan.fitness(self.happiness, self.sadness)


	def swapSchedules(self, plan1index, plan2index):
		temp = self.schedules[plan1index]
		self.schedules[plan1index] = self.schedules[plan2index]
		self.schedules[plan2index] = temp


	def sortSchedulesList(self):		
		for plan1index in range(len(self.schedules)):
			for plan2index in range(0, plan1index):
				if self.Calcfitness(self.schedules[plan1index]) < self.Calcfitness(self.schedules[plan2index]):
					self.swapSchedules(plan1index, plan2index)

	def createNewPlan(self, plan, changedValue, day, time):
		newPlan = Schedule(self.days, self.timeSlots, self.courses)
		newPlan.setPlan(plan)
		newPlan.changedDateAndTime(changedValue, day, time)
		self.schedules.append(newPlan)

	def crossOver(self):
		#print("here")
		for plan1 in self.schedules:
			if int(random.random()*100)%10 == 1 and len(self.schedules)>4:
				plan2index = int(random.random()*100)%4
				#print(plan2index)
			else:
				plan2index = int(random.random()*100)%(len(self.schedules))
				#print(plan2index)

			dayRand1 = int(random.random()*100)%self.days
			dayRand2 = int(random.random()*100)%self.days
			timeRand1 = int(random.random()*100)%self.timeSlots
			timeRand2 = int(random.random()*100)%self.timeSlots

			dayAndTime1 = plan1.getDayAndTime(dayRand1, timeRand1)
			dayAndTime2 = self.schedules[plan2index].getDayAndTime(dayRand2, timeRand2)
			self.createNewPlan(plan1.getPlan(), dayAndTime1, dayRand1, timeRand1)
			self.createNewPlan(self.schedules[plan2index].getPlan(), dayAndTime2, dayRand2, timeRand2)

	def mutation(self):
		return 0


	def trimPopulation(self):
		while len(self.schedules)>100:
			del self.schedules[-1]



	def reachBestSchedule(self):
		self.sortSchedulesList()
		while True:
			print(self.Calcfitness(self.schedules[0]))
			self.crossOver()
			if int(random.random()*100)%50 == 1:
				self.mutation()
			self.sortSchedulesList()
			self.trimPopulation()
			#self.printInfo()
			if self.Calcfitness(self.schedules[0])>0:
				break
		self.schedules[0].printOutput()


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
		self.schedules = AllSchedules(NUMBER_OF_SCHEDULES , self.DAY_SLOT, self.TIME_SLOT, self.all_courses, self.valueofHappiness, self.sadness)
		self.schedules.createSchedules()
		self.schedules.reachBestSchedule()



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




