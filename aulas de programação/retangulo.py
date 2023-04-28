class Ret:
    def __init__(self,base,altura):
        self.altura = altura
        self.base = base

    def mudar_lados(self,base,altura):
        """
            Insira os novos valores para que sejam alterados.
        """
        self.base = base
        self.altura = altura

    def retorna_L(self):
        return (self.base,self.altura)

    def calc_area(self):
        return self.base * self.altura

    def calc_perim(self):
        return (self.base + self.altura)*2

    
while True:
    print("construtora sem nome\n")
    base = float(input('Digite a base do chão: '))
    altura = float(input('Digite a altura do chão'))
    projeto = Ret(base,altura)

    largura_p = float(input('qual a largura do piso? '))
    altura_p = float(input('Qual a altura do piso? '))
    area_p = (largura_p*altura_p)*0.01

    quant = 0
    while True:
        if quant >= projeto.calc_area():
            print(quant)
            break
        else:
            quant+=1