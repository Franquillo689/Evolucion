from random import randint

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
	return list[randint(0,len(list)-1)]

class DNA:
	def __init__(self, n_indiviudals, target, mutation_rate, verbose):
		self.n_indiviudals = n_indiviudals
		self.target        = target
		self.mutation_rate = mutation_rate
		self.verbose       = verbose
	
	def create_population(self):
		# Create each dna pupulation
		self.population = [ "" for i in range(self.n_indiviudals) ]
		# Fill dna with random characters
		for i in range(len(self.population)):
			for _ in range(len(self.target)):
				self.population[i] += return_random_char()




def main():
	target = "To be or not be." # AI target
	mutation_rate = 0.01 # Mutation rate
	popmax = 10 # Max problation
	# verbose is state when AI begins, when AI gets target verbose = True
	model = DNA(
					n_indiviudals = popmax, 
					target        = target, 
					mutation_rate = mutation_rate, 
					verbose       = False
				  )
	model.create_population()

if __name__ == '__main__':
	main()