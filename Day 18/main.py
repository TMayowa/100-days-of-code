# import colorgram
#
# colors = colorgram.extract('start_image.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
import turtle as t
import random

color_list = [(198, 163, 116), (131, 79, 51), (224, 211, 115), (239, 243, 246),
              (246, 249, 246), (82, 39, 28), (116, 40, 30), (170, 153, 27), (55, 86, 122), (71, 114, 78),
              (123, 156, 177), (176, 103, 97), (129, 148, 137), (44, 52, 63), (39, 34, 41), (49, 53, 52),
              (221, 180, 182), (217, 182, 177), (76, 72, 47), (185, 149, 151), (187, 208, 171), (115, 138, 122),
              (103, 78, 80), (96, 124, 161), (175, 191, 212), (90, 48, 49), (165, 109, 110), (58, 62, 71)]

tim = t.Turtle()

t.colormode(255)


def dot_art():
    tim.penup()
    x = -200
    y = -200
    for i in range(10):
        tim.goto(x, y)
        for j in range(10):
            rand_color = random.choice(color_list)
            tim.dot(10, rand_color)
            tim.forward(40)
        y += 40


dot_art()

t.Screen()
t.Screen().exitonclick()
