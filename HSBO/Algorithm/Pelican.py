import numpy as np


def POA(objective_function, bounds, population_size, max_iterations):
    """
    Pelican Optimization Algorithm (POA)
    """

    # Initialize the pelican population
    population = np.random.uniform(bounds[:, 0], bounds[:, 1], (population_size, bounds.shape[0]))

    # Evaluate the fitness of each pelican
    fitness = np.apply_along_axis(objective_function, 1, population)

    # Find the best pelican
    best_index = np.argmin(fitness)
    best_solution = population[best_index]
    best_fitness = fitness[best_index]

    # Iterate until the maximum number of iterations is reached
    for iteration in range(max_iterations):

        # Update the position of each pelican
        for i in range(population_size):
            if np.random.rand() < 0.5:
                # Exploration phase
                new_solution = population[i] + np.random.uniform(-1, 1, bounds.shape[0]) * (best_solution - population[i])
            else:
                # Exploitation phase
                new_solution = population[i] + np.random.uniform(-1, 1, bounds.shape[0]) * \
                               (population[i] - population[np.random.randint(population_size)])

            # Check if the new solution is within bounds
            new_solution = np.clip(new_solution, bounds[:, 0], bounds[:, 1])

            # Evaluate the fitness of the new solution
            new_fitness = objective_function(new_solution)

            # Update the pelican's position if the new solution is better
            if new_fitness < fitness[i]:
                population[i] = new_solution
                fitness[i] = new_fitness

                # Update the best solution if necessary
                if new_fitness < best_fitness:
                    best_solution = new_solution
                    best_fitness = new_fitness

    return best_solution, best_fitness


# Example usage
def sphere_function(x):
    return np.sum(x ** 2)


def pelican_opt(swarm_size):
    bounds = np.array([[-5, 5], [-5, 5]])
    population_size = swarm_size
    max_iterations = 100

    best_solution, best_fitness = POA(sphere_function, bounds, population_size, max_iterations)

    return np.mean(best_solution)