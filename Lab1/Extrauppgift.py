def find_cubic_sums(n):
    solutions = []
    for a in range(1, int(n**(1/3))+1):
        b_cubed = n - a**3
        if b_cubed < 1:
            break
        b = round(b_cubed**(1/3))
        if b**3 == b_cubed and b >= a:
            solutions.append((a, b))
    return solutions
