import unittest
from src.ui.gui import NPuzzleGUI
from src.ui.cli import NPuzzleCLI

class TestNPuzzleUI(unittest.TestCase):

    def setUp(self):
        self.gui = NPuzzleGUI()
        self.cli = NPuzzleCLI()

    def test_gui_initialization(self):
        self.assertIsNotNone(self.gui)
        self.assertTrue(self.gui.is_initialized())

    def test_cli_initialization(self):
        self.assertIsNotNone(self.cli)
        self.assertTrue(self.cli.is_initialized())

    def test_gui_display(self):
        self.gui.display()
        self.assertTrue(self.gui.is_displayed())

    def test_cli_prompt(self):
        prompt = self.cli.get_prompt()
        self.assertEqual(prompt, "Enter your command: ")

    def test_gui_button_functionality(self):
        self.gui.setup_buttons()
        self.assertTrue(self.gui.buttons_are_functional())

    def test_cli_command_execution(self):
        result = self.cli.execute_command("solve")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()