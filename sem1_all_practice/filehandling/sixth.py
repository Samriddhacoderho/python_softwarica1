import pickle

a={"name":"Sam","color":"blue"}
c=pickle.dumps(a)
print(c)
d=pickle.loads(c)
print(d)
