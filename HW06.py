import os, psutil, timeit
from random import randint as randint

def matrix_generator(dim: int, x: int, y=1, z=1, start_ind=0, end_ind=100) -> list:
    """вспомогательная фунция для генерации массива случайных целых чисел с размерностью dim ().
        количество значений в каждой размерости задается параметрами x, y, z.
        Значения элементов ограничиваются диапазоном от start_ind до end_ind"""
    matr_x = []
    if dim == 1:
        for i in range(x):
            matr_x.append(randint(start_ind, end_ind))
    elif dim == 2:
        for i in range(x):
            matr_y = []
            for j in range(y):
                matr_y.append(randint(start_ind, end_ind))
            matr_x.append(matr_y)
    elif dim == 3:
        for i in range(x):
            matr_y = []
            for j in range(y):
                matr_z = []
                for k in range(z):
                    matr_z.append(randint(start_ind, end_ind))
                matr_y.append(matr_z)
            matr_x.append(matr_y)
    else:
        return []
    return matr_x

# сортировка - метод пузырька
def buble_sort() -> None:
    """занимаемая память - 24576 байт, время исполнения - 0.203182825 сек"""
    process = psutil.Process(os.getpid())
    start_mem_size = process.memory_info().rss
    global matrix_len
    matrix = matrix_generator(1, matrix_len, start_ind=-100, end_ind=100)
    sort_matrix = matrix[:]
    for i in range(matrix_len - 1):
        changed = False
        for j in range(1, matrix_len - i):
            if sort_matrix[j - 1] < sort_matrix[j]:
                sort_matrix[j - 1], sort_matrix[j] = sort_matrix[j], sort_matrix[j - 1]
                changed = True
        if not (changed):
            break
    print(process.memory_info().rss - start_mem_size)
    print(sort_matrix)

# сортировка - метод выбора
def select_sort() -> None:
    """занимаемая память - 24576 байт, время исполнения - 0.099984621 сек"""
    process = psutil.Process(os.getpid())
    start_mem_size = process.memory_info().rss
    global matrix_len
    matrix = matrix_generator(1, matrix_len, start_ind=-100, end_ind=100)
    sort_matrix = matrix[:]
    for i in range(matrix_len):
        for j in range(i + 1, matrix_len):
            if sort_matrix[j] > sort_matrix[i]:
                sort_matrix[j], sort_matrix[i] = sort_matrix[i], sort_matrix[j]
    print(process.memory_info().rss - start_mem_size)
    print(sort_matrix)

#сортировка - измененный алгоритм выбора - в каждой итерации перекладываем макс. эл-т из одного массива в другой
def enh_select_sort() -> None:
    """занимаемая память - 126976 байт, время исполнения - 0.031208523 сек"""
    process = psutil.Process(os.getpid())
    start_mem_size = process.memory_info().rss
    global matrix_len
    matrix = matrix_generator(1, matrix_len, start_ind=-100, end_ind=100)
    sort_matrix = matrix[:]
    sort_matrix_1 = []
    for i in range(matrix_len):
        sort_matrix_1.append(sort_matrix.pop(sort_matrix.index(max(sort_matrix))))
    print(process.memory_info().rss - start_mem_size)
    print(sort_matrix)

matrix_len = 1500
statement = "select_sort"
setup = f"from __main__ import {statement}"
print(timeit.timeit(f"{statement}()", setup=setup, number=1))

