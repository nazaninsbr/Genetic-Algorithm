import random 
import time
import copy

NUMBER_OF_SCHEDULES = 1000
NUMBER_OF_GENERATIONS = 10
MAX_NUMBER_OF_SCHEDULES = 200
OUTPUT_FILE_NAME = "out.txt"

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
				line.append([Course(-1, -1)])
			self.plan.append(line)

	def PlaceInFirstEmptySpace(self, index):
		for day_ in range(len(self.plan)):
			for timeSlot_ in range(len(self.plan[0])):
				if self.plan[day_][timeSlot_][0].getCourseId()==-1:
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
		while try_times<20:
			day_ = int((random.random())*100)%(self.days)
			timeSlot_ = int((random.random())*100)%(self.timeSlots)
			if self.hasConflict(index, self.plan[day_][timeSlot_])==False:
				self.plan[day_][timeSlot_].append(self.courses[index])
				return 1
			try_times +=1

		return -1 
			

	def createPlan(self):
		li = []
		while len(self.courses)>0:
			index = int((random.random())*100)%(len(self.courses))
			if (self.courses[index].getCourseId() in li)==False:
				emptySpace = self.PlaceInFirstEmptySpace(index)
				if emptySpace==-1:
					break
				li.append(self.courses[index].getCourseId())
			#self.sumHappiness += self.happiness[self.courses[index].getCourseId()-1]
			del self.courses[index]
		while len(self.courses)>0:
			index = int((random.random())*100)%(len(self.courses))
			if (self.courses[index].getCourseId() in li)==False:
				emptySpace = self.putInRandomPossiblePlace(index)
				if emptySpace!=-1:
					#print("Can't Have Course "+str(self.courses[index].getCourseId())+" This Semester")
					li.append(self.courses[index].getCourseId())
				# else:
					#self.sumHappiness += self.happiness[self.courses[index].getCourseId()-1]
			del self.courses[index]


	def fitness(self ,happiness = [] , sadness = []):
		self.sumHappiness = 0
		self.sumSadness = 0
		for d in self.plan:
			for t in d:
				for ncindex in range(len(t)):
					if t[ncindex].getCourseId() != -1:
						self.sumHappiness += int(happiness[t[ncindex].getCourseId()-1])
						for nrindex in range(ncindex+1, len(t)):
							if t[nrindex].getCourseId() != -1:
								if t[nrindex].getCourseId() != t[ncindex].getCourseId():
									self.sumSadness += int(sadness[t[ncindex].getCourseId()-1][t[nrindex].getCourseId()-1])
		totalFitness = self.sumHappiness - self.sumSadness 
		return totalFitness

	# def sortPlan(self):
	# 	for day in range(len(self.plan)):
	# 		for time in range(len(self.plan[day])):
	# 			for course in range(len(self.plan[day][time])):
	# 				for course2 in range(0, course):
	# 					if self.plan[day][time][course].getCourseId() <  self.plan[day][time][course2].getCourseId():
	# 						temp = copy.deepcopy(self.plan[day][time][course])
	# 						self.plan[day][time][course] = copy.deepcopy(self.plan[day][time][course2])
	# 						self.plan[day][time][course] = copy.deepcopy(temp)

	def printOutput(self, fitness):
		# self.sortPlan()
		file = open(OUTPUT_FILE_NAME, 'w')
		file.write(str(fitness)+'\n')
		for day in range(len(self.plan)):
			for time in range(len(self.plan[day])):
				for course in range(len(self.plan[day][time])):
					if self.plan[day][time][course].getCourseId() != -1:
						data = str(day+1)+" "+str(time+1)+" "+str(self.plan[day][time][course].getCourseId())+" "+ str(self.plan[day][time][course].getProf())
						file.write(data+'\n')
						#print(data)
		file.close()
	def printPlan(self):
		printedPlan = []
		for day in self.plan:
			printedPlan.append([])
			for time in day:
				printedPlan[-1].append([])
				for course in time:
					if course != -1:
						printedPlan[-1][-1].append(course.getCourseId())
					else:
						printedPlan[-1][-1].append(-1)
		print("Plan:"+str(printedPlan))


	def getPlan(self):
		return self.plan

	def getDayAndTime(self, dayRand1, timeRand1):
		return self.plan[dayRand1][timeRand1]

	def setPlan(self, plan):
		self.plan = copy.deepcopy(plan)


	def FixDuplicate(self):
		# addedCourses = []
		# for day in value:
		# 	for time in day:
		# 		for course in time:
		# 			addedCourses.append(course.getCourseId())
		# print(addedCourses)
		# if changedPart == 0:
		# 	for day in self.plan[len(value)-1:]:
		# 		for time in day:
		# 			for course in time:
		# 				if course.getCourseId() != -1:
		# 					if course.getCourseId() in addedCourses:
		# 						course = Course(-1, -1)
		# else:
		# 	for day in self.plan[:len(value)]:
		# 		for time in day:
		# 			for course in time:
		# 				if course.getCourseId() != -1:
		# 					if course.getCourseId() in addedCourses:
		# 						course = Course(-1, -1)
		seenCourses = []
		for day in range(len(self.plan)):
			for time in range(len(self.plan[day])):
				for course in range(len(self.plan[day][time])):
					if self.plan[day][time][course].getCourseId() != -1:
						if self.plan[day][time][course].getCourseId() in seenCourses:
							self.plan[day][time][course] = Course(-1, -1)
						else:
							seenCourses.append(self.plan[day][time][course].getCourseId())



	def changedDateAndTime(self, value):
		changedPart = int(random.random()*100)%2
		if changedPart==0:
			size = len(value)
			self.plan[0:size] = copy.deepcopy(value) 
		else:
			size = len(value)
			self.plan[len(self.plan)-size:] = copy.deepcopy(value)
		#temp = self.plan[day][time]
		#self.plan[day][time] = value 
		self.FixDuplicate()

	def mutate(self):
		for _ in range(self.days*self.timeSlots):
			while True:	
				dayRand = int(random.random()*100)%self.days
				timeRand = int(random.random()*100)%self.timeSlots
				if len(self.plan[dayRand][timeRand])>0:
					courseRand = int(random.random()*100)%(len(self.plan[dayRand][timeRand]))
					break
			thisCourse = self.plan[dayRand][timeRand][courseRand]
			del self.plan[dayRand][timeRand][courseRand]
			self.courses.append(thisCourse)
			self.putInRandomPossiblePlace(0)

	def beforeDay(self, midDay):
		return self.plan[0:midDay]


	def afterDay(self, midDay):
		return self.plan[midDay:]


