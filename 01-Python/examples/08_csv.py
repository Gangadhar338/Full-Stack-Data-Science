import csv
from pathlib import Path
p=Path('scores.csv')
with p.open('w',newline='',encoding='utf-8') as f: csv.writer(f).writerows([['name','score'],['Asha',90]])
with p.open(newline='',encoding='utf-8') as f: print(list(csv.reader(f)))
