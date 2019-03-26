import os




def cls():
    os.system(['clear','cls'][os.name == 'nt'])

def network       ():
	cls()
	f=os.popen("ip a")
	rd=f.read()
	#print(rd)
	f.close()
	while 1:
		print(rd)
		print('0. Выход')
		v = input("Введите:")
		if v == '0':
			break

		cls()

# now, to clear the screen
def users():
	cls()
	f = open('/etc/passwd')
	f=f.read()
	while 1:
		
		print('Имя машины: ',f)
		print('0. Выход')
		v = input("Введите:")
		if v == '0':
			break

		cls()	 
def hosts():
	cls()
	f = open('/etc/hostname')
	f=f.read()
	while 1:
		print(f)
		print('0. Выход')
		v = input("Введите:")
		if v == '0':
			break

		cls()	

cls()
a = ''' 
1. Пользователи
2. Настроить сеть
3. Имя машины
4. Сервисы
0. Выход
'''

while 1:
	print(a)
	v = input("Введите:")
	if v == '1':
		users()
	elif v == '3':
		hosts()
	elif v == '2':
		network()
	elif v == '0':
		break

	cls()
