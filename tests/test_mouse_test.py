import unittest
from src.mouse_test import MouseTest

class TestMouseTest(unittest.TestCase):

    def setUp(self):
        self.mouse_test = MouseTest()

    def test_start_test(self):
        self.mouse_test.start_test()
        self.assertTrue(self.mouse_test.test_started)

    def test_end_test(self):
        self.mouse_test.start_test()
        self.mouse_test.end_test()
        self.assertFalse(self.mouse_test.test_started)

    def test_hit_target(self):
        self.mouse_test.start_test()
        self.mouse_test.hit_target()
        self.assertEqual(self.mouse_test.hits, 1)

    def test_miss_target(self):
        self.mouse_test.start_test()
        self.mouse_test.miss_target()
        self.assertEqual(self.mouse_test.misses, 1)

if __name__ == '__main__':
    unittest.main()