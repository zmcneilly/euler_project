#!env/bin/python

MAX=1000
FACTOR=[3,5]
DUPES=[]
i = 0
while i < (len(FACTOR) - 1):
   DUPES.append(FACTOR[i] * FACTOR[i+1])
   i += 1

total = 0
for x in FACTOR:
  i = 0
  while (i*x < MAX):
    total += i*x
    i += 1

for x in DUPES:
  i = 0
  while (i*x < MAX):
    total -= i*x
    i += 1 

print total
