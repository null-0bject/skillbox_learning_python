# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd


rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код


def rainbow_circle(x=300, y=-100, width=10, step=12):
    radius = 500
    dot = sd.get_point(x, y)
    for _ in range(6, -1, -1):
        radius += step
        sd.circle(dot, radius=radius, color=rainbow_colors[_-7], width=width)


def rainbow():
    x_start = 50
    x_end = 350
    start_point = sd.get_point(x_start, 50)
    end_point = sd.get_point(x_end, 450)
    sd.line(start_point=start_point, end_point=end_point, color=rainbow_colors[0], width=4)
    for _ in range(1, 7):
        x_start += 5
        x_end += 5
        start_point = sd.get_point(x_start, 50)
        end_point = sd.get_point(x_end, 450)
        sd.line(start_point=start_point, end_point=end_point, color=rainbow_colors[_], width=4)
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код


if __name__ == '__main__':
    rainbow_circle()
    # rainbow()

sd.pause()
