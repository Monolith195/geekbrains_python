import unittest
import json
from lesson04.server import request_handler


def assert_equal(x, y):
    assert x == y, '{} != {}'.format(x, y)


class TestServer(unittest.TestCase):
    def test_success_response(self):
        request = {
            "action": "presence"
        }
        response = {
            "response": 200
        }
        assert_equal(request_handler(request).decode('utf-8'), json.dumps(response))

    def test_error_response(self):
        request = {
            "action": "error"
        }
        response = {
            "response": 400,
            "error": "Bad Request"
        }
        assert_equal(request_handler(request).decode('utf-8'), json.dumps(response))
