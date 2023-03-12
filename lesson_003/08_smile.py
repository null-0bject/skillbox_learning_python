# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random as rd
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код


def smiley_face(x, y, color=sd.COLOR_YELLOW):
    smiley_center = sd.get_point(x, y)
    sd.circle(smiley_center, color=color)
    left_eye = sd.get_point(x-20, y+20)
    right_eye = sd.get_point(x+20, y+20)
    sd.circle(left_eye, color=color, radius=10)
    sd.circle(right_eye, color=color, radius=10)
    points_list = [sd.get_point(x-20, y), sd.get_point(x-10, y-15), sd.get_point(x+10, y-15),
                    sd.get_point(x+20, y)]
    sd.lines(point_list=points_list, width=1)


for _ in range(10):
    x = rd.randint(0, 600)
    y = rd.randint(0, 550)
    smiley_face(x, y)
sd.pause()
