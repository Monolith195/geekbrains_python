import unittest
import json
from lesson04.utils import presence_d
from lesson04.client import send_msg
from lesson04.client import create_msg
from lesson04.server import request_handler


def assert_equal(x, y):
    assert x == y, "{} != {}".format(x, y)


class MockServer:
    def send(self, data):
        self.data = data

    def recv(self, port):
        request = json.loads(self.data)
        return request_handler(request)

    def close(self):
        pass


class TestClient(unittest.TestCase):
    client = MockServer()

    def test_incorrect_data(self):
        data = '{"action": "test"}'
        response = send_msg(self.client, data)
        response_d = json.loads(response)
        assert_equal(response_d['response'], 400)
        assert_equal(response_d['error'], 'Bad Request')

    def test_correct_data(self):
        response = send_msg(self.client, create_msg(presence_d))
        http_code = json.loads(response)['response']
        assert_equal(http_code, 200)
