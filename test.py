import unittest

class Tests(unittest.TestCase):
    def test_whereis(self):
        from butils import whereis
        location = whereis(whereis)
        self.assertTrue(isinstance(location.line_no, int))
        self.assertTrue(isinstance(location.filename, str))

if __name__ == '__main__':
    unittest.main()
