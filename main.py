import matplotlib.pyplot as plt
import math

fig = plt.figure(figsize=(8,8))
fig.patch.set_facecolor((0, 0, 0))
ax = plt.axes()
ax.set_facecolor((0, 0, 0))
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.yaxis.label.set_color('white')
ax.xaxis.label.set_color('white')
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
#plt.grid(color='grey', linestyle='-', linewidth=0.5, which='both')

def get_gradient(x, y):
    return ((x**2) + (y**2) - 1)

size = 5

for i in range (-size, size+1, 1):
    for j in range(-size, size+1, 1):
        xx = i*0.5
        yy = j*0.5
        m = get_gradient(xx, yy)
        length = 0.125
        a = (m*(length**0.5)) / (((m**2)+1)**0.5)
        b = (length**0.5) / (((m**2)+1)**0.5)
        plt.plot([xx-(0.5*b), xx+(0.5*b)], [yy-(0.5*a), yy+(0.5*a)])

plt.show()
