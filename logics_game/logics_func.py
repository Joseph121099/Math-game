import random # импортируем модуль random
#import os # импортируем модуль os для очистки консоли.  os.system("cls")

#####################################################################################
def multiplication():
	multiplication_1 = random.randint(1, 10)
	multiplication_2 = random.randint(1, 10)

	result_1 = multiplication_1 * multiplication_2

	print("Пример: " + str(multiplication_1) + " * " +  str(multiplication_2))

	entered = ""
	while entered != result_1:	
		entered = int(input("Введите число: "))

		if entered == result_1:
			print("Верно.")
			division()
		elif entered != result_1:
			print("Неправильно.")
			multiplication()
#######################################################################################





#######################################################################################
def division():
	division_1 = random.randint(1, 10)
	division_2 = random.randint(1, 10)

	# Пофиксить баг
	# while division_1 < division_2:
	# 	if division_1 < division_2:
	# 		division_1 = random.randint(1, 10)
	# 		division_2 = random.randint(1, 10)
	# 	else:
	# 		pass

	result_2 = division_1 // division_2

	print("Пример: " + str(division_1) + " / " + str(division_2))

	entered = ""
	while entered != result_2:
		entered = int(input("Введите число: "))

		if entered == result_2:
			print("Верно.")
			addition()
		elif entered != result_2:
			print("Неправильно.")
			division()
#######################################################################################





#######################################################################################
def addition():
	addition_1 = random.randint(1, 10)
	addition_2 = random.randint(1, 10)

	result_3 = addition_1 + addition_2

	print("Пример: " + str(addition_1) + " + " + str(addition_2))

	entered = ""
	while entered != result_3:
		entered = int(input("Введите число: "))

		if entered == result_3:
			print("Верно.")
			subtraction()
		elif entered != result_3:
			print("Неправильно.")
			addition()		
#######################################################################################





#######################################################################################
def subtraction():
	subtraction_1 = random.randint(1, 10)
	subtraction_2 = random.randint(1, 10)

	result_4 = subtraction_1 - subtraction_2

	print("Пример: " + str(subtraction_1) + " - " + str(subtraction_2))

	entered = ""
	while entered != result_4:
		entered = int(input("Введите число: "))

		if entered == result_4:
			print("Верно.")
			break	
		elif entered != result_4:
			print("Неправильно.")
			#subtraction()
#######################################################################################




