from unittest import TestCase
from index import add
from index import subtract

class IndexTest(TestCase):

    def test_add(self):
        assert add(1, 1) == 2

    def test_subtract(self):
        assert subtract(3, 1) == 2