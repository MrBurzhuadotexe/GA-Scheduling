from random import randint
from random import choice


POPULATION_SIZE = 100
NUMBER_OF_GENERATIONS = 100000
MUTATION_INDEX = 2



def optimize(chromosome):
    time_per_machine = [0 for x in range(number_of_machines)]
    for i in range(len(chromosome)):
        time_per_machine[chromosome[i]] += time_per_process[i]



def random_chromosome(number_of_machines, number_of_processes):
    chromosome = []
    for proc in range(number_of_processes):
        chromosome.append(randint(0, number_of_machines - 1))
    return chromosome


def greedy(number_of_machines, processes, shift=0):
    chromosome = []
    # czas działania i-tej maszyny
    machines_occupation_time = [0 for x in range(number_of_machines)]

    # iść po każdemu procesu po koleje
    for proc in range(len(processes)):
        # znaleść wolną maszynę
        free_machine = machines_occupation_time.index(min(machines_occupation_time))

        chromosome.append((free_machine + shift) % number_of_machines)
        # zwiększyć czas działania tej maszyny
        machines_occupation_time[free_machine] += processes[proc]

    return chromosome


def fitness(chromosome):
    global number_of_machines, time_per_process
    time_per_machine = [0 for x in range(number_of_machines)]
    for i in range(len(chromosome)):
        time_per_machine[chromosome[i]] += time_per_process[i]
    return max(time_per_machine)


def mutation(chromosome, mutation_index=MUTATION_INDEX):
    global MUTATION_INDEX, number_of_machines
    number_of_mutations = randint(0, len(chromosome) // 100 * mutation_index)
    for i in range(number_of_mutations):
        chromosome[randint(0, len(chromosome)-1)] = randint(0, number_of_machines-1)
    return chromosome


def crossover(parent1, parent2):
    crossover_point = randint(1, len(parent1)-1)

    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    return mutation(child1), mutation(child2)


def gannt_chart(chrosome, scale):
    global number_of_machines, time_per_process
    chart = ['' for i in range(number_of_machines)]
    for i in range(len(chrosome)):
        index = str(i)
        string = '['+ '_'*(time_per_process[i]//(2*scale)) + index + '_'*(time_per_process[i]//(2*scale)) + ']'
        chart[chrosome[i]] += string
    for i in chart:
        print(i)


########################### driver code ###################################

filename = input()
file = open(filename, "r")

number_of_machines = int(file.readline())
number_of_processes = int(file.readline())

time_per_process = []
for i in file:
    time_per_process.append(int(i))


population = []

for i in range(POPULATION_SIZE//8):
    population.append(mutation(greedy(number_of_machines, time_per_process, randint(1, number_of_machines)), 100))
    population.append(mutation(greedy(number_of_machines, sorted(time_per_process, reverse=True), randint(1, number_of_machines)), 100))


while len(population) < POPULATION_SIZE:
    population.append(random_chromosome(number_of_machines, number_of_processes))

p_fit = fitness(population[0])

for i in range(NUMBER_OF_GENERATIONS):
    population = sorted(population, key=lambda x:fitness(x))

    if p_fit > fitness(population[0]):
        print(fitness(population[0]))


    p_fit = fitness(population[0])

    next_gen = population[:POPULATION_SIZE//10]

    for j in range(POPULATION_SIZE // 10 * 8):
        parent1 = choice(population[:POPULATION_SIZE // 2])
        parent2 = choice(population[:POPULATION_SIZE // 2])

        child1, child2 = crossover(parent1, parent2)

        next_gen.append(min(child1, child2, key=lambda x:fitness(x)))


    while len(next_gen) < POPULATION_SIZE:
       next_gen.append(random_chromosome(number_of_machines, number_of_processes))

    population = next_gen
