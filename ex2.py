def menu():
  print("Bienvenido por favor seleccione una de las sigueintes opciones")
  print("1- Convertir grados Celsius a Fahrenheit")
  print("2- Convertir dolar a pesos")
  print("3- Convertir metros a pies")
  print("4- Salir") 
 

menu()
select = input("> ")
select = int(select)


while select != 4:
  if select == 1:
      celsius = input("Introduzca temperatura en celcius: ")
      celsius = float(celsius)
      res = celsius * 9/5 + 32
      print (str(res) + " Grados Fahrenheit")
      
      menu()
      select = input("> ")
      select = int(select)
  elif select == 2:
       dolares = input("Introduzca cantidad de dolares: ")
       dolares = float(dolares)
       tasa = 58.45 
       pesos = dolares * tasa
       print(str(dolares) + "$US equivale a " + str(pesos) + "$RD")

   
       menu()
       select = input("> ")
       select = int(select)
  elif select == 3:
      metros = input("Introduzca la cantidad en metros: ")
      metros = float(metros)
      factor = 3.28
      pies = metros * factor
      print (metros, "m = ", pies, "pies")

      
      menu()
      select = input("> ")
      select = int(select)
  elif select >= 4:
      print("La opcion seleccionada no se encuentra en el menu")
      print("por favor, seleccione una de las siguientes opciones")

     
      menu()
      select = input("> ")
      select = int(select)
if  select == 4:
     print("Gracias por utilizar el programa")   