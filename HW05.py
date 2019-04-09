#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных
# числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.

from collections import namedtuple, defaultdict

def enteprises_calc()->int:
    enterprise = namedtuple('enterprise', [
        'name',
        'first_qrt_profit',
        'second_qrt_profit',
        'third_qrt_profit',
        'forth_qrt_profit'])
    enterprises_data = []
    enterprises_count = int(input("Pleas enter a required number of enteprises: "))
    for i in range(1, enterprises_count + 1):
        print(f"Please, enter {i}-th enterprise data in format: Company name, 1-th quarter profit, 2-th quarter profit,"
              f"3-th quarter profit, 4-th quarter profit")
        raw_data = input().split(",")
        for i in range(1, 5):
            raw_data[i] = float(raw_data[i])
        enterprises_data.append(enterprise(*raw_data))
    enterprise_profit = {}
    average_profit = 0
    for enterp in enterprises_data:
        profit_sum = 0
        for i in range(1, 5):
            profit_sum += enterp[i]
        enterprise_profit.setdefault(enterp[0],profit_sum)
        average_profit += profit_sum/enterprises_count
    print(f"Average profit for all enterprises is {average_profit}")
    print("List of enterprises, which profit lower than average value:")
    for k, v in enterprise_profit.items():
        if v < average_profit:
            print(f"{k} with profit {v}")
    print("List of enterprises, which profit greater than average value:")
    for k, v in enterprise_profit.items():
        if v >= average_profit:
            print(f"{k} with profit {v}")
    return 0


enteprises_calc





