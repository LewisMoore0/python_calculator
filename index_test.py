from unittest import TestCase
from index import add, subtract, multiply, divide

class IndexTest(TestCase):

    def test_add(self):
        assert add(1, 1) == 2

    def test_subtract(self):
        assert subtract(3, 1) == 2

    def test_multiply(self):
        assert multiply(2, 10) == 20
    
    def test_divide(self):
        assert divide(10, 2) == 5