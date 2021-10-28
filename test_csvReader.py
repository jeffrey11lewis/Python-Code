import unittest

from csvReader import unitTestTEST

class TestIfCSV(unittest.TestCase):
    def test_spicyTest(self):
        self.assertEqual(unitTestTEST(3), 9 )
        self.assertEqual(unitTestTEST(5), 15)
        self.assertEqual(unitTestTEST(12), 36)