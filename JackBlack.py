import random 
import time

mao_humano = []
mao_robo = []

def lin():
    print("=" * 90)

while True:    
    
    escolha = input("Deseja jogar?(S/N): ")
    
    if escolha.upper() == "S":
        cartas_robo = random.randint(1,13)
        cartas_humano = random.randint(1,13)
        print(f"Cartas do dealer: {mao_robo}")
        print(f"Suas cartas: {mao_humano}")
        mao_robo.append(cartas_robo)
        mao_humano.append(cartas_humano)

        print(f"A carta sorteada do dealer é: {mao_robo}")
        print(f"A sua carta sorteada é: {mao_humano}")
    
    elif escolha.upper() == "N":
        print("Fechando o programa...")
        exit()
    
    else:
        print("Valor inválido")
        continue
    
    while True:
        try:
            choice = int(input("""Escolha uma das opções: 
[1] - Hit
[2] - Run
[0] - Sair
"""))
            lin()

            if choice == 1:
                nova_humano = random.randint(1,13)
                mao_humano.append(nova_humano)
                if sum(mao_humano) > 21:
                    print("Você perdeu")
                    print(f"Esta foi a carta sorteada: {nova_humano} | Total: {sum(mao_humano)}")
                    lin()
                    mao_humano.clear()
                    mao_robo.clear()
                    break
                
                elif sum(mao_humano) == 21:
                    print("Você venceu!")
                    print(f"Esta foi a carta sorteada: {nova_humano} | Total: {sum(mao_humano)}")
                    lin()
                    mao_humano.clear()
                    mao_robo.clear()
                    break
                
                else:
                    print(f"A carta sorteada foi {nova_humano}")
                    print(f"Essas são suas cartas {mao_humano} | Total: {sum(mao_humano)}")
            
            if choice == 2:
                
                while True:
                    print(f"Essas são as cartas da casa: {mao_robo} | Total: {sum(mao_robo)}")
                    novo_robo = random.randint(1,13)
                    mao_robo.append(novo_robo)
                    time.sleep(1)
                    lin()
                    
                    if sum(mao_robo) > 21:
                        print(f"Esta foi a carta da mesa sorteada: {novo_robo} | Total: {sum(mao_robo)} ")
                        print("A casa perdeu!")
                        lin()
                        mao_humano.clear()
                        mao_robo.clear()
                        break
                
                    elif sum(mao_robo) > 21:
                        print(f"Esta foi a carta da mesa sorteada: {novo_robo} | Total: {sum(mao_robo)}")
                        print("A casa venceu!")
                        lin()
                        mao_humano.clear()
                        mao_robo.clear()
                        break               
                    
                    elif sum(mao_robo) > sum(mao_humano):
                        print(f"Esta foi a carta da mesa sorteada: {novo_robo} | Total: {sum(mao_robo)} | ")
                        print("A casa venceu!")
                        lin()
                        mao_humano.clear()
                        mao_robo.clear()
                        break
                 
                    else:
                        print(f"Esta foi a carta da mesa sorteada: {novo_robo} | Total: {sum(mao_robo)}")
                 
            if choice == 0:
                print("Finalizado a aplicação...")
                exit()
                 
        except ValueError:
            print("Valor inválido")
            lin()
                  
            break