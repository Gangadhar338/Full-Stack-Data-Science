# Python File Handling

Use `with open(...)` to manage files safely. Choose an encoding explicitly.

## Example
```python
from pathlib import Path

path = Path("example.txt")
path.write_text("Hello, files!", encoding="utf-8")
content = path.read_text(encoding="utf-8")
print(content)
```

## Practice
1. Write three lines to a text file.
2. Read the file and count its lines.
3. Handle a missing file with try/except.
