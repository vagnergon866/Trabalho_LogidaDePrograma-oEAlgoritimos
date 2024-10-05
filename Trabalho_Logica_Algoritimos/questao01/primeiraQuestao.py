print("Sistema desenvolvido por Vagner do Amaral Gonçalves")

valor_base = float(input("Informe o valor base do plano: R$ "))
idade = int(input("Informe a idade do cliente: "))

if idade == 0 and idade < 19:
    porcentagem = 1
    valor_mensal = valor_base * porcentagem
elif idade >= 19 and idade < 29:
    porcentagem = 1.5
    valor_mensal = valor_base * porcentagem
elif idade >= 29 and idade < 39:
    porcentagem = 2.25
    valor_mensal = valor_base * porcentagem
elif idade >= 39 and idade < 49:
    porcentagem = 2.4
    valor_mensal = valor_base * porcentagem
elif idade >= 49 and idade < 59:
    porcentagem = 3.5
    valor_mensal = valor_base * porcentagem
else:
    porcentagem = 6
    valor_mensal = valor_base * porcentagem

print(f"Valor mensal do plano é de : R${valor_mensal}")
