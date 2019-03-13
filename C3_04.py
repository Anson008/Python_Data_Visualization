# Defining axis lengths and limits


from pylab import *
import numpy as np

# generate uniformly distributed 256 points from -pi to pi, inclusive
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)

y = np.cos(x)
y1 = np.sin(x)

plot(x, y)
plot(x, y1)

# define plot title
title("Functions $\sin$ and $\cos$")

# set x limit
xlim(-3.0, 3.0)
# set y limit
ylim(-1.0, 1.0)

# format ticks at specific values
xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
        [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi/2$'])
yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])

show()
