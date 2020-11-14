products = []
while True:
	name = input('Please enter the product:')
	if name == 'q': #q = quit
	    break
	price = input('Pleas enter the price of the product:')
	p = [name, price]
	products.append(p)
print(products)

#products[0][0] # 第一個0是大清單的第0格，第二個0是小清單的第0格

for product in products:
	print('The price of', product[0], 'is', product[1])