from abc import ABC, abstractmethod
from abc import abstractproperty   #<- virou obsoleto o abstractproperty

#Teste 1
class Mob(ABC):
    @abstractmethod
    def fazer_ruido(self):
        pass

class UrubuDoPix(Mob):
    def fazer_ruido(self):
        return "E o pix?!"

class Lacraia(Mob):
    def fazer_ruido(self):
        return "É O TCHAN!"

urubu_pix = UrubuDoPix()
print(urubu_pix.fazer_ruido())

lacraia = Lacraia()
print(lacraia.fazer_ruido())


#Teste 2
class Livraria(ABC):
    @abstractmethod
    def comprar(self):
        pass
    
    @abstractmethod
    def vender(self):
        pass
    
    
class Cliente(Livraria):
    def vender(self):
        return "Vou vender minha alma"
    
    def comprar(self):
        return "Vou comprar um livro de autoajuda(Estoicismo), -> idiotice"
    

p1 = Cliente()
print(p1.comprar())
print(p1.vender())




#teste 3
class MyBaseClass(ABC):
    @property
    @abstractmethod
    def my_abstract_property(self):
        pass

class MyClass(MyBaseClass):
    @property
    def my_abstract_property(self):
        return 'Esta é uma propriedade concreta'

obj = MyClass()
print(obj.my_abstract_property)

