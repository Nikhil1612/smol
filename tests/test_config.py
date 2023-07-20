import unittest
from src import config

class TestConfig(unittest.TestCase):

    def test_target_size(self):
        self.assertIsInstance(config.TARGET_SIZE, int)
        self.assertGreater(config.TARGET_SIZE, 0)

    def test_test_duration(self):
        self.assertIsInstance(config.TEST_DURATION, int)
        self.assertGreater(config.TEST_DURATION, 0)

    def test_cursor_size(self):
        self.assertIsInstance(config.CURSOR_SIZE, int)
        self.assertGreater(config.CURSOR_SIZE, 0)

if __name__ == "__main__":
    unittest.main()