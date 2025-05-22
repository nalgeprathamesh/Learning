# Common set operations included union,intersection, differnece, symmetric difference and subset/superset
s1 = {21,342,0,28938,928,1,2,3}
s2 = {82948,893,123,1,2,3,0}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.issubset(s2))
print(s1.symmetric_difference(s2))