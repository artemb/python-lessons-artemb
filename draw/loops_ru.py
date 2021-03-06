# Следующие 2 строчки создают экран с осями
from draw.drawlib import set_up, new_shape
screen = set_up(axis=True)

# Создаем черепашку в заданном месте заданного цвета
# Черепашка не выглядит как черепашка, она выглядит как стрелочка
turtle = new_shape(100, 100, 'blue')

# Двигаем черепашку, она оставляет за собой линию
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)

# Не завершаем программу, зависаем на следующей строке, пока пользователь не закроет окно
screen.mainloop()


# Задача 1. Черепашка уже рисует квадрат, но строки кода повторяются
#           Используя цикл for x in range(N) уберите повторения
#
# Задача 2. Вместо прямоугольник нарисуйте треугольник, пятиугольник, шестиугольник
#
# Задача 3. Рисование правильных многоугольников происходит одинаково,
#           меняются лишь некоторые параметры, в зависимости от количества углов
#           Введите переменную vex, задающую количество углов.
#           Исправьте алгоритм таким образом, чтобы меняя значение vex можно было бы
#           нарисовать многоугольник с любым количеством углов от 3х до 20
#
# Задача 4. Многоугольник с 20 вершинами уже очень похож на круг, не так ли?
#           Нарисуйте круг.
