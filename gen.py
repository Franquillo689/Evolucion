class DNA:
	def __init__(self, n_indiviudals, target, mutation_rate, verbose):
		self.n_indiviudals = n_indiviudals
		self.target        = target
		self.mutation_rate = mutation_rate
		self.verbose       = verbose
	
	def create_population(self):
		self.population = ["" for i in range(self.n_indiviudals)]
		print(self.population)






def main():
	target = "To be or not to be."
	mutation_rate = 0.01
	model = DNA(n_indiviudals = 400, target = target, mutation_rate = mutation_rate, verbose = False)
	model.create_population()


if __name__ == '__main__':
	main()