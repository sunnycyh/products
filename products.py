import os # operating system

# read file or creat file
products = []
if os.path.isfile('products.csv'): # 相對路徑 # os is a module, path is another module
	print('Yeah! We found it!')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if 'Product,Price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)

else:
	print('We cannot find it......')

# enter notes by user
while True:
	name = input('Please enter the products: ')
	if name == 'q': # quit
		break
	price = input('Please enter the price: $')
	products.append([name, price])
print(products)

# print all records
for p in products:
	print('The price of', p[0], 'is $', p[1])

# write file
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('Product,Price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')