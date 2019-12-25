# dict comprehension exercise

string = 'Links \nLinks \nLinks \nLinks zwei, drei, vier. \nLinks zwei, links zwei, links zwei, drei, vier, links. \nLinks zwei, links zwei, links zwei, drei, vier, links. \nLinks zwei, drei, vier!'
print (string)
# deleting of punctuation marks
string = string.replace(',', '')
string = string.replace('.', '')
string = string.replace('!', '')
string = string.replace('\n', '')
# making all characters low
string = string.lower()
# convertering str to list
lst = list (string.split(' '))
# converting list to set to remove duplicates
st = set (lst)
# converting set to tuple to use iteration
tpl = tuple (st)
# creating a dictionary
dictio = {tpl[i] : lst.count(tpl[i]) for i in range(len (tpl))}

print(dictio)
