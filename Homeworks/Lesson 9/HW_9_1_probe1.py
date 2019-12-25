

def data_collection (*args):
    """
    Сбор персональных данных
    """
    dc = args
    return dc
    
def data_save (func):
    """
    Занесение возврата data_collection в файл
    """
    with open('HW_9.txt', 'w') as data:
        data.write(str(func))

print (data_collection ('Oleksand', 'Bilozortsev',
                 '+380977778899', 'Parkovaya str.',
                 'Kramatorsk', 'Ukraine'))

data_save(data_collection)
