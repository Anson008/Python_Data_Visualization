# Defining plot line styles, properties, and format strings


from pylab import *

# get current axis
ax = gca()

# set view to tight, and maimum number of tick intervals to 10
ax.locator_params(tight=True, nbins = 10)

# generate 100 normal distribution values
ax.plot(np.random.normal(10, 0.1, 100))

show()
