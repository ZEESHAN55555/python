test=input("Enter string")
l=[]
l=test.split()
freq=[l.count(p) for p in l]
print(zip(l,freq))
print(dict(zip(l,freq)))


my_dict={'apple':10,'banana':20,'angle':30}

for key,value in my_dict.items():
    if key[0].lower()=='b':
        print(f"the valueof '{key}' is {value}")