# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
brick_x = 100
brick_y = 50


def brick(x,y):
    start_point = sd.get_point(x, y)
    end_point = sd.get_point(x + 100, y + 50)
    sd.rectangle(start_point, end_point, width=1, color=sd.random_color())


def brick_row_even():
    y = 500
    for __ in range(6):
        x = -50
        for _ in range(7):
            brick(x, y)
            x += 100
        y -= 100


def brick_row_odd():
    y = 550
    for __ in range(6):
        x = 0
        for _ in range(6):
            brick(x, y)
            x += 100
        y -= 100


def brick_wall():
    brick_row_odd()
    brick_row_even()

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код


if __name__ == '__main__':
    brick_wall()
sd.pause()
