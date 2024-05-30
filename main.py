import random
import math


class Solution:
    def __init__(self):
        self.genotype = [random.randint(0, 9) for _ in range(5)]
        self.fitness = 0
        self.difference = 0


class GA:
    def __init__(self):
        self.populationSize = 100
        self.maxGeneration = 2000
        self.population = []
        self.target_y = 17.5398258887737
        self.x = 5

    def initPopulation(self):
        self.population = [Solution() for _ in range(self.populationSize)]

    def calculateFitness(self):
        for sol in self.population:
            res = sol.genotype[0] * math.sin(self.x ** 0)
            res += sol.genotype[1] * math.sin(self.x ** 1)
            res += sol.genotype[2] * math.cos(self.x ** 2)
            res -= sol.genotype[3] * math.sin(self.x ** 3)
            res -= sol.genotype[4] * math.cos(self.x ** 4)
            sol.fitness = res
            sol.difference = abs(self.target_y - res)

    def selectParents(self):
        tournament_size = 5
        parents = random.sample(self.population, tournament_size)
        parents.sort(key=lambda sol: sol.difference)
        return parents[0], parents[1]

    def crossOver(self, s1, s2):
        newSol = Solution()
        crossover_point = random.randint(1, 4)
        newSol.genotype[:crossover_point] = s1.genotype[:crossover_point]
        newSol.genotype[crossover_point:] = s2.genotype[crossover_point:]
        return newSol

    def mutate(self, s):
        mutation_chance = 0.1
        for i in range(5):
            if random.random() < mutation_chance:
                s.genotype[i] = random.randint(0, 9)

    def updatePopulation(self):
        self.population.sort(key=lambda sol: sol.difference)
        new_population = self.population[:self.populationSize // 2]

        while len(new_population) < self.populationSize:
            parent1, parent2 = self.selectParents()
            child = self.crossOver(parent1, parent2)
            self.mutate(child)
            new_population.append(child)
        self.population = new_population

    def run(self):
        self.initPopulation()
        for generation in range(self.maxGeneration):
            self.calculateFitness()
            best_solution = min(self.population, key=lambda sol: sol.difference)
            if best_solution.difference == 0:
                break
            self.updatePopulation()
        self.calculateFitness()
        best_solution = min(self.population, key=lambda sol: sol.difference)
        return best_solution


if __name__ == "__main__":
    ga = GA()
    sol = ga.run()
    print(f"Best solution is: {sol.genotype} -> {sol.fitness}, difference: {sol.difference}")
