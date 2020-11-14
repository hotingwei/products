products = []
while True:
	name = input('Please enter the product:')
	if name == 'q': #q = quit
	    break
	price = input('Pleas enter the price of the product:')
	price = int(price)
	p = [name, price]
	products.append(p)
print(products)

#products[0][0] # 第一個0是大清單的第0格，第二個0是小清單的第0格

for p in products:
	print('The price of', p[0], 'is', p[1])

with open ('products.csv', 'w', encoding='utf-8') as f: 
	f.write('product,price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #真正寫入 #因為先前把p[1]轉為數字，現在因為加號關係需要轉換成字串
