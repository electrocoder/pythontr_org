
#dosya okuma
import os

print os.listdir(os.getcwd())

hfile=open("1.py","r")
lines=hfile.readlines()
print lines
