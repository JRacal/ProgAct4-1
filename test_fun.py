import unittest

def fun(x):

    return x+1

class MyTest(unittest.TestCase):

    def test(self):
        self.assertEqual(fun(5),6)

if __name__ == '__main__':
    unittest.main()