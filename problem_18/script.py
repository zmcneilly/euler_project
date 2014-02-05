#!env/bin/python

# Read in the triangle from an input file
fhandle = open("input.txt","r")
x = fhandle.readlines()
# Reverse and clean the triangle
t = []
for x1 in x[::-1]:
    t.append(x1.replace('\n','').split())

for x in t:
    print x

for x in range(1,len(t),1):
    for x1 in range(0,len(t[x]),1):
        s1 = int(t[x-1][x1])
        s2 = int(t[x-1][x1+1])
        if s1 > s2:
            t[x][x1] = int(t[x][x1])+s1
        else:
            t[x][x1] = int(t[x][x1])+s2
           
for x in t:
    print x

