products = []
while True:
	name = input('Please enter the products: ')
	if name == 'q': # quit
		break
	price = input('Please enter the price: $')
	products.append([name, price])
	
print(products)

for p in products:
	print('The price of', p[0], 'is $', p[1])