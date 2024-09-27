anterior=0
proxima=1
soma=1

for n in range(0,34):
    soma=proxima+anterior
    anterior=proxima
    proxima=soma
    numero=int(input("Digite um número:"))
    if numero!=anterior:
        print("Seu núnmero não faz parte da sequência de Fibonacci.")
            