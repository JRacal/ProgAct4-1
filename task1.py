import unittest

def area(a):
    if a == 'TIP_Manila':
        return True
    else:
        return False

def ipaddress(ip):
    if ip == '192.168.45.25':
        return True
    else:
        return False

def subnetmask(subnet):
    if subnet == '255.255.255.0':
        return True
    else:
        return False
    

class MyTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(area('TIP_Manila'))
        self.assertTrue(ipaddress('192.168.45.25'))
        self.assertTrue(subnetmask('255.255.255.0'))
    def test_2(self):
        self.assertTrue(area('TIP_Qc'))
        self.assertTrue(ipaddress('192.168.45.24'))
        self.assertTrue(subnetmask('255.255.255.0'))
    def test_3(self):
        self.assertTrue(area('TIP_Manila'))
        self.assertTrue(ipaddress('192.168.45.25'))
        self.assertTrue(subnetmask('255.255.255.0'))
    def test_4(self):
        self.assertTrue(area('TIP_Manila'))
        self.assertTrue(ipaddress('192.168.45.24'))
        self.assertTrue(subnetmask('255.255.0.0'))


if __name__ == '__main__':
    unittest.main()