import os 
import time
import bitcoinlib
import colorama

from colorama import Fore,Style
from bitcoinlib.wallets import Wallet
from bitcoinlib.mnemonic import Mnemonic
def clear ():
    os.system('cls' if os.name == 'nt' else 'clear')

def creates(name):
    clear()
    try:
        print("[+] Gerando chaves...")
        time.sleep(3)
        clear()
        mnemo = Mnemonic('english')
        key12 = mnemo.generate(strength=128)
        wall = Wallet.create(name, keys=key12, network='bitcoin')
        wallet_info = wall.get_key()
        
        print(f"\n[:3]CARTEIRA '{name}' GERADA COM SUCESSO!")
        print(f"Chave (12 PALAVRAS): {key12}\n")
        print(f"ENDEREÇO DE RECEBIMENTO: {wallet_info.address}\n")
        print(f"\nCHAVE PRIVADA (WIF):{wallet_info.wif}\n")

        for i in range(180, 0, -1):
            minutos = i // 60
            segundos = i % 60

            print(f"Auto-limpeza em: {minutos:02d}:{segundos:02d} ", end="\r")
            
            time.sleep(1) 
            
        clear()
        print("sucesso")
        time.sleep(2)

    except Exception as e:
        print(Fore.RED + f"ERRO: {e}")
        input("\nPressione Enter para continuar...")

INFO = "https://guns.lol/olho_zero"
logo = f"""{Fore.RED}  
                 ▓█████▄  ▄▄▄      ██▀███   ██ ▄█▀      ▄▄▄▄   ▄▄▄█████▓ ▄████▄ 
                  ▒██▀ ██▌▒████▄   ▓██ ▒ ██▒ ██▄█▒      ▓█████▄ ▓  ██▒ ▓▒▒██▀ ▀█ 
                  ░██   █▌▒██  ▀█▄ ▓██ ░▄█ ▒▓███▄░      ▒██▒ ▄██▒ ▓██░ ▒░▒▓█    ▄
                 ▒░▓█▄   ▌░██▄▄▄▄██▒██▀▀█▄  ▓██ █▄      ▒██░█▀  ░ ▓██▓ ░ ▒▓▓▄ ▄██
                 ░░▒████▓ ▒▓█   ▓██░██▓ ▒██▒▒██▒ █▄    ▒░▓█  ▀█▓  ▒██▒ ░ ▒ ▓███▀ 
                 ░ ▒▒▓  ▒ ░▒▒   ▓▒█░ ▒▓ ░▒▓░▒ ▒▒ ▓▒    ░░▒▓███▀▒  ▒ ░░   ░ ░▒ ▒  
                   ░ ▒  ▒ ░ ░   ▒▒   ░▒ ░ ▒ ░ ░▒ ▒░    ░▒░▒   ░     ░      ░  ▒  
                   ░ ░  ░   ░   ▒    ░░   ░ ░ ░░ ░       ░    ░   ░ ░    ░       
                     ░          ░     ░     ░  ░       ░ ░               ░ ░     
                     
                                    {INFO}
{Style.RESET_ALL}                     
"""
menu = f"""{Fore.RED}   
1 - Gerar Carteira
2 - Sair
{Style.RESET_ALL}
"""

while True:
    clear()
    print(logo)
    print(menu)
    escolhas = input("Digita: ")
    if escolhas == "1":
        clear()
        print("[+] AVISO IMPORTANTE:")
        print("O Uruma BTC é apenas um GERADOR de chaves.")
        print("Para gerir seus Bitcoins com total eficácia e segurança,")
        print("recomendamos o uso da ferramenta ELECTRUM.")
        input("Pressione o Enter para continuar")
        clear()
        name = input("Nome da carteira: ")
        clear()
        creates(name)
        break
    elif escolhas == "2":
        break
    input("...")
    clear()