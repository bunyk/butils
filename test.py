
from mock import Mock, patch
import unittest


class TestWhereis(unittest.TestCase):
    def test_whereis(self):
        from butils import whereis
        location = whereis(whereis)
        self.assertTrue(isinstance(location.line_no, int))
        self.assertTrue(isinstance(location.filename, str))

    def test_with_generator(self):
        from butils import whereis
        def g():
            yield 1
        location = whereis(g())
        print type(g)
        self.assertTrue(isinstance(location.line_no, int))
        self.assertTrue(isinstance(location.filename, str))


class TestWatchForOutput(unittest.TestCase):
    def test_works(self):
        from butils import watch_for_output

        mock_stdout = Mock()
        output = []
        def write(txt):
            output.append(txt)
        mock_stdout.write  = write
        with patch('sys.stdout', mock_stdout):
            watch_for_output(lambda s: 'yes' in s)
            print 'yes'

        self.assertIn('test.py:', output[1])
        self.assertIn("print 'yes'", output[1])

class TestPprint(unittest.TestCase):
    # def test_works(self):
    #     from butils.pprint import pprint

    #     mock_stdout = Mock()
    #     output = []
    #     def write(txt):
    #         output.append(txt)
    #     mock_stdout.write  = write
    #     mock_sys = Mock()
    #     mock_sys.stdout = mock_stdout

    #     with patch('butils.pprint.sys', mock_sys):
    #         pprint({'a': [1, 2]})

    #     self.assertEquals(output, [])

    def test_other(self):
        from butils.pprint import pprint
        # pprint('asdf ' * 200)



if __name__ == '__main__':
    unittest.main()
