# .fv(rate, nper, pmt, pv)  rate: rate of return, nper: lifespan,
#  pmt: payment beginning or end of each period, pv: present value of investment
import numpy as np

# Calculate investment_1
investment_1 = np.fv(rate=0.05, nper=15, pmt=0, pv=-10000)
print("Investment 1 will yield a total of $" + str(round(investment_1, 2)) + " in 15 years")

# Calculate investment_2
investment_2 = np.fv(rate=0.08, nper=15, pmt=0, pv=-10000)
print("Investment 2 will yield a total of $" + str(round(investment_2, 2)) + " in 15 years")