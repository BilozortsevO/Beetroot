
class Person:
    def __init__ (self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        
        
    @property
    def full_name (self):
        return self.first_name.title() + ' ' + self.last_name.title()

    @property
    def email_box (self):
        return self.first_name.lower() + '.' + self.last_name.lower() + '@email.com'


fellow = Person ('svirid', 'golohvostov')
print (fellow.full_name)
print (fellow.email_box)
fellow2 = Person ('proniya',  'prokopovna')
print (fellow2.full_name)
print (fellow2.email_box)
