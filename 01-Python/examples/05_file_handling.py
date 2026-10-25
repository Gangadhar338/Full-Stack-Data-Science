from pathlib import Path
p = Path("example.txt")
p.write_text("Hello, files!", encoding="utf-8")
print(p.read_text(encoding="utf-8"))
p.unlink(missing_ok=True)
