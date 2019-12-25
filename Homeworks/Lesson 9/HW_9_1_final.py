import json

def data_collection (**kwrds):
    """
    Сбор персональных данных
    """
    return kwrds
    
def data_save (a):
    """
    Занесение возврата data_collection в файл
    """
    with open('HW_9.json', 'w') as data_in:
        json.dump(a, data_in)

all_data = data_collection (name='Oleksand', last_name = 'Bilozortsev',
                            telephone_number = '+380977778899',
                            street = 'Parkovaya str.',
                            city = 'Kramatorsk', country = 'Ukraine')

data_save(all_data)

def data_takeout (b):
    """
    Извлечение данных из файла
    """
    with open('HW_9.json') as data_out:
        load_from_file = (json.load(data_out))
        return load_from_file

print (data_takeout(''))
