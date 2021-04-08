import socket

sock = socket.socket()
sock.setblocking(1)
port = int(input('Введите номер порта: '))
host = input('Введите хост: ')

# port = 9090
# host = '192.168.1.147'

print("Соединение с сервером")
sock.connect((host, port))

while True:
    msg = input('Введиты строку для передачи или exit для выхода: ')
    if msg == 'exit':
        break
    # print("Отправка данных серверу")
    sock.send(msg.encode())

    # print("Прием данных от сервера")
    data = sock.recv(1024)
    print(data.decode())

print("Разрыв соединения с сервером")