def addnumbers(n):
   number = 0
   for i in range(n):
      if i%3 == 0 or i%5 == 0:
         number = i + number
   print(number)
   


addnumbers(1000)