import numpy as np

class DNA:
	def __init__(self, n_indiviudals, target, mutation_rate):
		self.n_indiviudals = n_indiviudals # Individual amount
		self.target_str    = target
		self.target        = [ ord(i) for i in target ]        # DNA target 
		self.mutation_rate = mutation_rate # Mutation Rate
		self.generation    = 1             # Generation number
		self.ind_size      = len(target)   # Amount of genes
		self.fitness       = np.array([])  # Fitness list of population
		self.population    = []            # DNA list of each individual
		self.verbose       = False		     # When True => program must finish
		self.genetic_pool  = np.array([ 
							     ' ', '!', '#', '$', '%', '&', '(', ')', 
							     '*', '+', ',', '-', '.', '/', '~', '|',
	        				     '0', '1', '2', '3', '4', '5', '6', '7', 
	       					  '8', '9', ':', ';', '<', '=', '>', '?', 
	       					  '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 
	       					  'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
	       					  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
	       					  'X', 'Y', 'Z', '[', ']', '^', '_', 'a', 
	       					  'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
	       					  'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
	       					  'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
	        				     'z', '{', '}'
	       					 ])

	def create_population(self):
		# Create each dna pupulation
		self.population = [ [] for i in range(self.n_indiviudals) ]
		# Fill dna with random characters
		for i in range(len(self.population)):
			for _ in range(self.ind_size):
				# Pick a random number that corresponds to 
				# a character from self.genetic_pool.
				self.population[i].append(np.random.randint(32, 126))

	def calculate_fitness(self):
		# Calculate fitness of pupulation
		# Return a list with all fitness
		fitness_list = []
		for i in self.population:
			fitness = 0
			counter = 0
			for j in i:
				if j == self.target[counter]:
					fitness += 1 / self.ind_size
				counter += 1
			fitness_list.append(fitness)
		fitness_list = np.array(fitness_list)
		fitness_list = fitness_list / fitness_list.sum()
		self.fitness = fitness_list

	def crossover(self):
		# Do the reproduction of
		# best individuals.
		offspring = []
		for i in range(self.n_indiviudals//2):
			parents      = np.random.choice(self.n_indiviudals, 2, p = self.fitness)
			cross_point  = np.random.randint(self.ind_size)

			#print([self.population[parents[0]][:cross_point] + self.population[parents[1]][cross_point:]])
			#print([self.population[parents[1]][:cross_point] + self.population[parents[0]][cross_point:]])

			offspring   += [self.population[parents[0]][:cross_point] + self.population[parents[1]][cross_point:]]
			offspring   += [self.population[parents[1]][:cross_point] + self.population[parents[0]][cross_point:]]
		self.population    = offspring
		self.n_indiviudals = len(self.population)
		self.generation   += 1

	def mutation(self):
		# Mutate new population
		for i in range(self.n_indiviudals):
			ind_dna = self.population[i]
			for j in range(self.ind_size):
				prob = np.random.random()
				mutation = np.random.randint(32, 126)
				if prob < self.mutation_rate:
					ind_dna[j] = mutation
			self.population[i] = ind_dna


	def best_individual(self):
		# Return best individual
		fitness   = 0
		max_index = 0
		for i in range(self.n_indiviudals):
			if self.fitness[i] > fitness:
				max_index = i
				fitness   = self.fitness[i]

		best_ind = self.population[max_index]
		best_ind = ''.join([ chr(i) for i in best_ind ])

		if best_ind == self.target_str:
			# If best individual is equal
			# to the target, then finish program.
			self.verbose = True

		return best_ind


def loop():
	model.calculate_fitness()
	best_ind = model.best_individual()
	print("Best individual: ",best_ind)
	model.crossover()
	model.mutation()





target = "To be or not be." # AI target
mutation_rate = 0.01 # Mutation rate
popmax = 1000 # Max problation
model = DNA(
				n_indiviudals = popmax, 
				target        = target, 
				mutation_rate = mutation_rate
			  )
model.create_population() # Create initial population
#model.calculate_fitness()


#model.crossover()
#for i in model.population:
#	print(i)

#print(model.population)
while True:
	if model.verbose:
		print("Amount of generations: ", model.generation)
		break
	loop()

