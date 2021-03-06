from viroconcom.params import ConstantParam, FunctionParam
from viroconcom.distributions import WeibullDistribution, LognormalDistribution, MultivariateDistribution
from viroconcom.contours import DirectSamplingContour
import matplotlib.pyplot as plt

# Define a Weibull distribution representing significant wave height.
shape = ConstantParam(1.471)
loc = ConstantParam(0.8888)
scale = ConstantParam(2.776)
dist0 = WeibullDistribution(shape, loc, scale)
dep0 = (None, None, None)  # All three parameters are independent.

# Define a Lognormal distribution representing spectral peak period.
my_sigma = FunctionParam("exp3", 0.0400, 0.1748, -0.2243)
my_mu = FunctionParam("power3", 0.1, 1.489, 0.1901)
dist1 = LognormalDistribution(sigma=my_sigma, mu=my_mu)
dep1 = (0, None, 0)  # Parameter one and three depend on dist0.

# Create a multivariate distribution by bundling the two distributions.
distributions = [dist0, dist1]
dependencies = [dep0, dep1]
mul_dist = MultivariateDistribution(distributions, dependencies)

# Draw sample from multivariate distribution with given number and
# compute a direct sampling contour.
# Number of points 1000000, return period of 25 year, state duration of 6 hours, step of 6 degrees.
dsc = DirectSamplingContour(mul_dist, 1000000, 25, 6, 6)
direct_sampling_contour = dsc.direct_sampling_contour()

# Plot the contour and the sample.
plt.scatter(dsc.data[1], dsc.data[0], marker='.')
plt.plot(direct_sampling_contour[1], direct_sampling_contour[0], color='red')
plt.title('Direct sampling contour')
plt.ylabel('Significant wave height (m)')
plt.xlabel('Zero-upcrossing period (s)')
plt.grid(True)
plt.show()
