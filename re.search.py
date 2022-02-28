#with find 
hand = open('mbox-short.txt')
for line in hand:
    if line find('From:') >= 0:
        print(line)

#with re.search
import re
hand = open('mbox-short.txt')
for line in hand:
   line = line.rstrip()
   if re.search('From:', line)
        print(line)