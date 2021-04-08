import threading
import socket

print("Запуск сервера")
sock = socket.socket()
sock.bind(('', 9090))
print("Начало прослушивания порта")
sock.listen(0)
msg = ''


def serv_func(conn, addr):
	msg=''
	print("Подключение клиента")
	print(addr)
	while True:
		# print("Прием данных от клиента")
		data = conn.recv(1024)
		if not data:
			break
		msg += data.decode()
		# print("Отправка данных клиенту")
		conn.send(data)
	print(msg)
	print(f"Отключение клиента {addr}")
	conn.close()

while True:
	conn, addr = sock.accept()
	th = threading.Thread(target=serv_func, args=(conn, addr))
	th.start()