# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
# из байтовового в строковый тип на кириллице.

import subprocess

web1 = ['ping', 'yandex.ru']
web2 = ['ping', 'youtube.com']

ping_yandex = subprocess.Popen(web1, stdout=subprocess.PIPE)

for line in ping_yandex.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))

ping_youtube = subprocess.Popen(web2, stdout=subprocess.PIPE)

for line in ping_youtube.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))
