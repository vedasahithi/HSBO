import numpy as np
import random
from scipy.stats import levy


def secretary_bird(Swarm_size):

    # random initialization of the Secretary Birds’ positions in the search space.
    def initial_soln(p, lb, ub, M):
        soln = []
        for i in range(p):
            t = []
            for j in range(M):
                r = random.randint(0, 1)            # r denotes a random number between 0 and 1
                t.append(lb + r * (ub - lb))  # Equation 1
            soln.append(t)
        return soln

    def fitness(soln):
        # Objective function
        Fit = []
        for i in range(len(soln)):
            F = 0
            for j in range(len(soln[i])):
                hr = np.random.random()
                F += soln[i][j] * hr
            Fit.append(F)
        return Fit

    # Initialize problem setting

    Dim = 5
    lb, ub = 0, 10
    N = Swarm_size              # Population size
    T = 100             # Max iteration

    # Initialize the population randomly
    Position = initial_soln(N, lb, ub, Dim)

    Fitness = fitness(Position)             # Fitness of solution

    best_fit = np.min(Fitness)  # Best Fitness
    best = np.argmin(Fitness)  # Index of Best Fit
    best_soln = Position[best]  # Best solution

    for t in range(1, T):
        # t = current iteration number
        for j in range(1, N):
            # ------------ Hunting strategy of secretary bird (exploration phase) ------------
            # xrandom_1, xrandom_2 are the random candidate solutions in the frst stage iteration
            pos_1 = np.random.choice(len(Position), size=1, replace=False)
            X_rand1 = Position[pos_1[0]]

            pos_2 = np.random.choice(len(Position), size=1, replace=False)
            X_rand2 = Position[pos_2[0]]

            R1 = np.random.randint(0, 1, Dim)
            RB = np.random.randint(0, 1, Dim)  # Equation 6
            RL = 0.5 * levy.rvs(Dim)  # Equation 11
            R2 = np.random.randint(0, 1, Dim)

            if t < int(1/3*T):
                Position[j] = Position[j] + (np.subtract(X_rand1, X_rand2)) * R1          # Equation 4
                Fitness = fitness(Position)

                best_fit_new = np.argmin(Fitness)  # Best Fitness
                if best_fit_new < best_fit:
                    best_soln = Position[best_fit_new]

            elif t > int(1/3*T) and t < int(2/3*T):

                Position[j] = best_soln + np.exp(int(t/T) ^ 4) * (RB - 0.5) * (best_soln - Position[j])  # Equation 7
                Fitness = fitness(Position)
                best_fit_new = np.argmin(Fitness)  # Best Fitness
                if best_fit_new < best_fit:
                    best_soln = Position[best_fit_new]

            else:
                Position[j] = best_soln + ((1-int(t/T)) ^ int(2*t/T)) * Position[j] * RL  # Equation 9
                Fitness = fitness(Position)
                best_fit_new = np.argmin(Fitness)  # Best Fitness
                if best_fit_new < best_fit:
                    best_soln = Position[best_fit_new]

            r = random.uniform(0, 1)
            K = random.randint(0, 1)        # Equation 16
            # ------------ Escape strategy of secretary bird (exploitation stage) ------------

            if r < 0.5:
                C = best_soln + (2 * RB - 1) * (1 - int(t/T))*2 * Position[j]     # Equation 14
                Position[j] = C
                Fitness = fitness(Position)
                best_fit_new = np.argmin(Fitness)  # Best Fitness
                if best_fit_new < best_fit:
                    best_soln = Position[best_fit_new]
            else:
                # C = Position[j] + R2 * np.subtract(X_rand1, (K * Position[j]))      # Equation 14

                # UPDATE EQUATION
                C = (1/(2*np.cos(np.pi*t) - 1)) * ((R2* X_rand1)) * (1+2*np.cos(np.pi*t) - (Position[j] *
                                                                         (1 - 2*np.cos(np.pi*t)) * (1-R2*K)))

                Position[j] = C
                Fitness = fitness(Position)
                best_fit_new = np.argmin(Fitness)  # Best Fitness
                if best_fit_new < best_fit:
                    best_soln = Position[best_fit_new]
    BEST_SOLUTION = best_soln

    return np.mean(BEST_SOLUTION)







