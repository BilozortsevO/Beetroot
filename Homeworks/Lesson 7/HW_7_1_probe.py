# dict comprehension exercise

string = 'Links \nLinks \nLinks \nLinks zwei, drei, vier. \nLinks zwei, links zwei, links zwei, drei, vier, links. \nLinks zwei, links zwei, links zwei, drei, vier, links. \nLinks zwei, drei, vier!'
print (string)

chars = '.,;:"\'!?'

string = string.replace('\n', '')

for i in chars:
    string = string.replace (i, '')

string = string.lower()
lst = list (string.split(' '))
st = set (lst)
tpl = tuple (st)
dictio = {tpl[i] : lst.count(tpl[i]) for i in range(len (tpl))}

print(dictio)
