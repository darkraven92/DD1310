import math

def find_cubes(n):
    solutions = []
    for a in range(1, math.floor(n**(1/3))+1):
        for b in range(a, math.floor(n**(1/3))+1):
            if a**3 + b**3 == n:
                solutions.append((a,b))
                if len(solutions) == 2:
                    return solutions
    return solutions

n = int(input("Ange ett positivt heltal: "))
solutions = find_cubes(n)

if len(solutions) == 0:
    print(f"Det finns inga lösningar till a³ + b³ = {n}")
elif len(solutions) == 1:
    print(f"Det finns en lösning till a³ + b³ = {n}: {solutions[0]}")
else:
    print(f"Det finns två lösningar till a³ + b³ = {n}: {solutions[0]} och {solutions[1]}")
