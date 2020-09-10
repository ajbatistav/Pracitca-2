c=1

for z in range(1000):
      factor = (z + 1)
      if factor%6 == 0:
     
         while c <= 12:
             res = z * c
             print (f"{z} X {c} = {res}")
             c += 1  
                 