import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# malla
xs = np.linspace(0,1,101)
ys = np.linspace(0,1,101)
X, Y = np.meshgrid(xs, ys)
F = (2/5)*(2*X + 3*Y)   # f(x,y)

# 1) Superficie 3D
fig = plt.figure(figsize=(10,4))
ax = fig.add_subplot(1,2,1, projection='3d')
ax.plot_surface(X, Y, F, edgecolor='k', linewidth=0.1, alpha=0.9)
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('f(x,y)')
ax.set_title('Superficie f(x,y)')

# 2) Contorno y region R sombreada
ax2 = fig.add_subplot(1,2,2)
cs = ax2.contour(X, Y, F, levels=10)
ax2.clabel(cs, fontsize=8)
ax2.set_xlim(0,1); ax2.set_ylim(0,1)
ax2.set_xlabel('x'); ax2.set_ylabel('y')
ax2.set_title('Contornos de f y región R')

# sombrear R: 1/4 < y < 1/2, 0 < x < y/2
YY, XX = np.meshgrid(np.linspace(0,1,200), np.linspace(0,1,200))
mask = (YY>0.25) & (YY<0.5) & (XX < YY/2)
ax2.scatter(XX[mask], YY[mask], s=1, color='orange', alpha=0.7)
plt.tight_layout()
plt.show()
