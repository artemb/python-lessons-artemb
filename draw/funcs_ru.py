# Настраиваем поле для рисования.
from draw.drawlib import set_up, new_shape
s = set_up(bgcolor='black', axis=False)

# Будем рисовать прямоугольник
# Задаем параметры - начальная координата, цвет и размеры
start_x = 0
start_y = 0
color = 'yellow'
size_x = 50
size_y = 100

# Начинаем рисование
turtle = new_shape(start_x, start_y, color, speed='fast')
# Начинаем закрашивание
turtle.begin_fill()

for x in range(2):
    turtle.forward(size_x)
    turtle.left(90)
    turtle.forward(size_y)
    turtle.left(90)

# Закрашиваем нарисованную фигуру
turtle.end_fill()
# Прячем саму черепашку, чтобы не мешала любоваться фигурой
turtle.hideturtle()

# Не завершаем программу, зависаем на следующей строке, пока пользователь не закроет окно
s.mainloop()

# Задача 1. Отлично, у нас есть алгоритм, который рисует прямоугольник по заданным параметрам.
#           Попробуйте поменять параметры и нарисовать прямоугольники разных размеров, цветов и в разных местах.
#
# Задача 2. А теперь нарисуйте 2 разных прямоугольника вместе.
#
# Задача 3. Напишите функцию, которая рисует прямоугольник по заданным параметрам.
#           Используя написанную функцию, нарисуйте 4 разных прямоугольника вместе.
#
# Задача 4. Напишите функции для рисования треугольников и кругов.
#
# Задача 5.
