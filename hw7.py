shopping_bag = []

print("[구입]")
while True:
    item = input("상품명?:")
    if item == '':
        break
    shopping_bag.append(item)
    print(f'장바구니에 {item}가(이) 담겼습니다.\n')

print(f'\n>>>장바구니 보기: (shopping.bag)')
