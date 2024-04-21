class Animal:
    def fazer_barulho(self):
        print("ruído génerico")
        

class Gato(Animal):
    def fazer_barulho(self):
        # return super().fazer_barulho()
        print("MIAIU")
    
    
class Cachorro(Animal):
    def fazer_barulho(self):
        # return super().fazer_barulho()
        print("AUAUAUAU")
    
    
p1 = Cachorro()
p2 = Gato()
barulho_cachorro = p1.fazer_barulho()
barulho_gato = p2.fazer_barulho()
# print(f"Barulho do cachorro: {barulho_cachorro}, Barulho do gato: {barulho_gato}")