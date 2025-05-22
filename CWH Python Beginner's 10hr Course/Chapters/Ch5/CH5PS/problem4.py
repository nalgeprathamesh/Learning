# Guess the length of set 20 , 20.0 , '20'
s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s)) #It gives value as 2
# Python has considered 20 and 20.0 as same even if 20.0 is technically floating point
# The reason is python considers them numerically equal and thus ignore that they are different data types