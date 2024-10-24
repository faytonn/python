import math

A = int(input())
B = int(input())

discriminant = A**2 - 4 * B

if discriminant < 0:
    print("No solution")
else:
    sqrtDiscriminant = math.sqrt(discriminant)
    foundSolution = False
    for x in ((A + sqrtDiscriminant) / 2, (A - sqrtDiscriminant) / 2):
        if x.is_integer():
            x=int(x)
            y = A - x
            if x * y == B:
                if not foundSolution or x != y:
                    print(f"X = {x}, Y = {y}")
                    foundSolution = True
    if not foundSolution:
        print("No solution")
   
