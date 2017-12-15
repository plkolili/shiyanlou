#!/usr/bin/env python3
import sys

for arg in sys.argv[1:]:
    spl=arg.split(':')
    a=int(spl[1])
    number=int(spl[0])
   

#    print("enter interger")
#if __name__=='__main__':
    
    b=a-a*0.165-3500

    if b<=0:
        c=0
    elif 0<b<=1500:
        c=b*0.03-0
    elif 1500<b<=4500:
        c=b*0.1-105
    elif 4500<b<=9000:
        c=b*0.2-555
    elif 9000<b<=35000:
        c=b*0.25-1005
    elif 35000<b<=55000:
        c=b*0.30-2755
    elif 55000<b<=80000:
        c=b*0.35-5505
    else:
        c=b*0.45-13505
#    print(number,':')

print（number，format（C,format(a-c-a*0.165,".2f"),sep=':')
