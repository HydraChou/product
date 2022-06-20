products = []

while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入價格: ')
    p = []    #小清單 = p = [name, price]
    p.append(name)  
    p. append(price)
    products. append(p)  #商品清單轉為二維清單，清單中還有清單 or products. append([name, price])

print(products)

products[0][0]  #第一個是大清單中的第0格，第二個是小清單中的第0格

for p in products:
    print(p[0], '的價格是', p[1])