#Suma de nunmeros con input fuera de while
total = 0
nro = float(input("Numero: "))
while nro != 0:
    total += nro
    nro = float(input("Numero: "))
print("Total: ", total)

#Suma de numeros con input dentro de while y con variable al principio
total = 0
nro = 1
while nro != 0:
    nro = float(input("Numero: "))
    total += nro
print("Total: ", total)

#programa del monto a pagar
total = 0
monto = float(input("monto de la venta: $"))

while monto != 0:
    if monto < 0:
        print("Monto no valido")

    else:
        total += monto
    monto = float(input("Monto de la venta: $"))

if total > 1000:
    total -= total * 0.1
print("Monto total a pagar $", round(total,2))