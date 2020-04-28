products = []
while True:
	name = input('Please enter the products: ')
	if name == 'q': # quit
		break
	price = input('Please enter the price: $')
	products.append([name, price])
	
print(products[0][1])

products[0][0]