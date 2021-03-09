from conta import Conta

conta = Conta(123, "Nico", 55.5, 1000.0)

print(conta)
print(conta.numero)
print(conta.titular)
print(conta.saldo)
print(conta.limite)


conta.extrato()
conta.deposita(15.0)
conta.extrato()
conta.saca(10.0)
conta.extrato()
