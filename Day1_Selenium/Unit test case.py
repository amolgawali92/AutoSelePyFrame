import unittest

class MyTestCase(unittest.TestCase):
    pass
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4)

    class MyTestCase(unittest.TestCase):
    def setUp(self):

# Code executed before each test

        def tearDown(self):


# Code executed after each test

        def test_addition(self):


# Test logic goes here

        if __name__ == '__main__':
            unittest.main()
