print("Running test...") 

import unittest
from guessing_game import guessing_game

class TestGuessingGame(unittest.TestCase):
    def test_correct_guess_in_three_attempts(self):
        inputs = iter(["10", "70", "42"])
        outputs = []

        def mock_input(_): return next(inputs)
        def mock_print(msg): outputs.append(msg)

        tries = guessing_game(input_fn=mock_input, number=42, print_fn=mock_print)

        self.assertEqual(tries, 3)
        self.assertIn("Correct in 3 tries!", outputs[-1])
        self.assertIn("Too low.", outputs)
        self.assertIn("Too high.", outputs)

if __name__ == "__main__":
    unittest.main()
