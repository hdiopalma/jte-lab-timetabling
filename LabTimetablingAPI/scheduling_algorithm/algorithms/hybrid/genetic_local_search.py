#Hybrid Algorithm Class
# Create a hybrid algorithm class that combine the genetic algorithm and tabu search, the genetic algorithm will be used to generate the initial solution and focus on the exploration, while the tabu search will be used to improve the solution and focus on the exploitation.

from re import S
from scheduling_algorithm.structure import Chromosome, Population

from scheduling_algorithm.algorithms.global_search.genetic_algorithm import GeneticAlgorithm

from scheduling_algorithm.algorithms.local_search.tabu_search import TabuSearch
from scheduling_algorithm.algorithms.local_search.simulated_annealing import SimulatedAnnealing

from scheduling_algorithm.factory.factory import Factory

from scheduling_algorithm.fitness_function import FitnessManager
from scheduling_algorithm.operator.crossover import CrossoverManager
from scheduling_algorithm.operator.mutation import MutationManager
from scheduling_algorithm.operator.repair import RepairManager
from scheduling_algorithm.operator.selection import SelectionManager, ElitismSelection

import time

class GeneticLocalSearch(GeneticAlgorithm):
    def __init__(self):
        super().__init__()
        self.local_search = SimulatedAnnealing()
    
    def __str__(self):
        return f"GeneticLocalSearch(factory={self.factory}, selection_manager={self.selection_manager}, crossover_manager={self.crossover_manager}, mutation_manager={self.mutation_manager}, repair_manager={self.repair_manager}, elitism_size={self.elitism_size}, local_search={self.local_search})"
    
    def __repr__(self):
        return self.__str__()
    
    def run(self, max_iteration: int, population_size: int):
        '''Run the hybrid algorithm.
        '''
        time_start = time.time()
        # Initialize the population
        population = self._init_population(population_size)
        # Calculate the fitness of the population
        population.calculate_fitness()
        # Sort the population based on fitness
        population = Population(sorted(population, key=lambda chromosome: chromosome.fitness), population.fitness_manager)
        # Initialize the best chromosome
        best_chromosome = population[0].copy()
        # Initialize the iteration
        iteration = 0
        # Start the hybrid algorithm
        while iteration < max_iteration and best_chromosome.fitness > 0:
            # Evolve the population, crossover and mutation happens inside this function
            population, elitism = self._evolve_population(population)

            # Add the elitism and the local search to the population
            population.add_chromosome(elitism)
            population.calculate_fitness()

            # Introduction of local search, for possible improvement of previous best chromosome
            local_search = self.local_search(best_chromosome)
            population.add_chromosome(local_search)

            # Sort the population based on fitness
            population = Population(sorted(population, key=lambda chromosome: chromosome.fitness), population.fitness_manager)
            #remove the worst chromosome, so the population size is still the same
            population.pop()
            # Check if the best chromosome is better than the current best chromosome
            if population[0].fitness < best_chromosome.fitness:
                best_chromosome = population[0].copy()

            iteration += 1
        time_end = time.time()
        self.log['time_elapsed'] = time_end - time_start
        return best_chromosome
    
    def configure(self, factory: Factory = None, fitness_manager: FitnessManager = None, selection_manager: SelectionManager = None, crossover_manager: CrossoverManager = None, mutation_manager: MutationManager = None, repair_manager: RepairManager = None, elitism_selection: ElitismSelection = None, elitism_size: int = 1, local_search: TabuSearch = None):
        '''Configure the hybrid algorithm, use None to use the default value.
        '''
        self.elitism_size = elitism_size or self.elitism_size
        self.elitism_selection = elitism_selection or self.elitism_selection
        self.factory = factory or self.factory
        self.fitness_manager = fitness_manager or self.fitness_manager
        self.selection_manager = selection_manager or self.selection_manager
        self.crossover_manager = crossover_manager or self.crossover_manager
        self.mutation_manager = mutation_manager or self.mutation_manager
        self.repair_manager = repair_manager or self.repair_manager
        self.local_search = local_search or self.local_search
        return self
