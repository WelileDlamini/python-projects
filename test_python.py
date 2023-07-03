# how unittest works
import unittest
import python_scripting

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = mainnn.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'shkshks'
        result = mainnn.do_stuff(test_param)
        self.assertEqual(result, ValueError)
unittest.main()


