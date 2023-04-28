class Bola:
    def __init__(self,cor,circunferencia,material):
        self.cor = cor
        self.circ = circunferencia
        self.material = material
    
    def trocar_cor(self,nova_cor):
        self.cor = nova_cor

    def mostrar_cor(self):
        print(self.cor)


classe_bola = Bola('vermelha',2,'plastico')
classe_bola.mostrar_cor()
classe_bola.trocar_cor('azul')
classe_bola.mostrar_cor()