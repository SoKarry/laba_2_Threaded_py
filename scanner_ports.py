import threading
import socket
from time import sleep
from progress.bar import Bar

# host = input('Введите хост: ')
host = '192.168.1.147'
ports=[]

def check_ports(bar, l, r):
    global ports
    for port in range(l, r):
        bar.next()
        sock = socket.socket()
        try:
            sock.connect((host, port))
            ports.append(port)
            sock.close()
        except ConnectionRefusedError:
            pass
        except OSError:
            pass #фильтрую порт 0
        except TimeoutError:
            pass

threads=[]
bar = Bar('Processing', max=65536)

#делим на 512 потоков
for i in range(1, 513):
    th = threading.Thread(target=check_ports, args=(bar, (i-1)*128, i*128))
    threads.append(th)
    th.start()
for th in threads:
    th.join()


print('\nОткрытые порты: ')
ports.sort()
bar.finish()
for i in ports:
    print(i)