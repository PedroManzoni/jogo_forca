import random

print('------------------------------')
print('--------JOGO DA FORCA---------')
print('------------------------------\n')

arquivo = open("palavras.txt","r")
palavras = []

for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)

arquivo.close()

numero = random.randrange(0, len(palavras))
palavra_secreta = palavras[numero].upper()

letras = ['_' for letra in palavra_secreta]


enforcou = False
acertou = False
erros = 0

print(letras)
while( not enforcou and not acertou):

    
    print(" ")

    chute = input('Qual a letra que você deseja chutar?\n')
    chute = chute.strip().upper()

    if(chute in palavra_secreta):

        index = 0

        for letra in palavra_secreta:

            if(chute == letra):
                letras[index] = letra
            index = index + 1
                
                
            
    else:
        erros += 1

        print(f'você errou a {erros}ª vez, o limite são 6 erros \n')
        
    enforcou = erros == 6
    acertou = "_" not in letras
    print(letras)
    print(" ")


if(acertou):
    print("Você ganhou!!\n")
else:
    print("Você perdeu..\n")


print('FIM DE JOGO...')



