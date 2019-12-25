# Декоратор переименовывает функцию
def original_function():
    print("")
print(original_function.__name__)

def decor(func):
    def wrapper():
        print("")
        return func()
    return wrapper
@decor
def original_function():
    print("")
print(original_function.__name__)

# Декоратор не переименовывает функцию
import functools  
def decor(func):
    @functools.wraps(func)
    def wrapper():
        print("")
        return func()
    return wrapper
@decor
def original_function():
    print("")
print(original_function.__name__)
