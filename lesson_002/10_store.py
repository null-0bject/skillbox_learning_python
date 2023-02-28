#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

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

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

lamps_count = store[goods['Лампа']][0]['quantity']
lamps_cost = lamps_count * store[goods['Лампа']][0]['price']

table_count = store[goods['Стол']][0]['quantity'] + store[goods['Стол']][1]['quantity']

table_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price'] \
            + store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']


sofa_count = store[goods['Диван']][0]['quantity'] + store[goods['Диван']][1]['quantity']

sofa_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price'] \
            + store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']


chair_count = store[goods['Стул']][0]['quantity'] + store[goods['Стул']][1]['quantity'] \
              + store[goods['Стул']][2]['quantity']

chair_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price'] \
            + store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price'] \
            + store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']


if __name__ == '__main__':
    print(f'Ламп - {lamps_count} шт, стоимость {lamps_cost} руб\n'
          f'Столов - {table_count} шт, стоимость {table_cost} руб\n'
          f'Диванов - {sofa_count} шт, стоимость {sofa_cost} руб\n'
          f'Стульев - {chair_count} шт, стоимость {chair_cost} руб')
