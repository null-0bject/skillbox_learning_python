# -*- coding: utf-8 -*-

import simple_draw as sd
import random as rd
sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# здесь ваш код
# point = sd.get_point(100, 100)
# radius = 30
# for _ in range(3):
#     radius += 5
#     sd.circle(point, radius=radius)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг


def bubble(x, y, step, amount, colors: tuple = (255, 255, 255)):
    """
    Принимает параметры точки, шаг увеличивающегося пузырька и количество пузырьков
    :param colors: 
    :param x:  - координата Х точки
    :param y:  - координата У точки
    :param step: - Шаг
    :param amount: - количество
    """
    radius = 50
    dot = sd.get_point(x, y)
    for _ in range(amount):
        radius += step
        sd.circle(center_position=dot, radius=radius, width=5, color=colors)


# bubble(300, 150, 10, 10)
# print(bubble.__doc__)
# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
for x in range(100, 1100, 100):
    bubble(x, 300, step=5, amount=1)
# Нарисовать три ряда по 10 пузырьков
for y in range(100, 400, 100):
    for x in range(100, 1100, 100):
        bubble(x, y, step=5, amount=1)
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    x = rd.randint(0, 1000)
    y = rd.randint(0, 1000)
    color = (rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))
    bubble(x, y, colors=color, amount=1, step=5)
sd.pause()


