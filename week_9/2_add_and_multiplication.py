# Добавьте в предыдущий класс следующие методы:
#
#  __add__, принимающий вторую матрицу того же размера и возвращающий сумму матриц.
#  __mul__, принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр.
#  __rmul__, делающий то же самое, что и __mul__. Этот метод будет вызван в том случае, аргумент находится справа.
#  Для реализации этого метода в коде класса достаточно написать __rmul__ = __mul__.
# Иллюстрация:
#
#  В следующем случае вызовется
#  __mul__: Matrix([[0, 1], [1, 0]) * 10.
#  В следующем случае вызовется
#  __rmul__ (так как у int не определен __mul__ для матрицы справа): 10 * Matrix([[0, 1], [1, 0]).
# Разумеется, данные методы не должны менять содержимое матрицы.

from sys import stdin


class Matrix:

    def __init__(self, m):
        self.input_list = [line.copy() for line in m]

    def __str__(self):
        st = ''
        for i in range(len(self.input_list)):
            for j in range(len(self.input_list[i])):
                if j != len(self.input_list[i]) - 1:
                    st += str(self.input_list[i][j]) + '\t'
                else:
                    st += str(self.input_list[i][j])
            if i != len(self.input_list) - 1:
                st += '\n'
        return st

    def __add__(self, other):
        for i in range(len(self.input_list)):
            for j in range(len(self.input_list[i])):
                other.input_list[i][j] += self.input_list[i][j]
        return Matrix(other.input_list)

    def __mul__(self, other):
        for i in range(len(self.input_list)):
            for j in range(len(self.input_list[i])):
                other.input_list[i][j] *= self.input_list[i][j]
        return Matrix(other.input_list)

    __rmul__ = __mul__

    def size(self):
        return len(self.input_list), len(self.input_list[0])


exec(stdin.read())
