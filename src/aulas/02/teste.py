from conta import Conta

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
