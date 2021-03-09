from conta import Conta

print("Cria conta 1")
conta = Conta(123, "Nico", 55.5, 1000.0)

print(conta)

# atributos privados
print(conta._Conta__numero)
print(conta._Conta__titular)
print(conta._Conta__saldo)
print(conta._Conta__limite)

conta.extrato()
conta.deposita(15.0)
conta.extrato()
conta.saca(10.0)
conta.extrato()

print("Cria conta 2")
conta2 = Conta(321, "Marco", 100.0, 1000.0)
conta2.extrato()
print("Transfere da conta 2 para conta 1")
conta2.transfere(10.0, conta2, conta)
conta2.extrato()


print("Exibe o limite")
print(conta.get_limite())

print("Exibe o saldo")
print(conta.get_saldo())

print("Exibe o titular")
print(conta.get_titular())

print("Define o limite")
conta.set_limite(1000.0)
print(conta.get_limite())
