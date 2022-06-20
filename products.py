products = []

while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入價格: ')
    p = []    #小清單
    p.append(name)  
    p. append(price)
    products. append(p)  #商品清單轉為二維清單，清單中還有清單

print(products)