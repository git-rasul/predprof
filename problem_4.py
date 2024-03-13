import sys
import csv
import random

def main():
	"Точка входа программы"
	data = sys.stdin.read()
	lines = data.strip().split('\n')
	for i, line in enumerate(lines): lines[i] = [x for x in line.split(',')]
	
	for i, line in enumerate(lines):
		if i == 0: continue
		login = make_login(line[1])
		password = generate_password()
		lines[i].append(login)
		lines[i].append(password)
	
	with open('students_password.csv', 'w') as file:
		w = csv.writer(file)
		w.writerows(lines)

def make_login(name):
	"""Функция, создающая логин по шаблоны
	Описание аргументов:
	name - полное имя ученика
	"""
	sec_name, first_name, last_name = name.split()
	res = f'{sec_name}_{first_name[0]}{last_name[0]}'
	return res

def good(password):
	"""Функция проверяет, включает ли пароль в себя заглавные, строчные буквы английского алфавита и цифры
	Описание аргументов:
	password - массив символов пароля
	"""
	c1, c2, c3 = False, False, False
	for s in password:
		if 49 <= ord(s) <= 57: c1 = True
		if 97 <= ord(s) <= 122: c2 = True
		if 65 <= ord(s) <= 90: c3 = True

	return c1 and c2 and c3

def generate_password():
	"Функция генерирует пароль по шаблону"
	while True:
		alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
		password = []
		for _ in range(8):
			password.append(alph[random.randrange(len(alph))])
		
		if good(password): return ''.join(password)

main()
