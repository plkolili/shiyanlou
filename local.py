#!/usr/bin/env python3
#new try
def change():
    global a
    a=90
    print(a)
a=9
print("Before the function call",a)
print("inside change function",end=' ')
change()
print("After the function call",a)

