import random 
import time

mao_humano = []
mao_robo = []

def lin():
    print("=" * 90)

while True:    
    cartas_robo = random.randint(1,13)
    cartas_humano = random.randint(1,13)
    print(f"Cartas do dealer: {mao_robo}")
    print(f"Suas cartas: {mao_humano}")
    
    escolha = input("Deseja jogar? ")
    if escolha == "S":
       
        mao_robo.append(cartas_robo)
        mao_humano.append(cartas_humano)

        print(f"A carta sorteada do dealer é: {mao_robo}")
        print(f"A sua carta sorteada é: {mao_humano}")
    
    while True:
        choice = int(input("""Escolha uma das opções: 
[1] - Hit
[2] - Run
"""))

        if choice == 1:
            nova_humano = random.randint(1,13)
            mao_humano.append(nova_humano)
            if sum(mao_humano) > 21:
                print("Você perdeu")
                print(f"Esta foi a carta sorteada: {nova_humano} | Total: {sum(mao_humano)}")
                mao_humano.clear()
                mao_robo.clear()
                break
            
            elif sum(mao_humano) == 21:
                print("Você venceu!")
                print(f"Esta foi a carta sorteada: {nova_humano} | Total: {sum(mao_humano)}")
                mao_humano.clear()
                mao_robo.clear()
                break
            
            else:
                print(f"A carta sorteada foi {nova_humano}")
                print(f"Essas são suas cartas {mao_humano} | Total: {sum(mao_humano)}")
        
        if choice == 2:
            
            while True:
                novo_robo = random.randint(1,13)
                print(f"Total: {sum(mao_robo)} | Esta foi a carta da mesa sorteada: {novo_robo}")
                mao_robo.append(novo_robo)
                time.sleep(1)
                
                if sum(mao_robo) > 21:
                    print(f"Total: {sum(mao_robo)} | Esta foi a carta da mesa sorteada: {novo_robo}")
                    print("A casa perdeu!")
                    mao_humano.clear()
                    mao_robo.clear()
                    break
            
                elif sum(mao_robo) == 21:
                    print(f"Total: {sum(mao_robo)} | Esta foi a carta da mesa sorteada: {novo_robo}")
                    print("Empate!")
                    mao_humano.clear()
                    mao_robo.clear()
                    break               
                
                elif sum(mao_robo) > sum(mao_humano):
                    print(f"Total: {sum(mao_robo)} | Esta foi a carta da mesa sorteada: {novo_robo}")
                    print("A casa venceu!")
                    mao_humano.clear()
                    mao_robo.clear()
                    break
                
            break