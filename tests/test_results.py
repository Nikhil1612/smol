import unittest
from src.results import Results

class TestResults(unittest.TestCase):

    def setUp(self):
        self.results = Results()

    def test_calculate_results(self):
        self.results.hits = 5
        self.results.misses = 5
        self.results.calculate_results()
        self.assertEqual(self.results.accuracy, 50)

    def test_display_results(self):
        self.results.hits = 8
        self.results.misses = 2
        self.results.calculate_results()
        result_string = self.results.display_results()
        self.assertEqual(result_string, "Accuracy: 80%")

if __name__ == '__main__':
    unittest.main()