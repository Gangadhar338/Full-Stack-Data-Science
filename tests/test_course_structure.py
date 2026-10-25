import unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
class TestCourse(unittest.TestCase):
 def test_modules(self):
  fs=[p for p in R.iterdir() if p.is_dir() and p.name[:2].isdigit()]; self.assertGreaterEqual(len(fs),15)
  for p in fs:
   with self.subTest(module=p.name): self.assertTrue((p/'README.md').exists())
 def test_examples(self): self.assertGreaterEqual(len(list((R/'01-Python'/'examples').glob('*.py'))),8)
 def test_rag(self): self.assertTrue((R/'09-NLP-and-Generative-AI'/'lessons'/'02-rag-checklist.md').exists())
if __name__=='__main__': unittest.main(verbosity=2)
