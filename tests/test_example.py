import io
import sys
import unittest

from example_package import example


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.stdout = sys.stdout
        sys.stdout = io.StringIO()

    def tearDown(self) -> None:
        sys.stdout = self.stdout

    def test_hello_world(self):
        example.hello_world()
        self.assertEqual(sys.stdout.getvalue(), "Hello World!\n")

    def test_httpbin_get(self):
        response = example.httpbin_get()
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
