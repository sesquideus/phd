#!/usr/bin/env python
import random
import numpy as np


# mean 1 + 1/x
def generate_uniform(p, size):
    w = np.random.uniform(size=size)
    return np.where(w < p, 0, 1)

def generate_geometric(p, size):
    return np.random.geometric(p=p, size=size) - 1


def generate_mers(p, size):
    w = np.random.uniform(size=size)
    return np.where(w < p, 0, 10)



def simulate():
    population = 1000
    total = 0
    den = 0

    while population > 0 and population < 1000000:
        new_sick = generate_mers(p=0.9, size=population)

        den += population
        population = sum(new_sick)
        total += population

    return total, den

def main():
    n = 1000
    total = 0
    r_0 = 0

    for x in range(0, n):
        sick, den = simulate()
        x = sick / den

        r_0 += x
        total += sick


    print(f"Total {total / n} sick, r_0 = {r_0 / n}")


main()
