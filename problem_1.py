import csv

def main():
	"Точка входа программы"
	with open('students.csv') as file:
		r = csv.reader(file)
		lines = [line for line in r]
		
		score_sum, score_counter = 0, 0
		ids_to_change = []
		for line in lines[1:]:
			if line[-1] != 'None':
				score_sum += int(line[-1])
				score_counter += 1
			else:
				ids_to_change.append(line[0])

			if 'Хадаров Владимир' in line[1]:
				score = int(line[-1])
				project = int(line[2])
				print(f'Ты получил: {score}, за проект - {project}')

		average = round(score_sum/score_counter,3)
		for i, line in enumerate(lines):
			if line[-1] == 'None':
				lines[i][-1] = average
	

	with open('students_new.csv', 'w') as file:
		w = csv.writer(file)
		w.writerows(lines)
	
main()
