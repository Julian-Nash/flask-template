from app import create_app

import unittest


class TestApp(unittest.TestCase):
    """ Example HTTP tests """

    def setUp(self) -> None:
        self.app = create_app("testing")
        self.client = self.app.test_client()

    def test_index_returns_200_response(self):

        r = self.client.get("/")
        self.assertEqual(r.status_code, 200)