class AllSchedules:
	def __init__(self, count, days, timeSlots, courses=[], happiness=[], sadness=[]):
		self.happiness = happiness
		self.sadness = sadness
		self.count = count
		self.schedules = []
		self.days = days
		self.timeSlots = timeSlots
		self.courses = courses
		self.expectedVal = 0
		self.calcExpectedVal()

	def createSchedules(self):
		now = time.time()	
		for i in range(self.count):
			#print("Plan: "+str(i))
			sch = Schedule(self.days, self.timeSlots, self.courses)
			self.schedules.append(sch)
		later = time.time()
		difference = int(later - now)
		print("Population Creation: "+str(difference)+" Seconds")


	def Calcfitness(self, plan):
		return plan.fitness(self.happiness, self.sadness)


	def swapSchedules(self, plan1index, plan2index):
		temp = self.schedules[plan1index]
		self.schedules[plan1index] = self.schedules[plan2index]
		self.schedules[plan2index] = temp


	def sortSchedulesList(self):		
		for plan1index in range(len(self.schedules)-1):
			for plan2index in range(0, plan1index):
				if self.Calcfitness(self.schedules[plan2index+1]) > self.Calcfitness(self.schedules[plan2index]):
					self.swapSchedules(plan2index+1, plan2index)

		# for plan in self.schedules:
		# 	print(self.Calcfitness(plan))

	def createNewPlan(self, plan, changedValue):
		thisPlan = plan[:]
		newPlan = Schedule(self.days, self.timeSlots, [])
		newPlan.setPlan(thisPlan)
		newPlan.changedDateAndTime(changedValue)
		self.schedules.append(newPlan)

	def crossOver(self):
		# print("crossover")
		#print("here")
		expert = self.schedules[0:20]
		for plan1 in expert:
			if int(random.random()*100)%5 == 1 and len(self.schedules)>4:
				plan2index = int(random.random()*100)%4
				#print(plan2index)
			else:
				plan2index = int(random.random()*100)%(len(self.schedules))
				#print(plan2index)

			midDay = int(self.days/2)

			dayAndTime1 = plan1.beforeDay(midDay)[:]
			dayAndTime2 = self.schedules[plan2index].afterDay(midDay)[:]
			self.createNewPlan(plan1.getPlan(), dayAndTime2)
			self.createNewPlan(self.schedules[plan2index].getPlan(), dayAndTime1)

			# print(self.Calcfitness(self.schedules[0]))


	def createNewPlanWithMutation(self, plan):
		newPlan = Schedule(self.days, self.timeSlots, [])
		newPlan.setPlan(plan)
		newPlan.mutate()
		self.schedules.append(newPlan)

	def mutation(self):
		print('mutating')
		planindex = int(random.random()*100)%(int(len(self.schedules)/2))
		if planindex+20<len(self.schedules):
			thisplan = self.schedules[planindex+20].getPlan()
			self.createNewPlanWithMutation(thisplan)



	def trimPopulation(self):
		while len(self.schedules)>MAX_NUMBER_OF_SCHEDULES:
			#print(self.Calcfitness(self.schedules[-1]))
			del self.schedules[-1]

	def sortCourses(self, temp):
		for i in range(len(temp)-1, 0, -1):
			for j in range(i):
				if self.happiness[temp[j].getCourseId()-1] > self.happiness[temp[j+1].getCourseId()-1]:
					tempTemp = temp[j]
					temp[j] = temp[j+1]
					temp[j+1] = tempTemp


	def calcExpectedVal(self):
		temp = self.courses[:]
		self.sortCourses(temp)
		for i in range(int(self.days*self.timeSlots)):
			self.expectedVal += int(self.happiness[temp[i].getCourseId()-1])

	def reachBestSchedule(self):
		prevMax = 0
		numberOfGenerations = NUMBER_OF_GENERATIONS
		self.sortSchedulesList()
		while True:
			now = time.time()
			numberOfGenerations -= 1
			newMax = self.Calcfitness(self.schedules[0])
			print("Max: "+str(newMax))
			#if newMax>self.expectedVal or numberOfGenerations==0 or abs(newMax-prevMax)<50:
			if numberOfGenerations==0 or abs(newMax-prevMax)<50:
			# if numberOfGenerations==0:
				break
			prevMax = newMax
			self.crossOver()
			self.sortSchedulesList()
			if int(random.random()*100)%2 == 1:
				self.mutation()
			self.trimPopulation()
			later = time.time()
			difference = int(later - now)
			print("Generation Creation Time: "+str(difference)+" Seconds")
			
		self.schedules[0].printOutput(newMax)


	def printInfo(self):
		print("All Plans:")
		for i in range(len(self.schedules)):
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
			elif len(profCourse)==1:
				self.all_courses.append(Course(profCourse[0], profID))
			else:
				continue

	def createPopulation(self):
		self.schedules = AllSchedules(NUMBER_OF_SCHEDULES , self.DAY_SLOT, self.TIME_SLOT, self.all_courses, self.valueofHappiness, self.sadness)
		self.schedules.createSchedules()
		self.schedules.reachBestSchedule()



