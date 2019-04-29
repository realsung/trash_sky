import random

print("Level 1")
for i in range(2, 101):
   a = random.randint(1, 100)
   b = random.randint(1, 100)
   c = random.choice(['+', '-', '*', '/'])
   if(a < b):
      while(1):
         a = random.randint(1, 100)
         b = random.randint(1, 100)
         if(a > b):
            break
         else:
            continue
   print(a, c, b)
   d = input()
   if(c == '+'):
      if(a + b == int(d)):
         print("Level :", i)
      else:
         print("Wrong Answer")
         break
   elif(c == '*'):
      if(a * b == int(d)):
         print("Level :", i)
      else:
         print("Wrong Answer")
         break
   elif(c == '/'):
      if(a / b == float(d)):
         print("Level :", i)
      else:
         print("Wrong Answer")
         break
   else:
      if(a - b == int(d)):
         print("Level :", i)
      else:
         print("Wrong Answer")
         break

if(i == 100):
   print("FLAG{Y0ur_C4n_Us3_Python}")