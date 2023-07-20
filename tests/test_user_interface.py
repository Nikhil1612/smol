import unittest
from src.user_interface import UserInterface

class TestUserInterface(unittest.TestCase):

    def setUp(self):
        self.ui = UserInterface()

    def test_display_ui(self):
        self.ui.display_ui()
        self.assertTrue(self.ui.is_displayed)

    def test_handle_user_interaction(self):
        self.ui.handle_user_interaction('start_test')
        self.assertTrue(self.ui.test_started)

        self.ui.handle_user_interaction('end_test')
        self.assertFalse(self.ui.test_started)

if __name__ == '__main__':
    unittest.main()