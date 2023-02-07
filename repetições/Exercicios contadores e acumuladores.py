depósito = float(input("Digite o depósito inicial: "))
taxa= float(input("Digitea taxa de juros de uma poupança: "))
investimento = float(input("Digitea investimento por mes:  "))
mês = 1
saldo = depósito

while mês <= 24:
    saldo = saldo + (saldo * (taxa/100)) + investimento
    print(f"Saldo do mês {mês} é de R${saldo:5.2f}")
    mês = mês + 1
print(f"O ganho obtido com os juros foi de R${saldo-depósito:8.2f}.")
