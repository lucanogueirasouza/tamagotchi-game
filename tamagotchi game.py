from os import system
from random import randint
from time import sleep

def randomizar_numero(): 
    return randint(0,100)

def random_numero_especificacoes(): 
    return randint(1,15)

def limpar_tela(): 
    system("Cls")

def limitar_valor(valor):
    return max(0, min(100, valor))

def mostrar_tamagotchi(tamagotchi):
    for chave, valor in tamagotchi.items():
        if chave in ["Felicidade:", "Fome:", "Energia:"]:
            print(
                f"{chave} {valor}%"
                )
        else:
            print(
                f"{chave} {valor}"
                )

def instrucoes_jogatina():
    ver_instrucoes = str(input(
        "Deseja ver as instruções do jogo? [S/N]: "
    )).strip().lower() 
    limpar_tela()
    if ver_instrucoes == "s": 
        limpar_tela()
        print (
            "INSTRUÇÕES:\n" \
            "1. Não deixe a 'Fome' chegar em Cem (100)\n" \
            "2. Não deixe a 'Felicidade' chegar em Zero (0)\n" \
            "3. Não deixe a 'Energia' chegar em Zero (0)\n" \
            "4. Caso seu Tamagotchi chegar em 20 Anos, ele(a) falecerá."
        )
        sleep(10)
        limpar_tela()

def pular_dia(tamagotchi):
    tamagotchi["Energia:"] = limitar_valor(tamagotchi["Energia:"] + random_numero_especificacoes()) 
    tamagotchi["Felicidade:"] = limitar_valor(tamagotchi["Felicidade:"] - random_numero_especificacoes()) 
    tamagotchi["Fome:"] = limitar_valor(tamagotchi["Fome:"] + random_numero_especificacoes())
    tamagotchi["Idade:"] += 1

def brincar_tamagotchi(tamagotchi):
    tamagotchi["Energia:"] = limitar_valor(tamagotchi["Energia:"] - random_numero_especificacoes())
    tamagotchi["Felicidade:"] = limitar_valor(tamagotchi["Felicidade:"] + random_numero_especificacoes())
    tamagotchi["Fome:"] = limitar_valor(tamagotchi["Fome:"] + random_numero_especificacoes())

def fazer_tamagotchi_comer(tamagotchi):
    tamagotchi["Fome:"] = limitar_valor(tamagotchi["Fome:"] - random_numero_especificacoes())
    tamagotchi["Felicidade:"] = limitar_valor(tamagotchi["Felicidade:"] + random_numero_especificacoes())
    tamagotchi["Energia:"] = limitar_valor(tamagotchi["Energia:"] + random_numero_especificacoes())

def jogar():
    comecar_jogo = str(input(
        "Deseja começar o jogo? [S/N]: "
        )).lower().strip()
    limpar_tela()

    if comecar_jogo.startswith("s"): 
        instrucoes_jogatina()
        
        nome = str(input(
            "Digite o nome do seu novo Tamagotchi: "
            )).capitalize().strip()
        limpar_tela()

        tamagotchi = {
            "Nome:": nome,
            "Idade:": 0,
            "Felicidade:": randomizar_numero(),
            "Fome:": randomizar_numero(),
            "Energia:": randomizar_numero(),
        }

        mostrar_tamagotchi(tamagotchi)
        print("-=-" * 7)

        while True:
            if tamagotchi["Energia:"] == 0 or tamagotchi["Felicidade:"] == 0 \
            or tamagotchi["Fome:"] == 100 or tamagotchi["Idade:"] >= 20:
                limpar_tela()
                print(
                    f"Seu Tamagotchi, {nome}, faleceu.\n"
                    )
                print(
                    "Status Finais:"
                    )
                mostrar_tamagotchi(tamagotchi)
                break
            else: 
                painel_escolha = int(input(
                    f"[1] - Fazer o(a) {nome}, Comer\n"
                    f"[2] - Brincar com o(a) {nome}\n"
                    "[3] - Pular 'Dia'\n"
                    "Escolha: "
                ))

                if painel_escolha == 3:
                    limpar_tela()
                    print("-=-" * 7)
                    pular_dia(tamagotchi)
                    mostrar_tamagotchi(tamagotchi)
                    print("-=-" * 7)
                    continue

                if painel_escolha == 2:
                    limpar_tela()
                    print("-=-" * 7)
                    brincar_tamagotchi(tamagotchi)
                    mostrar_tamagotchi(tamagotchi)
                    print("-=-" * 7)
                    continue

                if painel_escolha == 1:
                    limpar_tela()
                    print("-=-" * 7)
                    fazer_tamagotchi_comer(tamagotchi)
                    mostrar_tamagotchi(tamagotchi)
                    print("-=-" * 7)
                    continue

jogar()