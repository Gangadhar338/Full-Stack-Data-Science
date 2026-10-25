
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).parent
EXAMPLES = ROOT / "01-Python" / "01-Fundamentals" / "examples"


class TestPythonFundamentals(unittest.TestCase):

    def run_example(self, filename, user_input=""):
        script = EXAMPLES / filename
        result = subprocess.run(
            [sys.executable, str(script)],
            input=user_input,
            text=True,
            capture_output=True,
            timeout=10,
            cwd=ROOT
        )
        self.assertEqual(
            result.returncode,
            0,
            msg=f"{filename} failed:\n{result.stderr}"
        )
        return result.stdout

    def test_hello(self):
        output = self.run_example("01_hello.py")
        self.assertIn("Hello, Data Science!", output)

    def test_variables(self):
        output = self.run_example("02_variables.py")
        self.assertIn("Name: Rahul", output)
        self.assertIn("Age: 21", output)

    def test_operators(self):
        output = self.run_example("03_operators.py")
        self.assertIn("Addition: 13", output)
        self.assertIn("Remainder: 1", output)
        self.assertIn("Power: 1000", output)

    def test_strings(self):
        output = self.run_example("04_strings.py")
        self.assertIn("First character: P", output)
        self.assertIn("Uppercase: PYTHON", output)

    def test_input_output(self):
        output = self.run_example(
            "05_input_output.py",
            user_input="Gowth\n21\n"
        )
        self.assertIn("Hello, Gowth!", output)
        self.assertIn("Next year, you will be 22.", output)

    def test_invalid_age(self):
        output = self.run_example(
            "05_input_output.py",
            user_input="Gowth\nabc\n"
        )
        self.assertIn("Please enter your age as a whole number.", output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
