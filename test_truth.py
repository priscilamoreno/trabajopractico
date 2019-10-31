import unittest


class TestTruth(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_false(self):
        self.assertFalse(False)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
