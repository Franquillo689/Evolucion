import numpy as np
import matplotlib.pyplot as plt

def return_random_char():
	# Return a random character between:
	# Space ! # $ % & ( ) * + - . 
	# / 0 1 2 3 4 5 6 7 8 9 : ; < = > ?
	# @ A B C D E F G H I J K L M N O P
	# Q R S T U V W X Y Z [ ] ^ _ a
	# b c d e f g h i j k l m n o p q r
	# s t u v w x y z { | } ~

	list = [' ', '!', '#', '$', '%', '&', '(', ')', 
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
	        ]
	return np.random.choice(list)
	#return list[randint(0,len(list)-1)]

class DNA:
	def __init__(self, n_indiviudals, target, mutation_rate):
		self.n_indiviudals = n_indiviudals # Cantidad de individuos
		self.target        = target        # ADN objetivo 
		self.mutation_rate = mutation_rate # Probabilidad de mutacion
		self.generation    = 1             # Numero de generacion
		self.ind_size      = len(target)   # Cantidad de genes
		self.fitness       = np.array([])  # Lista de fitness de la poblacion
		self.population    = []            # Lista con adn de la poblacion
		self.verbose       = False
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
		self.population = [ "" for i in range(self.n_indiviudals) ]
		# Fill dna with random characters
		for i in range(len(self.population)):
			for _ in range(len(self.target)):
				self.population[i] += np.random.choice(self.genetic_pool)

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
		#print("Fitness_list.sum(): ", fitness_list.sum())
		#print(fitness_list)
		self.fitness = fitness_list

	def crossover(self):
		# Do the reproduction of
		# best individuals.
		offspring = []
		for i in range(self.n_indiviudals//2):
			parents      = np.random.choice(self.n_indiviudals, 2, p = self.fitness)
			cross_point  = np.random.randint(self.ind_size)
			offspring   += [self.population[parents[0]][:cross_point] + self.population[parents[1]][cross_point:]]
			offspring   += [self.population[parents[1]][:cross_point] + self.population[parents[0]][cross_point:]]
		self.population  = offspring
		self.n_indiviudals = len(self.population)
		self.generation += 1

	def mutation(self):
		# Mutate new population
		for i in range(self.n_indiviudals):
			ind_dna = np.array(list(self.population[i]))
			for j in range(self.ind_size):
				prob = np.random.random()
				mutation = np.random.choice(self.genetic_pool)
				if prob < self.mutation_rate:
					ind_dna = mutation
			self.population[i] = ''.join(ind_dna)


	def best_individual(self):
		fitness   = 0
		max_index = 0
		for i in range(self.n_indiviudals):
			if self.fitness[i] > fitness:
				max_index = i
				fitness   = self.fitness[i]

		if self.population[max_index] == self.target:
			self.verbose = True

		return self.population[max_index]


'''
def main():
	target = "To be or not be." # AI target
	mutation_rate = 0.01 # Mutation rate
	popmax = 100 # Max problation
	# verbose is state when AI begins, when AI gets target verbose = True
	model = DNA(
					n_indiviudals = popmax, 
					target        = target, 
					mutation_rate = mutation_rate
				  )
	model.create_population() # Create initial population
'''
def loop():
	model.calculate_fitness()
	best_ind = model.best_individual()
	print("Mejor individuo: ",best_ind)
	model.crossover()
	model.mutation()

'''
if __name__ == '__main__':
	main()
	while True:
		if model.verbose:
			break
		loop()
'''



target = "To be or not be." # AI target
mutation_rate = 0.02 # Mutation rate
popmax = 700 # Max problation
# verbose is state when AI begins, when AI gets target verbose = True
model = DNA(
				n_indiviudals = popmax, 
				target        = target, 
				mutation_rate = mutation_rate
			  )
model.create_population() # Create initial population


while True:
	if model.verbose:
		print("Numero de generaciones: ", model.generation)
		break
	loop()