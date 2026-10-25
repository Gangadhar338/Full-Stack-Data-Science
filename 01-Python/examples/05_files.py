from pathlib import Path
p=Path('sample_output.txt'); p.write_text('Reliable data matters.\n',encoding='utf-8'); print(p.read_text(encoding='utf-8').strip())
