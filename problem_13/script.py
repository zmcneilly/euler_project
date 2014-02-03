#!env/bin/python

total = 0
with open ("input.txt","r") as fhandle:
    for data in fhandle.readlines():
        total += int(data)

print total
