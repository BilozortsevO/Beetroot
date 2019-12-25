# Creating a dictionary
def make_country (name, capital):
    print ("Country's name is " + name, "with the capital in " + capital)
dictio = {'name' : 'Czech', 'capital' : 'Prague'}    
make_country (dictio.get('name'), dictio.get('capital'))
