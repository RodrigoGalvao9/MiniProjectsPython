import functools


def metodo(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result   
    
    return wrapper

@metodo
def replica(so_teste):
    print("aleluia")
    return so_teste

p1 = replica("Vai com tudo!")

print(replica.__wrapped__)
print(replica.__name__)
