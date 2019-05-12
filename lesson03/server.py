import json
import argparse
from socket import *

parser = argparse.ArgumentParser()
parser.add_argument('-a', default='', help='all by default')
parser.add_argument('-p', default=7777, help='7777 by default')
args = parser.parse_args()

s = socket(AF_INET, SOCK_STREAM)
s.bind((args.a, args.p))
s.listen(1)
print('Server started - {}:{}'.format(args.a, args.p))


def send_msg_to_client(clt, msg) -> None:
    clt.send(msg)
    clt.close()


while True:
    client, address = s.accept()
    data = client.recv(1000)
    print('Client message: ', data.decode('utf-8'), ' receive from client: ', address)

    try:
        data_d = json.loads(data)
    except Exception as e:
        send_msg_to_client(client, e)
        continue

    action = data_d["action"]
    if action == "presence":
        send_msg_to_client(client, 'Presence received'.encode('utf-8'))
