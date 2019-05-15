import json
import argparse
from socket import *
from lesson04.utils import receive_size
from lesson04.utils import presence_d


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('address', help='server\'s ip', type=str)
    parser.add_argument('port', default=7777, help='server\'s port, 7777 by default', nargs='?', type=int)
    return parser


def create_connection(address, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((address, port))
    return s


def create_msg(message) -> bytes:
    msg = json.dumps(message)
    msg_b = msg.encode('utf-8')
    return msg_b


def send_msg(s, msg_b):
    s.send(msg_b)
    response_data = s.recv(receive_size).decode('utf-8')
    s.close()
    return response_data


def main():
    args = create_parser().parse_args()
    s = create_connection(args.address, args.port)
    print('Server message: ', send_msg(s, create_msg(presence_d)))


if __name__ == '__main__':
    main()
