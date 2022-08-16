import numpy as np

N, m = int(input()), int(input())

a = np.random.uniform(-1, 1, (N, m))
np.savetxt('vectors.csv', a, delimiter=',')
