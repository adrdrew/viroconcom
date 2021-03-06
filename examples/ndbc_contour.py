from matplotlib import pyplot as plt
from viroconcom.fitting import Fit
from viroconcom.contours import IFormContour
import viroconcom.dataNDBC as ndbc


# Example for one year.
buoy = 41108
date = "2017-02-11/to/2018-11-27"

H = ndbc.NDBC(buoy)
df = H.get_data(date)
sample_1 = df.WVHT
sample_2 = df.APD

dist_description_0 = {'name': 'Weibull',
                      'dependency': (None, None, None),
                      'width_of_intervals': 2}
dist_description_1 = {'name': 'Lognormal',
                      'dependency': (0, None, 0),
                      'functions': ('exp3', None, 'power3')}

my_fit = Fit((sample_1, sample_2),
             (dist_description_0, dist_description_1))

# Compute a contour based on the fit and plot it together with the sample.
iform_contour = IFormContour(my_fit.mul_var_dist, 25, 0.5, 100)
plt.scatter(sample_1, sample_2, label='sample')
plt.plot(iform_contour.coordinates[0][0], iform_contour.coordinates[0][1],
            '-k', label='IFORM contour')
plt.xlabel('Significant wave height (m)')
plt.ylabel('Average wave period (s)')
plt.legend()
plt.show()