def test():
	profCourses = input().split()
	print (convertListToInt(profCourses))

def test2():
	print("1{}".format([1, 2, 3]))


def sortFile():
	content = []
	file = open(OUTPUT_FILE_NAME, 'r')
	for line in file:
		if line != '\n':
			content.append(line.replace('\n', ''))
	file.close()

	for passnum in range(len(content)-1,0,-1):
		for i in range(1, passnum):
			line1Split = content[i].split()
			line2Split = content[i+1].split()
			# print("XX")
			# print(line1Split)
			# print(line2Split)
			if int(line1Split[0])==int(line2Split[0]) and int(line1Split[1])==int(line2Split[1]) and int(line1Split[2])>int(line2Split[2]):
				temp = copy.deepcopy(content[i])
				content[i] = copy.deepcopy(content[i+1])
				content[i+1] = copy.deepcopy(temp)
				# print("After Swap")
				# print(str(line1Split[2])+" > "+str(line2Split[2]))
				# print(content[i])
				# print(content[i+1])


	file = open(OUTPUT_FILE_NAME, 'w')
	for line in content:
		file.write(line+'\n')
	file.close()


def mainFunc():
	uni = University()
	uni.readInput()
	uni.createPopulation()
	sortFile()

if __name__ == '__main__':
	now = time.time()
	mainFunc()
	later = time.time()
	difference = int(later - now)
	print("Total Time: "+str(difference)+" Seconds")



