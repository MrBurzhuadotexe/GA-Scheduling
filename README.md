# Genetic-Algorythm-Scheduling
### Desription 
A Genetic Algorithm (GA) is a heuristic optimization method inspired by the evolutionary process in nature. It is used to solve optimization problems where there are many possible solutions.
We begin by creating an initial population of individuals. The algorithm is based on the principle of "survival of the fittest," meaning literally crossing pairs of individuals, giving preference to the best ones. Selection is done through a **fitness function**, which assigns a value to each individual representing its quality from the perspective of the problem being solved. This function is the basic criteria that the algorithm will minimize.
We select individuals for reproduction based on their fitness values. The fitter they are, the more likely they are to be selected for reproduction. Next the pairs are selected for ф **crossover**, their genes are exchanged to create new ones. Randomly selected genes in certain individuals are modified, simulating genetic **mutations**. Mutation introduces diversity into the population, which can help avoid convergence to a local optimum.
Based on selection, crossover and mutation, a new population of solutions is generated. The algorithm repeats these steps for a certain number of generations or until a termination condition is met.

