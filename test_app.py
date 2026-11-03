import unittest

from app import app, decode, encode


class CipherTests(unittest.TestCase):
    def test_round_trip(self):
        text = "Hello, World! 123"
        self.assertEqual(decode(encode(text)), text)

    def test_encode_known_value(self):
        self.assertEqual(encode("abc XYZ"), "qwe BNM")


class ApiTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_encode_endpoint(self):
        response = self.client.post("/encode", json={"text": "Hello"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["encoded"], "Itssg")

    def test_decode_endpoint(self):
        response = self.client.post("/decode", json={"text": "Itssg"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["decoded"], "Hello")

    def test_missing_text_returns_400(self):
        response = self.client.post("/encode", json={})
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
