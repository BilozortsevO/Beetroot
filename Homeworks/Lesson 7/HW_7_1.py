# dict comprehension exercise

string = 'Links Links Links Links zwei drei vier Links zwei links zwei links zwei drei vier links Links zwei links zwei links zwei drei vier links Links zwei drei vier'
print (string)
string = string.lower()
lst = list (string.split(' '))
st = set (lst)
tpl = tuple (st)
dictio = {tpl[i] : lst.count(tpl[i]) for i in range(len (tpl))}

print(dictio)
