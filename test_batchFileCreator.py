import os.path
import unittest

file_exists = os.path.exists(r'C:\Users\torch\Desktop\clickHere.bat')

class test_file_Exists(unittest.TestCase):
    def test_file_exists(file_exists):

        file_exists.assertTrue(file_exists)

#print(file_exists)