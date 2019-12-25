import json

def data_collection (**kwrds):
    """
    Сбор персональных данных
    """
    dc = kwrds
    return dc
    
def data_save (a):
    """
    Занесение возврата data_collection в файл
    """
    with open('HW_9.json', 'w') as data:
        json.dump(a, data)

all_data = data_collection (name='Oleksand', last_name = 'Bilozortsev',
                 telephone_number = '+380977778899',
                 street = 'Parkovaya str.',
                 city = 'Kramatorsk', country = 'Ukraine')

data_save(all_data)
