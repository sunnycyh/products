import os # operating system

def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if 'Product,Price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# enter notes by user
def user_input(products):
	while True:
		name = input('Please enter the products: ')
		if name == 'q': # quit
			break
		price = input('Please enter the price: $')
		products.append([name, price])
	print(products)
	return products

# print all records
def print_products(products):
	for p in products:
		print('The price of', p[0], 'is $', p[1])

# write file
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('Product,Price\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main(): # command all = main function
	filename = 'products.csv'
	if os.path.isfile(filename): # 相對路徑 # os is a module, path is another module
		print('Yeah! We found it!')
		products = read_file(filename)
	else:
		print('We cannot find it......')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main() # after refactor 