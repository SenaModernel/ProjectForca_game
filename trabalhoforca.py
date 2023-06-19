import os
import time
import random
import sys
#Jogo feito por: Pedro Sena e Luis Yago


def limpar_tela ():
    os.system('cls')

strength1 = '''  
         __________
        |         |
        |
        |
        |
        |
        """     
        '''
strength2 = ''' 
        __________
        |        |
        |        O
        |
        |
        |
        """
        '''

strength3 = ''' 
        __________
        |        |
        |        O
        |        |
        |
        |
        """
        '''



strength4 = '''
        __________
        |         |
        |         O
        |        /|
        |
        |
        """
        '''

strength5 = '''__
        ________
        |      |
        |      O
        |     /|\\
        |
        |
        """ 
        '''

strength6 ='''   
        __________
        |        |
        |        O
        |       /|\\
        |       /
        |
        """ 
'''

dicas = [] 


nome1 = input("Nome do desafiante? ").upper()

nome2 = input("Nome do desafiado? ").upper()
limpar_tela()


normas = print(f"{nome1},O DESAFIO JÁ VAI COMEÇAR!")
time.sleep(3)
limpar_tela()

palavra_chave = input("\nInsira a PALAVRA CHAVE: ").lower().strip()

dica1 = input(f"\n Se possivel,{nome1} ajude inserindo a Dica (1): ")
dicas.append(dica1)
dica2 = input(f"\nSe possivel,{nome1} ajude inserindo a Dica (2): ")
dicas.append(dica2)
dica3 = input(f"\nSe possivel,{nome1} ajude inserindo a Dica (3): ")
dicas.append(dica3)
time.sleep(0)
limpar_tela()


print(f"Buenas, {nome2} você foi desafiado por {nome1}!!")

time.sleep(3)
limpar_tela()
num_dicas = 3 
acertos = 0
erros = 0 
letra_digitadas = []
letras_certas = []
letras_erradas = []
index = 0

while True:
    key = ''
    for letra in palavra_chave:
        key += letra if letra in letras_certas else "_ "
    print("Acerte a palavra:",key)
    if erros ==0:
            print(strength1)       
    if key == palavra_chave:
       print(f'''{nome2} VENCEU O DESAFIO!!

                          (づ｡◕‿‿◕｡)づ
            ''')
       break
    print ('''\n        Você tem direito a 3 dicas!
                    Caso se garanta, digite uma letra remetente a palavra...
                        Se desejar as dicas,  (1)!  ''') 
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa == '1':
        if index < len(dicas): 
                        print("\ndica: ",dicas[index],"\n")
                        index += 1
                        time.sleep(3)
                        limpar_tela()
    try: 
        letra_digitadas
    except:
        print("Caracter inválido!\n")

    if tentativa in letra_digitadas:
        print("Você já tentou essa letra!\n")
        erros = erros
        
    else:
         letra_digitadas += tentativa
    
    if tentativa in palavra_chave or tentativa == '1':
        letras_certas += tentativa
    else:
        erros += 1
        print ("Essa letra não está na palavra!\n")

        if erros >=6:
            print('''       
        __________
        |        |
        |        O
        |       /|\\
        |       / \\
        |
        """    ''')
            print(f"{nome2} PARABÉNS TCHÊ, VOCÊ GANHOU DO {nome1}")
            break
        
        
    if tentativa:
        if erros ==1:
            print(strength2)
                

    if tentativa:
        if erros ==2:
            print(strength3)
                

    if tentativa:
        if erros ==3:
            print(strength4)
            
    if tentativa:
        if erros ==4:
            print(strength5)
                
    if tentativa:
        if erros ==5:
            print(strength6)
            
                
        if erros ==6:
            print(f'''
                    {nome1},VOCÊ NÃO CONCLUIU O DESAFIO DO {nome2}!''')



    


            
   






    
                
            
        





