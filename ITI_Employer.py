import re


class Person():
    moods = ('happy','tired','lazy')
    def __init__(self , name , money):
        self.name = name
        self.money = money
        self.mood = ''
        self.healthRate=0

    @property
    def healthRate(self):
        return self.__healthRate

    @healthRate.setter
    def healthRate(self, value):
        if (value < 0 or value > 100) :
            raise ValueError("HealthRate must be between 0 and 100")
        self.__healthRate = value

    def sleep(self , hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        elif hours > 7:
            self.mood ="lazy"
        else:
            self.mood = ""
        
    
    def eat(self , meals):
        if meals == 3:
            self.healthRate = 100
        elif meals ==2 :
            self.healthRate = 75
        elif meals == 1 :
            self.healthRate = 50
        else:
            self.healthRate = 0

    def buy(self , items):
        if (self.money -0.1*items > 0):
            self.money -= 0.1*items
    
    def work(self , hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        elif hours < 8:
            self.mood ="lazy"
        else:
            self.mood = ""


class Employee(Person):
    def __init__(self, name, money,id,emailAddress):
        super().__init__(name, money)
        self.id = id
        self.car = ""
        self.email = emailAddress
        self.salary =1000
        self.distanceToWork=0

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if (value < 1000) :
            raise ValueError("Salary must be 1000 or more")
        self.__salary = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self , emailAdd):
        mail=r'\b[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not (re.fullmatch(mail,emailAdd)):
            raise ValueError("email address must be valid")
        self.__email = emailAdd


class Office():
    def __init__(self,name):
        self.name = name
        self.employees =[]


    def get_all_employees(self):
        return self.employees

    def get_employee(self):
        pass

    def hire(self):
        pass

    def fire(self):
        pass

    def calcualte_lateness(self):
        pass

    def deduct(self):
        pass

    def reward(self):
        pass



class Car():
    def __init__(self , name , fuelrate , velocity):
        self.name = name
        self.fuelRate = fuelrate
        self.velocity = velocity

    def run(self):
        pass

    def stop(self):
        pass



e = Employee('Ahmed',1000,1,'zozo@gmail')
e.salary=99999


    