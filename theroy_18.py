
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
        print('DoB:     ' + self.birth)

    def getAddress(self):
        print('Address: ' + self.address)

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
        print('NI:      ' + self.ni)

one = Employee()
one.getName()
