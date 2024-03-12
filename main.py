def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def divisao(a,b):
    if b!=0:
        return a/b
    else:
        return "não é possível"

    def multiplicaçao(a,b):
        return a*b

numero_1 = int(input("informe o primeiro número"))
numero_2 = int(input("informe o segundo número"))
operador = input("Informe o operador \n+-adição \n-subtração \n/divisão \n.multiplicacão \n => ")

if operador == "+":
    print("resultado ", soma(numero_1, numero_2))
elif operador =="-":
    resultado = numero_1 + numero_2
    print(f"resultados= {resultado}")
elif operador =="/":
    resultado = numero_1 / numero_2
    print(f"resultados= {resultado}")
elif operador =="*":
    resultado = numero_1 * numero_2
    print(f"resultado={resultado}")
else:
    print("escolha uma das 4 opições")

