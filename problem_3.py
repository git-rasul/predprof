import csv
def main():
	"Точка входа программы"
	while True:
		query = input('Ввод: ')
		if query == 'СТОП': break

		with open('students.csv') as file:
			r = csv.reader(file)
			lines = [line for line in r]
			found = False
			for line in lines:
				if query == line[2]:
					sec_name, first_name, last_name = line[1].split()
					found = True
					print(f'Вывод: Проект № {query} делал: {first_name[0]}. {sec_name} он(а) получил(а) оценку - {line[-1]}')
			if found == False:
				print('Вывод: Ничего не найдено')

main()
