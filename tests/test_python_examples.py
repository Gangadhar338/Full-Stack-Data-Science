import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "01-Python" / "examples"
EXPECTED = {"01_conditionals.py": "B", "02_loops.py": "Sum: 5050", "03_functions.py": "4.0", "04_data_structures.py": "83.75", "05_file_handling.py": "Hello, files!", "06_exceptions.py": "246", "07_oop.py": "Asha True", "08_modules.py": ".csv", "09_comprehensions.py": "[1, 4, 9, 16, 25]", "10_generators.py": "[3, 2, 1]", "11_decorators.py": "Finished", "12_type_hints.py": "4.0", "13_package_demo.py": "Full-Stack-Data-Science"}

class TestPythonExamples(unittest.TestCase):
    def test_all_examples(self):
        for filename, expected in EXPECTED.items():
            with self.subTest(example=filename):
                result = subprocess.run([sys.executable, str(EXAMPLES / filename)], capture_output=True, text=True, timeout=10)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn(expected, result.stdout)

if __name__ == "__main__":
    unittest.main(verbosity=2)
