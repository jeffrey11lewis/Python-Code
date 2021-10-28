import os.path
import unittest

file_exists = os.path.exists(r'C:\Users\torch\Desktop\clickHere.bat')

class test_file_Exists(unittest.TestCase):
    def test_file_exists(self):

        self.assertTrue(file_exists)
print('file exists = ', file_exists)