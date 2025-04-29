# Jogo de Par ou ímpar para exercitar Laços de repetição.

from random import randint

cnt = 0

print("=-="*10)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-="*10)

while True:
    escolha = str(input("Par ou Impar? [P/I] ")).upper().strip()[0]
    n = int(input("Diga um valor: "))
    print('-'*30)
    c = randint(0, 10)
    s = n + c
    if n > 10 or escolha not in "PI":
        print("ERRO! Por favor digite um numero menor ou igual a 10 e escolha PAR ou IMPAR!")
        print("=-="*10)
    if (escolha == "P" and s % 2 == 0) or (escolha == "I" and s % 2 != 0):
        print(f"Você VENCEU! Você jogou {n} e o computador jogou {c}. Total de {s} DEU PAR")
        print("Vamos jogar novamente...")
        print("=-="*10)
        cnt += 1
    elif (escolha == "P" and s % 2 != 0) or (escolha == "I" and s % 2 == 0):
        break
print(f"Você perdeu! Você jogou {n} e o computador jogou {c}. Total de {s} DEU IMPAR. Vitórias consecutivas: {cnt}")
print("=-="*10)
