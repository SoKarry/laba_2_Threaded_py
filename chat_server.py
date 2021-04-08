import socket

host = '127.0.0.1'
port = 9091
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((host, port))
print('Сервер запущен успешно')

users = {}

while True:
    data, addr = s.recvfrom(1024)

    if data == '':
        continue

    user_id = addr[1]
    data = data.decode()
    if data == '__join':
        print(f'Client {user_id} joined chat')
        #показываем последние 10 сообщений из истории
        s.sendto('Последние 10 сообщений из истории переписки: '.encode(), addr)
        with open("history.txt") as file:
            for line in (file.readlines()[-10:]):
                s.sendto(line.encode(), addr)
        continue

    if '<nick_check>' in data:
        user_nick = data.split('>=')[1]
        if user_nick not in users.values():
            users.setdefault(addr, user_nick)
            s.sendto('<nick_check_true>'.encode(), addr)
            continue
        else:
            s.sendto('<nick_check_false>'.encode(), addr)
            continue

    data = f'{users.get(addr)}: {data}'
    print(data, file=open("history.txt", "a"))
    for user in users:
        if user != addr:
            s.sendto(data.encode(), user)