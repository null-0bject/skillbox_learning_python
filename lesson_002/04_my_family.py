#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)


my_family = ['Sister', 'Brother', 'Nephew']


# список списков приблизителного роста членов вашей семьи


my_family_height = [
    ['Olga', 165],
    ['Andrew', 176],
    ['Eugene', 150]
]


# Выведите на консоль рост сестры в формате
#   Рост сестры - ХХ см


print(my_family_height[0][1])


# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см


sum_of_height = [my_family_height[0][1], my_family_height[1][1], my_family_height[2][1]]
print(sum(sum_of_height))
