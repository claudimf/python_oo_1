import gc
from conta import Conta

conta = Conta(123, "Nico", 55.5, 1000.0)
conta = Conta(123, "Nico2", 55.5, 1001.0)

print(
    "Garbage collection thresholds:", gc.get_threshold()
    )

collected = gc.collect()
print(
    "Garbage collector: collected", "%d objects." % collected
    )
