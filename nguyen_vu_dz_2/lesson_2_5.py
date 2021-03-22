prices_list = [57.8, 46.51, 97, 11.11, 12.12, 13.13, 19.19, 15.15, 17.17, 16.16, 10.10]

for price in prices_list:
    price_str = str(price)
    price_list = []
    if isinstance(price, float):
        price_list = price_str.split('.')
    else:
        price_list = price_str.split('.')
        price_list.append("00")
    price_list[0] = int(price_list[0])
    price_list[1] = int(price_list[1])

    print(f"{price_list[0]:02d} руб. {price_list[1]:02d} коп.")

print("Ответ на пункт 4.B:")
print(prices_list, id(prices_list))
prices_list.sort(reverse=True)
print(prices_list, id(prices_list))

prices_list_s = sorted(prices_list, reverse=True)
print("Ответ на пункт 4.С:", prices_list_s, id(prices_list_s))

print("Ответ на пункт 4.D:")
max_price_number = 5
for n in range(0, max_price_number):
    print(prices_list_s[n])
