# Drawing scatter plots with colored markers

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
y1 = np.random.randn(len(x))
y2 = 1.2 + np.exp(x)

ax1 = plt.subplot(121)
plt.scatter(x, y1, color='indigo', alpha=0.3, edgecolors='white', label='No correl')
plt.xlabel("No correlation")
plt.grid(True)
plt.legend()

ax2 = plt.subplot(122, sharex=ax1, sharey=ax1)
plt.scatter(x, y2, color='green', alpha=0.3, edgecolors='grey', label='Correl')
plt.xlabel("Correlation")
plt.grid(True)
plt.legend()

plt.show()
