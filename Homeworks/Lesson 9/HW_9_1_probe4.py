import json

def data_collection (**kwrds):
    """
    Сбор персональных данных
    """
    dc = {}
    for k, v in kwrds.items():
        v = input ('Please insert '+k+' ')
        dc.setdefault(k, v)
    
    return dc
    
def data_save (func):
    """
    Занесение возврата data_collection в файл
    """
    with open('HW_9.json', 'w') as data:
        data.write(str(func))

print (data_collection (name=None, last_name =None,
                        telephone_number =None,
                        street =None,
                        city =None, country =None))

data_save(data_collection)
