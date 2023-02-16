#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число 
#N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#n = 5
#1 2 3 4 5
#x = 3
#-> 1



def list_1(length_list: int) -> list:
	list_2 = list()
	for i in range(length_list):
		list_2.append(int(input(f"Введите {i + 1} элемент массива -> ")))
	return list_2

def result_list(list2: list, find_count_num_in_list: int) -> int:
	count = 0
	for i in list2:
		if find_count_num_in_list == i:
			count += 1
	return count
length_list = int(input("Введите длину массива -> "))
find_number = int(input("Введте число, которое нужно посчитать -> "))
list_2 = list_1(length_list)
find_count_number = result_list(list_2, find_number)

print(f"Количество числа {find_number} в списке {list_2} = {find_count_number}")