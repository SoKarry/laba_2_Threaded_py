import socket
import threading

def recv_data(sc):
    while True:
        data = sc.recv(1024)
        print('\r' + data.decode() + '\n' + 'Вы: ', end='')

host = '127.0.0.1'
port = 9091

sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sc.connect((host, port))


while True:
    nickname_inp=input('Введите Ваш ник: ')
    nickname='<nick_check>='+nickname_inp
    sc.send(nickname.encode())
    data = sc.recv(1024)
    data = data.decode()
    if data == '<nick_check_true>':
        print(f'Ник успешно задан, добро пожаловаь в чат, {nickname_inp}')
        break
    elif data == '<nick_check_false>':
        print(f'Этот ник уже занят, введите другой!')

t1 = threading.Thread(target=recv_data, args=(sc,), daemon=True)
t1.start()
sc.send('__join'.encode())

while True:
    data = input(f'Вы: ')
    sc.send(data.encode())