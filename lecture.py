import sys
import math
from points import *

#algorithm 1
#region
points = []
for line in sys.stdin:
    w1, w2 = line.split()
    points.append(float(w1), float(w2))

minimumDistance = math.inf

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]
        d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if d < minimumDistance:
            minimumDistance = d

print(minimumDistance)
#endregion

#more efficient algorithm
#region





#endregion