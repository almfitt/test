#!python3
#6.2
'''

Задание 6.2
Сделать копию скрипта задания 6.2.
Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
    состоит из 4 чисел разделенных точкой,
    каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение: „Неправильный IP-адрес“

Ограничение: Все задания надо выполнять используя только пройденные темы.

    Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
    Определить тип IP-адреса.
    В зависимости от типа адреса, вывести на стандартный поток вывода:
        „unicast“ - если первый байт в диапазоне 1-223
        „multicast“ - если первый байт в диапазоне 224-239
        „local broadcast“ - если IP-адрес равен 255.255.255.255
        „unassigned“ - если IP-адрес равен 0.0.0.0
        „unused“ - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''



while True:
    ip_add = input('ввод IP-адреса в формате 10.0.1.1: ')
    ip_add = ip_add.split('.')
    if len(ip_add) != 4:
        print('Октета должно быть 4-ре, это же IP')
        continue
    try:
        ee = 0
        for i in ip_add:
            if int(i) >=0 and int(i) <= 255:
                ee = ee+1
            else:
                break
        if ee == 4:
            break
    except:
        continue

ip_new = []

for i in ip_add:
	ip_new.append(int(i))
if ip_new == [255,255,255,255]:
	print('local broadcast')
elif ip_new ==[0,0,0,0]:
		print('unassigned')
elif ip_new[0] in range(1,224):
	print('unicast')
elif ip_new[0] in range(224,240):
	print('multicast')
else:
	print('unused')


"""
while True:
    if len(ip_add) == 4:
        break
    else:
        ip_add = input('Неправильный IP-адрес.\nВведи в формате 10.1.1.1: ')
        ip_add = ip_add.split('.')

digit = ip_add   
     

while True:
	if digit[0].isdigit() != True:
		True
	elif int(digit[0]) not in range(256):
		True
	else:
		break
	digit = input('Неправильный IP-адрес.\nВведи в формате 10.1.1.1: ')
	digit = digit.split('.')

while True:
	if digit[1].isdigit() != True:
		True
	elif int(digit[1]) not in range(256):
		True
	else:
		break
	digit = input('Неправильный IP-адрес.\nВведи в формате 10.1.1.1: ')
	digit = digit.split('.')

while True:
	if digit[2].isdigit() != True:
		True
	elif int(digit[2]) not in range(256):
		True
	else:
		break
	digit = input('Неправильный IP-адрес.\nВведи в формате 10.1.1.1: ')
	digit = digit.split('.')


while True:
	if digit[3].isdigit() != True:
		True
	elif int(digit[3]) not in range(256):
		True
	else:
		break
	digit = input('Неправильный IP-адрес.\nВведи в формате 10.1.1.1: ')
	digit = digit.split('.')

ip_new = []

for i in digit:
	ip_new.append(int(i))
if ip_new == [255,255,255,255]:
	print('local broadcast')
elif ip_new ==[0,0,0,0]:
		print('unassigned')
elif ip_new[0] in range(1,224):
	print('unicast')
elif ip_new[0] in range(224,240):
	print('multicast')
else:
	print('unused')
"""

