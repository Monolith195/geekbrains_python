import json
import argparse
from datetime import datetime
from socket import *

parser = argparse.ArgumentParser()
parser.add_argument('address', help='server\'s ip', type=str)
parser.add_argument('port', default=7777, help='server\'s port, 7777 by default', nargs='?', type=int)
args = parser.parse_args()

s = socket(AF_INET, SOCK_STREAM)
s.connect((args.address, args.port))


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


def send_msg(msg_b) -> None:
    s.send(msg_b)


send_msg(create_presence_msg())
data = s.recv(2000)
print('Server message: ', data.decode('utf-8'))
s.close()
