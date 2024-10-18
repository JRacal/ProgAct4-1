import unittest

def ipformat(ip):
    if '0.0.0.0' <= ip < '255.255.255.255':
        return True
    else:
        return False

class testformat(unittest.TestCase):
    def testformat(self):
        self.assertTrue(ipformat('192.168.1.1'))

if __name__ == '__main__':
    unittest.main()