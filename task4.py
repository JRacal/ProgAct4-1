import unittest

def subnetmask(subnet):
    if subnet >= '255.255.255.0':
        return "class C"
    elif subnet >= '255.255.0.0':
        return "class B"
    elif subnet >= '255.0.0.0':
        return "class A"
    else:
        return f"invalid subnet: {subnet}"

class TestSubnet(unittest.TestCase):
    def testclass1(self):
        self.assertEqual(subnetmask('255.0.0.0'),"class A")
    def testclass2(self):
        self.assertEqual(subnetmask('255.255.0.0'),"class B")
    def testclass3(self):
        self.assertEqual(subnetmask('255.255.255.0'),"class C")
    def testclass4(self):
        self.assertEqual(subnetmask('0.0.0.0'),"invalid subnet: 0.0.0.0")

if __name__ == '__main__':
    unittest.main()