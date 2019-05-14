import json
import argparse
from socket import *
from lesson03.utils import *


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', default='', help='all by default')
    parser.add_argument('-p', default=7777, help='7777 by default')
    return parser


def start_server(server_address, server_port):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((server_address, server_port))
    s.listen(1)
    print(f'Server started - {server_address}:{server_port}')

    while True:
        client, address = s.accept()
        data = client.recv(receive_size)
        data_d = json.loads(data.decode('utf-8'))
        print(f'Client message: {data_d} receive from client: {address}')
        response = request_handler(data_d)
        send_msg_to_client(client, response)


def request_handler(request):
    if request['action'] == 'presence':
        return json.dumps(response_dict['OK']).encode('utf-8')
    else:
        return json.dumps(response_dict['Bad Request']).encode('utf-8')


def send_msg_to_client(clt, msg) -> None:
    clt.send(msg)
    clt.close()


def main():
    args = create_parser().parse_args()
    start_server(args.a, args.p)


if __name__ == '__main__':
    main()
