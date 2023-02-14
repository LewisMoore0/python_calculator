from unittest import TestCase
from index import add

class IndexTest(TestCase):

    def test_add(self):
        assert add(1, 1) == 2
