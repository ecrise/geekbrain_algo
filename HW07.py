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


def buble_sort_prg() -> int:
    """1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
    промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в
    виде функции. По возможности доработайте алгоритм (сделайте его умнее)."""

    # метод выбора пузырька
    def buble_sort(matrix: list) -> list:
        sort_matrix = matrix[:]
        for i in range(matrix_len - 1):
            changed = False
            for j in range(1, matrix_len - i):
                if sort_matrix[j - 1] < sort_matrix[j]:
                    sort_matrix[j - 1], sort_matrix[j] = sort_matrix[j], sort_matrix[j - 1]
                    changed = True
            if not(changed):
                break
        return sort_matrix

    matrix_len = 30
    test_matrix = matrix_generator(1, matrix_len, start_ind=-100, end_ind=100)
    print("Initial matrix is:\n", test_matrix, "\n")
    print("Sorted matrix is:\n", buble_sort(test_matrix))
    return 0


def merge_sort_prg() -> int:
    """2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
    промежутке [0; 50). Выведите на экран исходный и отсортированный массивы."""
    def merge_sort(matrix: list) -> list:
        matr_len = len(matrix)
        if matr_len == 1:
            return matrix
        elif matr_len == 2:
            if matrix[0] < matrix[1]:
                matrix[0], matrix[1] = matrix[1], matrix[0]
            return matrix
        else:
            first_matrix = []
            second_matrix = []
            half_len = len(matrix) // 2
            for i in range(half_len):
                first_matrix.append(matrix[i])
                second_matrix.append(matrix[i + half_len])
            if len(matrix) % 2 == 1:
                second_matrix.append(matrix[-1])
            first_matrix = merge_sort(first_matrix)
            second_matrix = merge_sort(second_matrix)
            result_matrix = []
            while len(first_matrix) > 0 and len(second_matrix) > 0:
                if first_matrix[0] < second_matrix[0]:
                    result_matrix.append(second_matrix.pop(0))
                else:
                    result_matrix.append(first_matrix.pop(0))
            while len(second_matrix) > 0:
                result_matrix.append(second_matrix.pop(0))
            while len(first_matrix) > 0:
                result_matrix.append(first_matrix.pop(0))
            return result_matrix

    matrix_len = 31
    #test_matrix = [11, 44, 22, 49, 35]
    test_matrix = matrix_generator(1, matrix_len, end_ind=50)
    print("Initial matrix is: \n", test_matrix, "\n")
    print("Sorted matrix is: \n", merge_sort(test_matrix))
    return 0



def matrix_medium() -> int:
    """3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
    Медианой     называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
    медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком
    сложно, то используйте метод сортировки, который не рассматривался на уроках"""
    matrix_len = 10
    # test_matrix = [0, 10, 1, 2, 7, 5, 6, 0, 0, 4, 3, 7, 4, 6, 5, 6, 3, 8, 6, 3, 3]
    test_matrix = matrix_generator(1, 2 * matrix_len + 1, end_ind=10)
    print(test_matrix)
    for base_element in test_matrix:
        lower_count = 0
        greater_count = 0
        equal_count = 0
        for element in test_matrix:
            if element < base_element:
                lower_count += 1
            elif element > base_element:
                greater_count += 1
            else:
                equal_count += 1
        if (equal_count == 1) and (lower_count == greater_count):
            print(f"The medium of the matrix is {base_element}")
            break
        elif (equal_count != 1) and (min(lower_count, greater_count) + equal_count - 1) // matrix_len == 1:
            print(f"The medium of the matrix is {base_element}\n")
            break
    print("For proving program!!!")
    print(sorted(test_matrix))
    print(list(sorted(test_matrix))[matrix_len])
    return 0


menu = {"Task 1 - Buble sorting": buble_sort_prg,
        "Task 2 - Merge sorting": merge_sort_prg,
        "Task 3 - Matrix medium": matrix_medium,
        "Exit": exit
        }

while True:
    for i, m in enumerate(menu, start=1):
        print(f"{i}. {m}")
    command = int(input("Enter a command: "))
    if 1 <= command <= len(menu):
        key = list(menu.keys())[command - 1]
        print("______________________________")
        menu[key]()
        print("______________________________")
    else:
        print("You enter wrong command!")
