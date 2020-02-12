

class arma:
    def __init__(self, nome, custo, dano, peso):
        self.nome = nome
        self.custo  = custo
        self.dano = dano
        self.peso = peso
    
    def __del__(self):
        pass

    def CriaArma(self): 
        nome = input('Digite o nome da arma: ')
        custo = int(input('Digite o custo da arma: '))
        dano = int(input('Digite o dano da arma: '))
        peso = int(input('Digite o peso da arma: '))
        NArma = arma(nome, custo, dano, peso)
        return NArma


    


        
        