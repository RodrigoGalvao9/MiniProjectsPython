def meu_decorador(funcao):
    def envelope():
        print("Envelope entregue")
        funcao()
    return envelope
        

@meu_decorador
def lacrar():
    print("lacrando")
    
lacrar()