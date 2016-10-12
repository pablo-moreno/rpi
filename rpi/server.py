import settings

import socket

from os.path import join

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((settings.ANDROID_IP, settings.PORT))
s.listen()
print('Server listening at {}:{}'.format('192.168.1.41', settings.PORT))
running = True
i = 1
while running:
    try:
        sc, address = s.accept()
        print('Client connected: {}'.format(address))
        file = join(settings.ANDROID_DIR, "file_{}".format(i))
        f = open(file, 'wb')
        i += 1
        l = sc.recv(1024)
        while l:
            f.write(l)
            l = sc.recv(1024)
        print('File received: {}'.format(file))
        f.close()
        sc.close()
    except KeyboardInterrupt:
        running = False
        print('\nServer closed')
s.close()