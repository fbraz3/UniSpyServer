import unittest
from frontends.gamespy.library.network.http_handler import HttpConnection
from frontends.gamespy.library.configs import ServerConfig
from frontends.tests.gamespy.library.mock_objects import LogMock
from frontends.gamespy.library.abstractions.client import ClientBase


class DummyHTTPHandler:
    def __init__(self, client_address=("127.0.0.1", 12345), headers=None):
        self.client_address = client_address
        self.headers = headers or {}


class HttpConnectionTest(unittest.TestCase):
    def setUp(self):
        self.config = ServerConfig("http_test", 80, 80, "127.0.0.1")
        self.logger = LogMock()

    def test_default_remote_ip(self):
        handler = DummyHTTPHandler(client_address=("127.0.0.1", 54321))
        conn = HttpConnection(handler, self.config, ClientBase, self.logger)
        self.assertEqual(conn.remote_ip, "127.0.0.1")

    def test_x_real_ip_header(self):
        handler = DummyHTTPHandler(
            client_address=("127.0.0.1", 54321),
            headers={"X-Real-IP": "203.0.113.195"}
        )
        conn = HttpConnection(handler, self.config, ClientBase, self.logger)
        self.assertEqual(conn.remote_ip, "203.0.113.195")
        self.assertEqual(conn.ip_endpoint, "203.0.113.195:54321")

    def test_x_forwarded_for_header(self):
        handler = DummyHTTPHandler(
            client_address=("127.0.0.1", 54321),
            headers={"X-Forwarded-For": "198.51.100.17, 127.0.0.1"}
        )
        conn = HttpConnection(handler, self.config, ClientBase, self.logger)
        self.assertEqual(conn.remote_ip, "198.51.100.17")


if __name__ == "__main__":
    unittest.main()
