import os
import unittest
from edtech_quiz import load_questions
from edtech_quiz import save_results

class TestQuiz(unittest.TestCase):

    def test_load_questions(self):
        questions = load_questions("questions.csv")
        self.assertIsInstance(questions, list)
        self.assertGreater(len(questions), 0)

    def test_save_results(self):
        test_file = "test_results.csv"

        if os.path.exists(test_file):
            os.remove(test_file)

        save_results(test_file, "Test User", "Test School", ["a", "b", "c"])

        self.assertTrue(os.path.exists(test_file))


if __name__ == "__main__":
    unittest.main()
