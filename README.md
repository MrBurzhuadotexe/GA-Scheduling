# Genetic-Algorythm-Scheduling
### Desription 
A Genetic Algorithm (GA) is a heuristic optimization method inspired by the evolutionary process in nature. It is used to solve optimization problems where there are many possible solutions.
We begin by creating an initial population of individuals. The algorithm is based on the principle of "survival of the fittest," meaning literally crossing pairs of individuals, giving preference to the best ones. Selection is done through a **fitness function**, which assigns a value to each individual representing its quality from the perspective of the problem being solved. This function is the basic criteria that the algorithm will minimize.

We select individuals for reproduction based on their fitness values. The fitter they are, the more likely they are to be selected for reproduction. Next the pairs are selected for a **crossover**, their genes are exchanged to create new ones. Randomly selected genes in certain individuals are modified, simulating genetic **mutations**. Mutation introduces diversity into the population, which can help avoid convergence to a local optimum.

Based on selection, crossover and mutation, a new population of solutions is generated. The algorithm repeats these steps for a certain number of generations or until a termination condition is met.
### Visualization
In our case a single indivudual(chromosom) is represented by an array **[x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>i</sub>]** where **x** is an index of the machine on which the **ith** process is going to run.
![Снимок экрана 2024-01-22 040526](https://github.com/MrBurzhuadotexe/GA-Scheduling/assets/147132802/2aa3d594-14fa-438a-a989-e2beaf16ccfa)


Crossover operation:
![Снимок экрана 2024-01-22 043006](https://github.com/MrBurzhuadotexe/GA-Scheduling/assets/147132802/104d05d0-80d5-498e-84b6-3166f7c5de16)
![Снимок экрана 2024-01-22 044048](https://github.com/MrBurzhuadotexe/GA-Scheduling/assets/147132802/8017a068-ef81-4f86-9caa-517605a180e2)


Mutation operation:
![Снимок экрана 2024-01-22 044048](https://github.com/MrBurzhuadotexe/GA-Scheduling/assets/147132802/8ac4facc-b4ef-4d24-abb9-779f99434188)
![Снимок экрана 2024-01-22 044636](https://github.com/MrBurzhuadotexe/GA-Scheduling/assets/147132802/8adb59ce-a1d7-4c01-848a-5eba125b858c)


