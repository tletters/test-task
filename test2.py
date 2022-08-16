import numpy as np
from math import dist
import matplotlib.pyplot as plt

data = np.loadtxt('vectors.csv', delimiter=',')

i, min1, min2, max1, max2 = 0, 0, 0, 0, 0
min_dist, max_dist = dist(data[0], data[1]), dist(data[0], data[1])
distance_list, graph_list = [], []

for now in data:
    i += 1
    for j in range(i, len(data)):
        new_dist = dist(now, data[j])
        distance_list.append(new_dist)
        graph_list.append(float(str(new_dist)[:3]))
        if new_dist < min_dist:
            min1 = i
            min2 = j
            min_dist = new_dist
        elif new_dist > max_dist:
            max1 = i
            max2 = j
            max_dist = new_dist

plt.hist(graph_list,  bins=int((max_dist - min_dist) * 20))

plt.xticks(list(set(graph_list)))
plt.show()

print(min1, min2, min_dist)
print(max1, max2, max_dist)
