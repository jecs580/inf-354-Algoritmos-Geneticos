import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

# Problem parameter
NB_QUEENS = 4


def evalNQueens(individual):
    """Función de evaluación para el problema de n-reinas.
    El problema es determinar una configuración de n reinas 
    en un tablero de ajedrez nxn de modo que ninguna reina 
    pueda ser tomada entre ellas. En esta versión, 
    cada una de las reinas se asigna a una columna, 
    y solo una reina puede estar en cada línea. 
    Por lo tanto, la función de evaluación solo cuenta 
    el número de conflictos a lo largo de las diagonales.
    """
    size = len(individual)
    # Cuenta el número de conflictos con otras reinas.
    # Los conflictos solo pueden ser diagonales, cuente con cada línea diagonal
    left_diagonal = [0] * (2*size-1)
    right_diagonal = [0] * (2*size-1)

    # Suma el número de reinas en cada diagonal:
    for i in range(size):
        left_diagonal[i+individual[i]] += 1
        right_diagonal[size-1-i+individual[i]] += 1

    # Cuenta la cantidad de conflictos en cada diagonal
    sum_ = 0
    for i in range(2*size-1):
        if left_diagonal[i] > 1:
            sum_ += left_diagonal[i] - 1
        if right_diagonal[i] > 1:
            sum_ += right_diagonal[i] - 1
    return sum_,


creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Como solo hay una reina por línea,
# los individuos están representados por una permutación
toolbox = base.Toolbox()
toolbox.register("permutation", random.sample, range(NB_QUEENS), NB_QUEENS)

# Estructura de inicializadores
# Un individuo es una lista que representa la posición de cada reina.
# Solo se almacena la línea, la columna es el índice del número en la lista.
toolbox.register("individual", tools.initIterate,
                 creator.Individual, toolbox.permutation)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evalNQueens)
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=2.0/NB_QUEENS)
toolbox.register("select", tools.selTournament, tournsize=3)


def main(seed=0):
    random.seed(seed)

    pop = toolbox.population(n=8)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("Avg", numpy.mean)
    stats.register("Std", numpy.std)
    stats.register("Min", numpy.min)
    stats.register("Max", numpy.max)

    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=8, stats=stats,
                        halloffame=hof, verbose=True)

    return pop, stats, hof


if __name__ == "__main__":
    main()
