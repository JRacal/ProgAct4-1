import unittest

def devices(device):
    if '10.10.1.0' <= device < '10.10.1.255':
        if device == '10.10.1.1':
            return "Router"
        else:
            return "Personal Computer"
    elif '10.10.6.0' <= device < '10.10.8.0':
        return "Switches"
    elif device == '10.10.9.1':
        return "Server"
    else:
        return "Invalid ip"

class testip(unittest.TestCase):
    def test_router(self):
        self.assertEqual(devices('10.10.3.1'), "Router")
    def test_pc(self):
        self.assertEqual(devices('10.10.2.20'), "Personal Computer")
    def test_switches(self):
        self.assertEqual(devices('10.10.8.0'), "Switches")
    def test_server(self):
        self.assertEqual(devices('10.10.10.1'), "Server")
    def test_invalid(self):
        self.assertEqual(devices('10.10.1.2'), "Invalid ip")
    
if __name__ == '__main__':
    unittest.main()
    