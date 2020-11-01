companies = ['Apple', 'Coca-Cola', 'Tesla']
prices = [159.49, 57.23, 34.40]

# Indexing
print(companies[0])
print(companies[-1])

# Slicing
print(prices[1:])

nested_list = [companies, prices]
print(nested_list[1])
print(nested_list[0][0])

# Methods and Functions
companies.append('Amazon')
companies.extend(['Acer', 'Samsung'])
print(companies.index('Apple'))
print(max(prices))

