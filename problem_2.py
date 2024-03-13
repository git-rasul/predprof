import csv

def main():
	"Точка входа программы"
	with open('students.csv') as file:
		r = csv.reader(file)
		lines = [line for line in r if line[-1] != 'None']

		lines = insertion_sorting(lines[1:], lambda x: int(x[-1]))
		counter = 0
		print('10 класс:')
		for i in range(len(lines)):
			if lines[i][-1] == '5' and '10' in lines[i][3]:
				counter += 1
				full_name = lines[i][1]
				sec_name, first_name, last_name = full_name.split()
				print(f'{counter} место: {first_name[0]}. {sec_name}')
				if counter >= 3: break

def insertion_sorting(lines, key):
	"""Данная функция осуществляет сортировку учеников по
	результатам оценивания проекта

	Описание аргументов:
	lines - список учеников
	key - ключ для сортировки"""

	ids = [i for i in range(len(lines))]
	scores = [key(x) for x in lines]

	for i in range(1, len(ids)):
		for j in range(i, 0, -1):
			if scores[j] < scores[j-1]:
				scores[j], scores[j-1] = scores[j-1], scores[j]
				ids[j], ids[j-1] = ids[j-1], ids[j]
	
	res = [lines[i] for i in ids]
	return res


main()

		
