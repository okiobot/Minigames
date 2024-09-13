import random 
import time

#Classe criada para modificar a quantidade de dinheiro que o usuário possui
class Money():
    def __init__(self, valor):
        self.valor = valor
    
    #Verificar o valor 
    def get_valor(self):
        return self.valor
    
    #Definir um novo valor
    def set_valor(self, novo_valor):
        self.valor = novo_valor

#Linha usada para demilitar
def linha():
    print("="*90)
    
#Símbolos disponíveis para o caça-níquel escolher
simbolos = ["@" , "#", "&", "7"]

modo = input("Digite '1' para iniciar Máquina de Cassino")
if __name__ == "__main__":    
    casino = Money(3000)
    
    while True:
        if modo == "1":
            try:
                
                #Se o usuário não possuir mais dinheiro, ele será "expulso" e não poderá mais jogar
                if casino.get_valor() == 0:
                    print("Você não tem mais dinheiro para apostar")
                    exit()
                
                #O usuário define a quantidade que deseja apostar
                print(f"Você possui R${casino.get_valor()}")
                aposta = int(input("Quanto dinheiro você deseja apostar: "))
                if aposta > casino.get_valor():
                    linha()
                    print("Você não possui o total apostado")
                    linha()
                    continue
            
            #Se o usuário digitar algo que não seja um número, o sistema detectará e não permitirá que o código continue
            except ValueError:
                print("Dado inválido")
                linha()
                continue
            linha()
            casino.set_valor(casino.get_valor() - aposta)
            x = input("Deseja roletar?: S/N ")
            jogar = x.upper()    
            
            #A máquina escolhe um dos símbolos e o adiciona à lista, três vezes
            if jogar == "S": 
                rodada = []
                time.sleep(0.5)
                escolha_maquina = random.choice(simbolos)
                print(escolha_maquina+" |", end=" ")
                rodada.append(escolha_maquina)
                time.sleep(0.5)
                escolha_maquina = random.choice(simbolos)
                print(escolha_maquina+" |", end=" ")
                rodada.append(escolha_maquina)
                time.sleep(0.5)
                escolha_maquina = random.choice(simbolos)
                print(escolha_maquina)
                rodada.append(escolha_maquina)
               
                #Se os símbolos forem iguais, o sistema detecta a vitória, triplica o valor apostado e soma ao total 
                if rodada[0] == rodada[1] and rodada[0] == rodada[2]:
                    linha()
                    print("Você venceu! Dinheiro apostado triplicado")
                    linha()
                    casino.set_valor(casino.get_valor() + aposta * 3)
                else:
                    #Caso o usuário perca, o valor apostado será reduzido do total e o sistema perguntará se o usuário gostaria de tentar novamente
                    linha()
                    y = input("Você perdeu, deseja tentar novamente? S/N ")
                    linha()
                    dnv = y.upper()
                    if dnv == "N":
                        #Mostra o total que o usuário possui
                        print(f"Você terminou com R${casino.get_valor()}")
                        exit()
                    else:               
                        continue
                    
                    #Limpa a lista para preparar para a próxima rodada, se houver
                    rodada.clear 
            else:
                exit()
