import json
import argparse
from datetime import datetime
from socket import *
from lesson03.utils import receive_size


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('address', help='server\'s ip', type=str)
    parser.add_argument('port', default=7777, help='server\'s port, 7777 by default', nargs='?', type=int)
    return parser


def create_connection(address, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((address, port))
    return s


def create_presence_msg() -> bytes:
    presence_d = {
        "action": "presence",
        "time": datetime.now().isoformat(),
        "type": "status",
        "user": {
            "account_name": "test",
            "status": "I'm here"
        }
    }
    msg = json.dumps(presence_d)
    msg_b = msg.encode('utf-8')
    return msg_b


def send_msg(s, msg_b) -> None:
    s.send(msg_b)


def main():
    args = create_parser().parse_args()
    s = create_connection(args.address, args.port)
    send_msg(s, create_presence_msg())
    data = s.recv(receive_size)
    print('Server message: ', data.decode('utf-8'))
    s.close()


if __name__ == '__main__':
    main()
