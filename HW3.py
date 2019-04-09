from random import randint as randint


def matrix_generator(dim:int, x:int, y=1, z=1, start_ind=0, end_ind=100)->list:
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
        return None
    return matr_x    
        

def int_division_rates()->int:
    """ 1. В диапазоне натуральных чисел от 2 до 1000000 определить,
        сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""
    dict_rates = {}
    for num in range(2, 1000001):
        for divider in range(2,10):
            if num % divider == 0:
                dict_rates.setdefault(divider, 0)
                dict_rates[divider] += 1
    for k, v in dict_rates.items():
        print(f"In numbers from 2 to 1000000 there are {v} numbers that can be divided by {k}")
        print(1000000 // k) #а можно было просто разделить)))
    return 0

def even_elemenst_ind()->int:
    """2. Во втором массиве сохранить индексы четных элементов первого массива.
    Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
    надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается
    с нуля), т.к. именно в этих позициях первого массива стоят четные числа."""
    test_matrix = matrix_generator(1, 20) #генерируем одномерный массив из 20 элементов
    print(test_matrix)
    even_ind_matrix = []
    elem_ind = 0
    for element in test_matrix:
        if element % 2 == 0:
            even_ind_matrix.append(elem_ind)
        elem_ind += 1
    print(even_ind_matrix)

def elements_exchange()->int:        
    """3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
    test_matrix = matrix_generator(1, 10) #генерируем одномерный массив из 20 элементов
    min_el_ind = 0
    max_el_ind = 0
    min_el = test_matrix[0]
    max_el = test_matrix[0]
    for i in range(len(test_matrix)):
        if test_matrix[i] < min_el:
            min_el = test_matrix[i]
            min_el_ind = i
        elif test_matrix[i] > max_el:
            max_el = test_matrix[i]
            max_el_ind = i
    print(test_matrix)
    print(f"now min elenent '{min_el}' is in position {min_el_ind}, and max elenent '{max_el}' is in position {max_el_ind}")
    test_matrix[max_el_ind], test_matrix[min_el_ind] = test_matrix[min_el_ind], test_matrix[max_el_ind]
    print(f"and now we change its in place")         
    print(test_matrix)
    return 0

def most_frequence_elem()->int:
    """4. Определить, какое число в массиве встречается чаще всего."""
    test_matrix = matrix_generator(1, 20000, end_ind = 25) #генерируем одномерный массив из 20000 элементов с макс значением 25
    dict_frequence = {}
    for num in test_matrix:
        dict_frequence.setdefault(num, 0)
        dict_frequence[num] += 1
    most_frequent_el = num
    for k, v in sorted(dict_frequence.items()):
        print(f"In random matrix with 10000 elements number {k} meets {v} times")
        if v > dict_frequence[most_frequent_el]:
            most_frequent_el = k
    print(f"Most frequent element is {most_frequent_el}")
    return 0    

def max_negativ_elem()->int:
    """5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве."""
    test_matrix = matrix_generator(1, 20, start_ind = -100) #генерируем одномерный массив из 20 элементов с значениями от -100 до 100
    for i in range(len(test_matrix)):
        if test_matrix[i] < 0:
            max_neg_el = test_matrix[i]
            break
    max_neg_el_ind = i
    for i in range(max_neg_el_ind, len(test_matrix)):
        if test_matrix[i] < 0 and test_matrix[i] > max_neg_el:
            max_neg_el = test_matrix[i]
            max_neg_el_ind = i
    print(test_matrix)
    print(f"Max negative element is {max_neg_el} in position {max_neg_el_ind}")
    return 0        

def min_max_sum()->int:
    """6. В одномерном массиве найти сумму элементов, находящихся между минимальным
и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать."""
    test_matrix = matrix_generator(1, 20) #генерируем одномерный массив из 20 элементов
    print(test_matrix)
    min_el_ind = 0
    max_el_ind = 0
    min_el = test_matrix[0]
    max_el = test_matrix[0]
    for i in range(1, len(test_matrix)):
        if test_matrix[i] < min_el:
            min_el = test_matrix[i]
            min_el_ind = i
        elif test_matrix[i] > max_el:
            max_el = test_matrix[i]
            max_el_ind = i
    if min_el_ind == max_el_ind:
        print("In text matrix all elements are equal")
    else:
        sum_el = 0
        direction = 1 if min_el_ind < max_el_ind else -1
        for i in range(min_el_ind + direction, max_el_ind, direction):
            sum_el += test_matrix[i]   
        print(f"The sumary between min element '{min_el}' and max element '{max_el}' is {sum_el}")
    return 0
        

def min_pair()->int:
    """7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться."""
    test_matrix = matrix_generator(1, 20) #генерируем одномерный массив из 20 элементов
    print(test_matrix)
    min_is_first = True #переменная нужна для контроля, что минимальный элемент не нулевой элемент
    first_min_el = test_matrix[0]
    second_min_el = test_matrix[0]
    for element in test_matrix:
        if element < first_min_el:
            second_min_el = first_min_el
            first_min_el = element         
            min_is_first = False
        else:
            if element < second_min_el:
                second_min_el = element
    if min_is_first: #если первый элемент оказался наименьшим, просто ищем второй мин. эл-т
        for i in range(1, len(test_matrix)):
            if test_matrix[i] < second_min_el:
                second_min_el = test_matrix[i]
    print(f"In test matrix two smallest elements are {first_min_el} and {second_min_el}")
    test_matrix = sorted(test_matrix) #или через сортировку
    print(list(test_matrix[i] for i in range(2)))
    return 0

def manual_matrix()->int:
    """8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее
в последнюю ячейку строки. В конце следует вывести полученную матрицу."""
    test_matrix = []
    row_count = 4
    colm_count = 5
    for i in range(row_count):
        matrix_row = []
        element_sum = 0
        for j in range(colm_count - 1):
            element = int(input(f"Please enter an element[{i}, {j}] of matrix: "))
            matrix_row.append(element)
            element_sum += element
        matrix_row.append(element_sum)
        test_matrix.append(matrix_row)
    for i in range(row_count):
        print("____"*colm_count)
        for j in range(colm_count):
            print(test_matrix[i][j], end = " | ")
        print()
    print("____"*colm_count)
    return 0

def max_from_min()->int:
    """9. Найти максимальный элемент среди минимальных элементов столбцов матрицы."""
    test_matrix = matrix_generator(2, 5, 6) #генерируем 2 массив [5x6]
    print(test_matrix)
    print("The max element is",max(list(min(row) for row in list(zip(*test_matrix)))))
    return 0


menu = {
    "Task 1 - Кратность чисел" : int_division_rates,
    "Task 2 - Индексы четных эл-тов" : even_elemenst_ind,
    "Task 3 - Поменять мин. и макс. эл-ты" : elements_exchange,
    "Task 4 - Самое часто встречающ. число" : most_frequence_elem,
    "Task 5 - Макс. отрицательный эл-т" : max_negativ_elem,
    "Task 6 - Сумма эл-тов между мин. и макс. эл-тами" : min_max_sum,
    "Task 7 - Два наименьших эл-та" : min_pair,
    "Task 8 - Ручной ввод и расчет последнего эл-та" : manual_matrix,
    "Task 9 - Макс. эл-т среди мин. эл-тов в столбцах" : max_from_min,
    "Exit" : exit
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
