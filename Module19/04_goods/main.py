goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


total_price_lamp = store["12345"][0].get("quantity") * store["12345"][0].get("price")
total_price_table = store["23456"][0].get("quantity") * store["23456"][0].get("price") + store["23456"][1].get("quantity") * store["23456"][1].get("price")
total_price_sofa = store["34567"][0].get("quantity") * store["34567"][0].get("price") + store["34567"][1].get("quantity") * store["34567"][1].get("price")
total_price_chair = store["45678"][0].get("quantity") * store["45678"][0].get("price") + store["45678"][1].get("quantity") * store["45678"][1].get("price") + store["45678"][2].get("quantity") * store["45678"][2].get("price")

amount_lamp = store["12345"][0].get("quantity")
amount_table = store["23456"][0].get("quantity") + store["23456"][1].get("quantity")
amount_sofa = store["34567"][0].get("quantity") + store["34567"][1].get("quantity")
amount_chair = store["45678"][0].get("quantity") + store["45678"][1].get("quantity") + store["45678"][2].get("quantity")



print("{} - {} шт, стоимость {} руб".format("Лампа", amount_lamp, total_price_lamp))
print("{} - {} шт, стоимость {} руб".format("Cтол", amount_table, total_price_table))
print("{} - {} шт, стоимость {} руб".format("Диван", amount_sofa, total_price_sofa))
print("{} - {} шт, стоимость {} руб".format("Cтул", amount_chair, total_price_chair))

# Я знаю, что сделано паршиво, скорее всего тут надо через функцию, да?
# Я просто всё пытался вспомнить, не получалось сделать, если не трудно можете показать, как правильно это решается?)

#через цикл конечно надо сделать. Тут же видны явные зависимости
for i_name in goods.keys():
    total_quantity = 0
    total_cost = 0
    for j_good in store[goods[i_name]]:
        total_quantity += j_good['quantity']
        total_cost += j_good['price'] * j_good['quantity']
    print('{} - {} шт, стоимость {} руб'.format(
        i_name, total_quantity, total_cost))
