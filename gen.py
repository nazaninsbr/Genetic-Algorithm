import random 

#NUMBER_OF_ELITE_CHROMOSOMES = 1
POPULATION_SIZE = 8
TARGET_CHROMOSOME = [1, 1, 0, 1, 0, 0, 1, 1, 1, 0]


class Chromosome:
	def __init__(self):
		self.genes = []
		self.fitness = 0

		for i in range(POPULATION_SIZE):
			if random.random() >=0.5:
				self.genes.append(1)
			else:
				self.genes.append(0)

	def get_fitness(self):
		self.fitness = 0
		for i in range(len(self.genes)):
			if self.genes[i] == TARGET_CHROMOSOME[i]:
				self.fitness +=1

		return self.fitness

	def get_genes(self):
		return self.genes

	def print_info(self):
		return str(self.get_genes())+" Fitness: "+str(self.get_fitness())

	def crossover(self):
		i = random.randint(0, len(self.genes)-1)
		if random.random() >=0.5:
			self.genes[i] = 1
		else:
			self.genes[i] = 0;
		j = random.randint(0, len(self.genes)-1)
		if random.random() >=0.5:
			self.genes[j] = 1
		else:
			self.genes[j] = 0;

class Population:
	def __init__(self, size):
		self.chromosomes = []
		self.maxChromosomeId = 0
		for i in range(size):
			self.chromosomes.append(Chromosome())

	def get_chromosomes(self):
		return self.chromosomes
		
	def print_info(self):
		for i in range(len(self.chromosomes)):
			print("Chromosome #"+str(i)+" "+self.chromosomes[i].print_info())


	def findMaxChromosome(self):
		_max = 0
		for i in range(len(self.chromosomes)):
			num = self.chromosomes[i].get_fitness()
			if num > _max:
				_max = num
				self.maxChromosomeId = i

	def reachedCompleteFitness(self):
		self.findMaxChromosome()
		val = self.chromosomes[self.maxChromosomeId].get_fitness()
		if val == len(TARGET_CHROMOSOME) or (val == len(TARGET_CHROMOSOME)-1):
			return True
		return False

	def crossover_population(self):
		self.findMaxChromosome()
		for i in range(len(self.chromosomes)):
			if i == self.maxChromosomeId:
				continue 
			else:
				self.chromosomes[i].crossover()

class GeneticAlgorithm:
	def __init__(self):
		self.mypopulation = Population(POPULATION_SIZE)

	def print_population(self):
		print("\n--------------------------------")
		self.mypopulation.print_info()


	def mutate_population(self):
		pass

	def crossover_population(self):
		self.mypopulation.crossover_population()

	def evolve(self):
		self.crossover_population()
		self.mutate_population()

	def reachedCompleteFitness(self):
		return self.mypopulation.reachedCompleteFitness()









if __name__ == '__main__':
	GA = GeneticAlgorithm()
	while GA.reachedCompleteFitness()==False:
		GA.evolve()
		GA.print_population()













