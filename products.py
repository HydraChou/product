# 讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
    for line in f:
        if '商品,價格' in line:
            continue   # 類似break，只能用在回圈裡，continue是跳過下面從頭開始，用來跳過欄位名稱
        name, price = line.strip().split(',')  #strip去掉東西，split用甚麼東西當切割的標準，遇到逗點就切一刀
        products.append([name, price])

# 讓使用者輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入價格: ')
    price = int(price)
    p = []    #小清單 = p = [name, price]
    p.append(name)  
    p. append(price)
    products. append(p)  #商品清單轉為二維清單，清單中還有清單 or products. append([name, price])

print(products)

products[0][0]  #第一個是大清單中的第0格，第二個是小清單中的第0格

# 印出所有購買紀錄
for p in products:
    print(p[0], '的價格是', p[1])

# 把資料儲存到電腦功能，寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:  # products.txt檔案會被產生出來，csv檔可以用excel打開，with是自動關閉的意思
    f.write('商品,價格\n')
    for p in products:
        f.write(str(p[0]) + ','+ str(p[1]) + '\n')   #字串合併，最後一個是分行符號
            # f.write是真正寫入功能，用逗點區隔不同屬性

# 字串有加減功能，'abc' + '123' = 'abc123'

