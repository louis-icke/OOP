
class Person():

    def __init__(self):
        self.name = input('Please input first name and last name:  ')
        self.birth = input('Please input date of birth:  ')
        self.address = input('Please input address:  ')

    def outputData(self):
        print('\nName:    ' + self.name)
        print('DoB:     ' + self.birth)
        print('Address: ' + self.address)

    def getName(self):
        print('\nName:    ' + self.name)

    def getBirth(self):
        print('\nDoB:     ' + self.birth)

    def getAddress(self):
        print('\nAddress: ' + self.address)

class Employee(Person):

    def __init__(self):
        self.name = input('Please input first name and last name:  ')
        self.birth = input('Please input date of birth:  ')
        self.address = input('Please input address:  ')
        self.ni = input('Please input National Insurance Number:  ')

    def outputData(self):
        print('\nName:    ' + self.name)
        print('DoB:     ' + self.birth)
        print('Address: ' + self.address)
        print('NI:      ' + self.ni)

    def getNi(self):
        print('\nNI:      ' + self.ni)

class HourlyPaidEmp(Employee):

    def __init__(self):
        self.name = input('Please input first name and last name:  ')
        self.birth = input('Please input date of birth:  ')
        self.address = input('Please input address:  ')
        self.ni = input('Please input National Insurance Number:  ')
        self.salary = int(input('Please input hourly salary:  '))
    
    def outputData(self):
        print('\nName:    ' + self.name)
        print('DoB:     ' + self.birth)
        print('Address: ' + self.address)
        print('NI:      ' + self.ni)
        print('Salary:  £' + self.salary + '/h')

    def getSalary(self):
        print('\nSalary:  £' + self.salary + '/h')
    
    def totalPaid(self,hours):
        total = self.salary * hours
        print('\nFor ' + str(hours) + ' hours, the employee is paid £' + str(total))

class SalariedEmp(Employee):

    def __init__(self):
        self.name = input('Please input first name and last name:  ')
        self.birth = input('Please input date of birth:  ')
        self.address = input('Please input address:  ')
        self.ni = input('Please input National Insurance Number:  ')
        self.salary = int(input('Please input yearly salary:  '))

    def outputData(self):
        print('\nName:    ' + self.name)
        print('DoB:     ' + self.birth)
        print('Address: ' + self.address)
        print('NI:      ' + self.ni)
        print('Salary:  £' + self.salary)

    def getSalary(self):
        print('\nSalary:  £' + self.salary)
    
    def getMonthly(self):
        month = self.salary / 12
        print('Each month the employee is paid £' + str(month))

one = SalariedEmp()
one.getMonthly()
