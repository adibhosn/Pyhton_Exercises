numeroSec = 40

chute = int(input("Digite um número: "))

acertou = chute == numeroSec
maior = chute > numeroSec
menor = chute < numeroSec
if(acertou):
    print("Parabéns! Você acertou!")
else:
    if menor:
        print("O número secreto é maior.")
    elif maior:
        print("O número secreto é menor.")


