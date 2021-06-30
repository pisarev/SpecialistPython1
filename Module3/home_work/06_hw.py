# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
brand_list = [];
for item in items:
    for key, value in item.items():
        if key == "brand": brand_list.append(value)
print("Товары на складе представлены брэндами:", brand_list)

brand_info = {
    "brand": [],
    "count": []
}

def find_brand(brand_name):
    for i, item in enumerate(brand_info["brand"]):
        if item == brand_name:
            return i
    return -1
    
for item in items:
    i = find_brand(item["brand"])
    if i == -1:
        brand_info["brand"].append(item["brand"])
        brand_info["count"].append(1)
    else:
        brand_info["count"][i] += 1
        
brand_index = -1
brand_count = 0
for i, count in enumerate(brand_info["count"]):
    if brand_index < 0 or brand_count < count:
        brand_index = i
        brand_count = count

#print(brand_info)

if brand_index != -1:
    print("На складе больше всего товаров брэнда(ов):", brand_info["brand"][brand_index])
            
item_index = -1
item_price = 0

for i, item in enumerate(items):
    price = items[i]["price"]
    if item_index < 0 or item_price < price:
        item_index = i
        item_price = price
if item_index != -1:
    print("На складе самый дорогой товар брэнда(ов):", items[item_index]["brand"])
