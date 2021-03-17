# Дан список чисел, который может содержать до 100000 чисел.
# Определите, сколько в нем встречается различных чисел.
# Функциональное программирование (ФП)

print(len(set(list(map(int, input().split())))))

# Пример др задачи на основе ФП:
# С помощью этих функций можно решить достаточно сложные задачи,
# без использования циклов и условных операторов.
# Например, задачу из домашнего задания по сортировкам про такси:
# в первой строке задано количество людей и автомобилей такси,
# в следующих двух строках расстояние в километрах для каждого человека и цена за километр для каждого такси.
# Необходимо сопоставить каждому человеку номер такси, чтобы суммарная цена поездок была минимальна.
# Идея решения заключается в том, чтобы люди, которым ехать дальше, ехали на более дешевых такси:

input()  # Пропускаем количества, обойдемся без них
people = map(int, input().split())
sortedPeople = sorted(enumerate(people), key=lambda x: x[1])
taxi = map(int, input().split())
sortedTaxi = sorted(enumerate(taxi), key=lambda x: x[1], reverse=True)
ans = zip(sortedPeople, sortedTaxi)
sortedAns = sorted(ans, key=lambda x: x[0][0])
print(*map(lambda x: x[1][0], sortedAns))

input()  # Пропускаем количества, обойдемся без них
print(
    *map(
        lambda x: x[1][0],
        sorted(
            zip(
                sorted(
                    enumerate(map(int, input().split())),
                    key=lambda x: x[1]
                ),
                sorted(
                    enumerate(map(int, input().split())),
                    key=lambda x: x[1],
                    reverse=True
                )
            ),
            key=lambda x: x[0][0]
        )
    )
)
