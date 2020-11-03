prices = [170.12, 93.29, 55.28, 145.3, 171.81, 59.5, 100.5]
earnings = [9.2, 5.31, 2.41, 5.91, 15.42, 2.51, 6.79]

prices_array = np.array(prices)
nd_array = np.array([prices, earnings])
transposed = np.transpose(nd_array)

# methods()
transposed.shape
transposed.size