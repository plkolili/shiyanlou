#!/usr/bin/env python3
import sys
def  get_tax(employee):
#字典的拷贝
    for key,value in employee.items():    #遍历字典的内容
        b=value-value*0.165-3500
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
        employee[key]=value-value*0.165-c #更新字典的值
        return employee #return dictionary


    
employee={}      #建立空字典
print(sys.argv[1:])
args=sys.argv[1:]
index=args.index('-c')
filename1=index,args[index+1])
index=args.index('-d')
filename2=index,args[index+1])
index=args.index('-o')
filename3=index,args[index+1])
for s in sys.argv[1:]:
    data=s.split(':')
    employee[data[0]]=int(data[1]) #初始字典数据, like input
employee=get_tax(employee)  #执行函数的过程,得到一个新的字典
for key,value in employee.items():
    print (key+':'+str(format(value,'.2f')))



		
class Config(object)
    def __init__(self,configfile)
        self._configfile={}
     		
class UserData(object)   		
    def __init__(self,userdatafile)
        self.userdata={}
    def calculator(self)
        open(filename1)
        filename.readlines()
        get_tax(filename.readlines())
    def dumptofile(self,outputfile)
        filename.write('employee_tax')

		
		
