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

	def create_population(self):
		# Create each dna pupulation
		self.population = [ "" for i in range(self.n_indiviudals) ]
		# Fill dna with random characters
		for i in range(len(self.population)):
			for _ in range(len(self.target)):
				self.population[i] += return_random_char()

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
		# best genes.
		offspring = []
		for i in range(self.n_indiviudals//2):
			parents     = np.random.choice(self.n_indiviudals, 2, p = self.fitness)
			cross_point = np.random.randint(self.ind_size)
			offspring  += [self.population[parents[0]][:cross_point] + self.population[parents[1]][cross_point:]]
			offspring  += [self.population[parents[1]][:cross_point] + self.population[parents[0]][cross_point:]]
		self.population = offspring





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
	model.calculate_fitness()
	model.crossover()

def loop():
	print("LOOP")


if __name__ == '__main__':
	main()
	#while True:
		#loop()
