import matplotlib.pyplot as plt

plt.plot(days, prices, color="red", linestyle="--")
# plt.[xlabel, ylabel, tittle]
plt.scatter(days, prices, color="green", s=0.1)

plt.hist(x=prices, bins=6, normed=1, alpha=0.5, label="Prices 1") # normalize means the porcentage of the data not the count
plt.hist(x=prices_new, bins=6, normed=1, alpha=0.5, label="Prices New")
