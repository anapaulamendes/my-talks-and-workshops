import random

print("Modelo de entrada:")
print("a b c d e f g h i ... j")
print("Digite seu modelo:")
input_model = input()
model = [int(i) for i in input_model.split()]
print("\n")
print("Modelo: {}".format(model))
print("\n")
individual_size = len(model)
population_size = 10
parents = 2
mutation_probability = 0.5

def individual(min, max):
	return[random.randint(min, max) for i in range(individual_size)]

def create_population():
	return[individual(0,9) for i in range(population_size)]

def fitness(individual):
	fitness = 0
	for i in range(len(individual)):
		if(individual[i] == model[i]):
			fitness += 1
	return fitness

def selection_and_crossover(population):
	scored = [(fitness(i), i) for i in population]
	scored = [i[1] for i in sorted(scored)]
	population = scored
	selected = scored[(len(scored) - parents):]
	for i in range(len(population) - parents):
		point = random.randint(1, individual_size - 1)
		parent = random.sample(selected, 2)
		population[i][:point] = parent[0][:point]
		population[i][point:] = parent[1][point:]
	return population

def mutation(population):
	for i in range(len(population) - parents):
		if(random.random() <= mutation_probability):
			point = random.randint(0, individual_size - 1)
			new_value = random.randint(1, 9)
			while(new_value == population[i][point]):
				new_value = random.randint(1,9)
			population[i][point] = new_value
	return population

population = create_population()
print("População Inicial: {}".format(population))
print("\n")
for i in range(100):
	population = selection_and_crossover(population)
	population = mutation(population)
print("População Final: {}".format(population))