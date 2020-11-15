import os #operating system

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f: #一個line是一個字串
			if 'product,price' in line:
				continue #一定要在迴圈裡，功能是跳到下一回
			name, price = line.strip().split(',') #意思是先將換行的\n去除掉，再用','當作分割的標準
			products.append([name, price])
	return products

#讓使用者輸入
def user_input(products):
	while True:
		name = input('Please enter the product:')
		if name == 'q': #q = quit
			break
		price = input('Pleas enter the price of the product:')
		price = int(price)
		p = [name, price]
		products.append(p)
	print(products)
	return products

#products[0][0] # 第一個0是大清單的第0格，第二個0是小清單的第0格

#印出所有購買紀錄
def print_products(products):
	for p in products:
		print('The price of', p[0], 'is', p[1])

#寫入檔案
def write_file(filename,products):
	with open (filename, 'w', encoding='utf-8') as f: 
		f.write('product,price\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n') #真正寫入 #因為先前把p[1]轉為數字，現在因為加號關係需要轉換成字串

def main(): #主要執行的程式碼函式
	filename = 'products.csv'
	if os.path.isfile(filename): #只給檔名是相對路徑，若是整個地址為絕對路徑 #path為模組、路徑
		print('File Found.')
		products = read_file(filename)
	else:
		print('File is not Found.')


	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main() #執行程式