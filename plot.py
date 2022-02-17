
from matplotlib import pyplot as plt
R=1
D =16
plt.plot(R,D)
path= 1
for i in range(D, (R + D - 1)):
    path *= i;
    path //= (i - D + 1);

plt.show()
