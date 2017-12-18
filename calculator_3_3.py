#!/user/bin/python

import sys

class ParameterError(BaseException):
    pass
class DateSave:
    shebao = {}
    stuff = []
    salary = []

class Config(object):
    def __init__(self, configfilename):  #
        self._config = {}
        self._configfilename = configfilename  #

    def get_config(self):
        with open(self._configfilename) as f:
            for line in f:
                listtmp = line.split('=')
                self._config[listtmp[0].strip()] = float(listtmp[1].strip())

        DateSave.shebao = self._config


class UserData(object):
    def __init__(self, userdatafilename):
        self._userdata = []
        self._userdatafilename = userdatafilename
        self._salary = []

    def get_userdata(self):
        with open(self._userdatafilename) as f:
            for line in f:
                listtmp = line.split(',')
                self._userdata.append([listtmp[0].strip(), listtmp[1].strip()])

        DateSave.stuff = self._userdata

    def calculator(self,stuff1): #此时么就传入进来了
        salary = float(stuff1[1])
        shebao = DateSave.shebao
        factor = (shebao['YangLao'] + shebao['YiLiao'] + shebao['GongShang'] + shebao['ShengYu'] + shebao['GongJiJin'])

        if shebao['JiShuL'] > salary:
            Insurance=shebao['JiShuL'] * factor
        elif shebao['JiShuH'] < salary:
            Insurance=shebao['JiShuH'] * factor
        else:
            Insurance=salary * factor

        b=salary-3500-Insurance
        if b <= 0:
            tax=0
        elif 0 < b <= 1500:
            tax=b * 0.03-0
        elif 1500 < b <= 4500:
            tax=b * 0.1-105
        elif 4500 < b <= 9000:
            tax=b * 0.2-555
        elif 9000 < b <= 35000:
            tax=b * 0.25-1005
        elif 35000 < b <= 55000:
            tax=b * 0.30-2755
        elif 55000 < b <= 80000:
            tax=b * 0.35-5505
        else:
            tax=b * 0.45-13505

        income=salary-tax-Insurance
        tax=format(tax, '.2f')
        Insurance = format(Insurance, '.2f')
        income = format(income, '.2f')


        stuff1.extend([Insurance, tax, income])
        self._salary.append(','.join(stuff1))

    def dumptofile(self,outfilename):
        with open(outfilename,'w') as f:
            for i in self._userdata:
                self.calculator(i)
            for j in self._salary:
                f.write(j)
                f.write('\n')

def main():
    args = sys.argv[1:]
    try:
        if len(args) != 6:
            raise ParameterError
        else:
            index = args.index('-c')
            configfilename = args[index + 1]
            config = Config('test.cfg')
            config.get_config()

            index = args.index('-d')
            userdatafilename = args[index + 1]
            userdata = UserData('user.csv')
            userdata.get_userdata()

            index = args.index('-o')
            outputfilename = args[index + 1]
            userdata.dumptofile('gongzi.csv')

    except (ParameterError, ValueError):
        print("Parameter Error")

if __name__ == '__main__':
    main()
