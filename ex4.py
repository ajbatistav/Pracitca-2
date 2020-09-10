sueldo = input("Ingrese su sueldo: ")
sueldo = float(sueldo)
sueldo_anual = sueldo * 12
r_1 = 416220.00 #15%
r_2 = 624329.00 #20%
r_3 = 867123.00 #25%
ars = 0.0304
afp = 0.0287

def cal_1():
  ARS = sueldo_anual * ars
  AFP = sueldo_anual * afp
  print ("Usted paga ", ARS, " de ARS anualmente")
  print ("Usted paga ", AFP, " de AFP anualmente")


if sueldo_anual <= r_1:
  
  print("Usted esta exento del ISR")
  cal_1()

elif sueldo_anual <= r_2:
  calculo_r2 = sueldo_anual * 0.15
  print ("Usted paga ", calculo_r2, " de IRS")
  cal_1()

elif sueldo_anual <= r_3:
  calculo_r3 = (sueldo_anual * 0.20) + 31216.00
  print ("Usted paga ", calculo_r3, " de IRS")
  cal_1()

else:
  calculo_r4 = (sueldo_anual * 0.25) + 79776.00
  print ("Usted paga ", calculo_r4, " de IRS")
  cal_1()
