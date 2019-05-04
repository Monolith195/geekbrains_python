# 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать
# скрипт, автоматизирующий его заполнение данными. Для этого: Создать функцию write_order_to_json(),
# в которую передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer),
# дата (date). Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных
# указать величину отступа в 4 пробельных символа; Проверить работу программы через вызов функции
# write_order_to_json() с передачей в нее значений каждого параметра.


import json
from datetime import datetime


def write_order_to_json(item, quantity, price, buyer, date):
    order_to_json = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }

    with open('orders.json', 'r') as orders:
        data = json.load(orders)

    data["orders"].append(order_to_json)

    with open('orders.json', 'w') as orders:
        json.dump(data, orders, indent=4, sort_keys=True)


write_order_to_json("Bread", 1, 55, "Test", datetime.now().isoformat())
write_order_to_json("Milk", 1, 70, "Test", datetime.now().isoformat())
