class Summary:
 def __init__(self,x): self.x=list(x)
 def mean(self): return sum(self.x)/len(self.x)
print(Summary([2,4,6]).mean())
