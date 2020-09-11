b1000 = 9
b500 = 19
b100 =  99

def retiro(monto):
       global b1000, b500, b100
       d1 = int(monto / 1000) #Se verifica si se pueden sacar billetes de 1000 y se obtiene la cantidad de billetes que se dispensaran
       monto = monto % 1000 # se obtiene el residuo de la division y se guarda en monto para el proximo billete
       if d1 >= b1000:
         monto = monto + (d1 - b1000) * 1000
         d1 = b1000
       d2 = int(monto / 500)
       monto = monto % 500
       if d2 >= b500:
         monto = monto + (d2 - b500) * 500
         d2 = b500
       d3 = int(monto / 100)
       monto = monto % 100  
       if d3 >= b100:
         monto = monto + (d3 - b100) * 100
         d3 = b100
       return [d1, d2, d3]


print ("Bienvenido al cajero ABC, por favor elegir el banco para su Transacción:  ")
print ("1. Banco ABC")
print ("2. Otros ")
select = input("> ")
select = int(select)


if select == 1:
  c = int(input("Ingrese el monto a retirar: "))
  if c <= 10000:
      res = retiro(c)
      print("Billetes de 1000: " , res[0])
      print("Billetes de 500: ", res[1])
      print("Billetes de 100: ", res[2]) 
  if c == 0:
      print ("Retiro nulo")
  if c >= 10000:
      print("El monto deseado excede el limite") 
  

if select == 2:
  c = int(input("Ingrese el monto a retirar: "))
  if c <= 2000:
      res = retiro(c)
      print("Billetes de 1000: " , res[0])
      print("Billetes de 500: ", res[1])
      print("Billetes de 100: ", res[2]) 
  if c == 0:
      print ("Retiro nulo")
  if c >= 2000:
      print("El monto deseado excede el limite")   