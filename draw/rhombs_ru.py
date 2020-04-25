# Настраиваем поле для рисования. Можете выбрать свои цвета
from draw.drawlib import set_up, new_shape, next_color
s = set_up(bgcolor='black', axis=False)
turtle = new_shape(0, 0, 'white', speed='fast')


# Начинаем закрашивать фигуру
turtle.begin_fill()

# Если хотите поменять цвет - используйте метод turtle.color
turtle.color('red')

# Рисуем ромб
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(135)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(135)

# Заканчиваем закраску
turtle.end_fill()

# Не завершаем программу, зависаем на следующей строке, пока пользователь не закроет окно
s.mainloop()

# Задача 1. Используя цикл for x in range(N) уберите повторения
#
# Задача 2. Используя вложенные циклы for x in range(N) нарисуйте цветок как в примере rhombs.png
#
# Задача 3. Используя функцию next_color(), закрасьте каждый ромб в свой цвет
#
# Задача 4. Придумайте и нарисуйте свой вариант фигуры, используя циклы, цвета и закарску
