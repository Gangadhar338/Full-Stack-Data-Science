def mean(xs):
 if not xs: raise ValueError('empty values')
 return sum(xs)/len(xs)
print(mean([2,4,6]))
