import random
import string

level = 1

while(1):
   if(level == 101):
      print 'Oh you know how to use hex encoding and decoding!! Here is a flag FLAG{Man_is_JAVA}'
      break
   print 'Level : ', level
   a = random.randint(1,2)
   if(a == 1):
      ran = ''.join(random.choice(string.uppercase + string.lowercase) for i in range(random.randrange(100)))
      print 'Please encode this', ran
      re = ran.encode("hex")
      if(raw_input() == re):
         print 'Congratulation!!'
         level += 1
      else:
         print 'Your Wrong!!'
         break
   else:
      ran = ''.join(random.choice(string.uppercase + string.lowercase) for i in range(random.randrange(100))).encode('hex')
      print 'Please decode this', ran
      re = ran
      if len(re)&1:re='0'+re
      re = re.decode('hex')
      if(raw_input() == re):
         print 'Congratulation!!'
         level += 1
      else:
         print 'Yout Wrong!!'
         break

