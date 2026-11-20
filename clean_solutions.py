# OOPs is a programming paradigm(style) in which we organise our code around objects and classes rather than writing everything using separate variable and functions

# Name=
# Age =
# F. Name=
# M. Name =
# Contact No. =
# Add. =

name1='Rahul'
age1=23
course1='B.tech'

name2='Ashish'
age2=22
course2='BCA'

def display1():
  print(name1,age1,course1)
def display2():
  print(name2,age2,course2)

display1()
display2()

# Code is difficult to manage
# If any change comes up u have to make the change at multiple places
# data and functions are scattered

# A class is a blueprint that tells python what information and functionality an object should have.

# Syntax

# pass - is a placeholder

class ClassName:
  # Attributes
  # Methods
  pass


# Objects -> is the instance of the class (the real entity created by having a look at the class)

class Student:
  pass

# object creation
# Syntax -> VariableName=ClassName()

s1=Student()
s2=Student()
s3=Student()

# Adding data (attributes)

class Student:
  pass


s1=Student()
# objName.AttributName=value
s1.name='Neha'
s1.age=26
s1.course='BCA'

s2=Student()
s2.name='Vishal'
s2.age=24

print(s1.name)
print(s1.age)
print(s2.name)
print(s2.age)


print(s1.__dict__)
print(s2.__dict__)

# Python allows us to add attributes dynamically to objects, even if those attributes were never defined in the class

# Constructor (__init__) -> A constructor is a special function/method used  in a class that is automatically called whenever an object is created for the class

class abc:
  def __init__(self):
    print('Hello Students')


a=abc()

class Student:
  def __init__(self,name,age):
    self.name=name
    self.age=age


s1=Student('Vikas',23) #ClassName.__init__(objName,arguments)
s2=Student('Nisha',20)

print(s1.name)
print(s1.age)
print(s2.name)
print(s2.age)


# Python OOP Mastery - 50 Scenario Exercises


# Question 1

class Device:
    def __init__(self, id, temperature):
        self.id = id
        self.temperature = temperature

    def trigger(self):
        print(f"Device {self.id} trigger executed")


# Question 2

class Device:
    def __init__(self, id, temperature):
        self.id = id
        self.temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < 0:
            raise ValueError("Temperature cannot be negative")
        self._temperature = value


# Question 3

class Thermostat(Device):
    def __init__(self, id, temperature, special_flag):
        super().__init__(id, temperature)
        self.special_flag = special_flag


# Question 4

class Thermostat(Device):
    def __init__(self, id, temperature, special_flag):
        super().__init__(id, temperature)
        self.special_flag = special_flag

    def trigger(self):
        print(f"Thermostat {self.id} custom trigger executed")

def process_all(entities):
    for entity in entities:
        entity.trigger()


# Question 5

class Device:
    def __init__(self, id, temperature):
        self.id = id
        self.temperature = temperature

    def __str__(self):
        return f"Device {self.id}: {self.temperature}"

    def __gt__(self, other):
        return self.temperature > other.temperature


# Question 6

class Account:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance

    def process_trade(self):
        print(f"Account {self.id} process_trade executed")


# Question 7

class Account:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value


# Question 8

class MarginAccount(Account):
    def __init__(self, id, balance, special_flag):
        super().__init__(id, balance)
        self.special_flag = special_flag


# Question 9

class MarginAccount(Account):
    def __init__(self, id, balance, special_flag):
        super().__init__(id, balance)
        self.special_flag = special_flag

    def process_trade(self):
        print(f"MarginAccount {self.id} custom process_trade executed")

def process_all(entities):
    for entity in entities:
        entity.process_trade()


# Question 10

class Account:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance

    def __str__(self):
        return f"Account {self.id}: {self.balance}"

    def __gt__(self, other):
        return self.balance > other.balance


# Question 11

class Patient:
    def __init__(self, id, heart_rate):
        self.id = id
        self.heart_rate = heart_rate

    def update_vitals(self):
        print(f"Patient {self.id} update_vitals executed")


# Question 12

class Patient:
    def __init__(self, id, heart_rate):
        self.id = id
        self.heart_rate = heart_rate

    @property
    def heart_rate(self):
        return self._heart_rate

    @heart_rate.setter
    def heart_rate(self, value):
        if value < 0:
            raise ValueError("Heart_rate cannot be negative")
        self._heart_rate = value


# Question 13

class ICUPatient(Patient):
    def __init__(self, id, heart_rate, special_flag):
        super().__init__(id, heart_rate)
        self.special_flag = special_flag


# Question 14

class ICUPatient(Patient):
    def __init__(self, id, heart_rate, special_flag):
        super().__init__(id, heart_rate)
        self.special_flag = special_flag

    def update_vitals(self):
        print(f"ICUPatient {self.id} custom update_vitals executed")

def process_all(entities):
    for entity in entities:
        entity.update_vitals()


# Question 15

class Patient:
    def __init__(self, id, heart_rate):
        self.id = id
        self.heart_rate = heart_rate

    def __str__(self):
        return f"Patient {self.id}: {self.heart_rate}"

    def __gt__(self, other):
        return self.heart_rate > other.heart_rate


# Question 16

class Product:
    def __init__(self, id, price):
        self.id = id
        self.price = price

    def apply_discount(self):
        print(f"Product {self.id} apply_discount executed")


# Question 17

class Product:
    def __init__(self, id, price):
        self.id = id
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


# Question 18

class DigitalProduct(Product):
    def __init__(self, id, price, special_flag):
        super().__init__(id, price)
        self.special_flag = special_flag


# Question 19

class DigitalProduct(Product):
    def __init__(self, id, price, special_flag):
        super().__init__(id, price)
        self.special_flag = special_flag

    def apply_discount(self):
        print(f"DigitalProduct {self.id} custom apply_discount executed")

def process_all(entities):
    for entity in entities:
        entity.apply_discount()


# Question 20

class Product:
    def __init__(self, id, price):
        self.id = id
        self.price = price

    def __str__(self):
        return f"Product {self.id}: {self.price}"

    def __gt__(self, other):
        return self.price > other.price


# Question 21

class Robot:
    def __init__(self, id, battery_level):
        self.id = id
        self.battery_level = battery_level

    def move_item(self):
        print(f"Robot {self.id} move_item executed")


# Question 22

class Robot:
    def __init__(self, id, battery_level):
        self.id = id
        self.battery_level = battery_level

    @property
    def battery_level(self):
        return self._battery_level

    @battery_level.setter
    def battery_level(self, value):
        if value < 0:
            raise ValueError("Battery_level cannot be negative")
        self._battery_level = value


# Question 23

class DroneBot(Robot):
    def __init__(self, id, battery_level, special_flag):
        super().__init__(id, battery_level)
        self.special_flag = special_flag


# Question 24

class DroneBot(Robot):
    def __init__(self, id, battery_level, special_flag):
        super().__init__(id, battery_level)
        self.special_flag = special_flag

    def move_item(self):
        print(f"DroneBot {self.id} custom move_item executed")

def process_all(entities):
    for entity in entities:
        entity.move_item()


# Question 25

class Robot:
    def __init__(self, id, battery_level):
        self.id = id
        self.battery_level = battery_level

    def __str__(self):
        return f"Robot {self.id}: {self.battery_level}"

    def __gt__(self, other):
        return self.battery_level > other.battery_level


# Question 26

class Media:
    def __init__(self, id, bitrate):
        self.id = id
        self.bitrate = bitrate

    def buffer_data(self):
        print(f"Media {self.id} buffer_data executed")


# Question 27

class Media:
    def __init__(self, id, bitrate):
        self.id = id
        self.bitrate = bitrate

    @property
    def bitrate(self):
        return self._bitrate

    @bitrate.setter
    def bitrate(self, value):
        if value < 0:
            raise ValueError("Bitrate cannot be negative")
        self._bitrate = value


# Question 28

class LiveStream(Media):
    def __init__(self, id, bitrate, special_flag):
        super().__init__(id, bitrate)
        self.special_flag = special_flag


# Question 29

class LiveStream(Media):
    def __init__(self, id, bitrate, special_flag):
        super().__init__(id, bitrate)
        self.special_flag = special_flag

    def buffer_data(self):
        print(f"LiveStream {self.id} custom buffer_data executed")

def process_all(entities):
    for entity in entities:
        entity.buffer_data()


# Question 30

class Media:
    def __init__(self, id, bitrate):
        self.id = id
        self.bitrate = bitrate

    def __str__(self):
        return f"Media {self.id}: {self.bitrate}"

    def __gt__(self, other):
        return self.bitrate > other.bitrate


# Question 31

class Driver:
    def __init__(self, id, rating):
        self.id = id
        self.rating = rating

    def accept_ride(self):
        print(f"Driver {self.id} accept_ride executed")


# Question 32

class Driver:
    def __init__(self, id, rating):
        self.id = id
        self.rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if value < 0:
            raise ValueError("Rating cannot be negative")
        self._rating = value


# Question 33

class PremiumDriver(Driver):
    def __init__(self, id, rating, special_flag):
        super().__init__(id, rating)
        self.special_flag = special_flag


# Question 34

class PremiumDriver(Driver):
    def __init__(self, id, rating, special_flag):
        super().__init__(id, rating)
        self.special_flag = special_flag

    def accept_ride(self):
        print(f"PremiumDriver {self.id} custom accept_ride executed")

def process_all(entities):
    for entity in entities:
        entity.accept_ride()


# Question 35

class Driver:
    def __init__(self, id, rating):
        self.id = id
        self.rating = rating

    def __str__(self):
        return f"Driver {self.id}: {self.rating}"

    def __gt__(self, other):
        return self.rating > other.rating


# Question 36

class User:
    def __init__(self, id, follower_count):
        self.id = id
        self.follower_count = follower_count

    def post_update(self):
        print(f"User {self.id} post_update executed")


# Question 37

class User:
    def __init__(self, id, follower_count):
        self.id = id
        self.follower_count = follower_count

    @property
    def follower_count(self):
        return self._follower_count

    @follower_count.setter
    def follower_count(self, value):
        if value < 0:
            raise ValueError("Follower_count cannot be negative")
        self._follower_count = value


# Question 38

class VerifiedUser(User):
    def __init__(self, id, follower_count, special_flag):
        super().__init__(id, follower_count)
        self.special_flag = special_flag


# Question 39

class VerifiedUser(User):
    def __init__(self, id, follower_count, special_flag):
        super().__init__(id, follower_count)
        self.special_flag = special_flag

    def post_update(self):
        print(f"VerifiedUser {self.id} custom post_update executed")

def process_all(entities):
    for entity in entities:
        entity.post_update()


# Question 40

class User:
    def __init__(self, id, follower_count):
        self.id = id
        self.follower_count = follower_count

    def __str__(self):
        return f"User {self.id}: {self.follower_count}"

    def __gt__(self, other):
        return self.follower_count > other.follower_count


# Question 41

class Server:
    def __init__(self, id, cpu_load):
        self.id = id
        self.cpu_load = cpu_load

    def allocate_ram(self):
        print(f"Server {self.id} allocate_ram executed")


# Question 42

class Server:
    def __init__(self, id, cpu_load):
        self.id = id
        self.cpu_load = cpu_load

    @property
    def cpu_load(self):
        return self._cpu_load

    @cpu_load.setter
    def cpu_load(self, value):
        if value < 0:
            raise ValueError("Cpu_load cannot be negative")
        self._cpu_load = value


# Question 43

class DatabaseServer(Server):
    def __init__(self, id, cpu_load, special_flag):
        super().__init__(id, cpu_load)
        self.special_flag = special_flag


# Question 44

class DatabaseServer(Server):
    def __init__(self, id, cpu_load, special_flag):
        super().__init__(id, cpu_load)
        self.special_flag = special_flag

    def allocate_ram(self):
        print(f"DatabaseServer {self.id} custom allocate_ram executed")

def process_all(entities):
    for entity in entities:
        entity.allocate_ram()


# Question 45

class Server:
    def __init__(self, id, cpu_load):
        self.id = id
        self.cpu_load = cpu_load

    def __str__(self):
        return f"Server {self.id}: {self.cpu_load}"

    def __gt__(self, other):
        return self.cpu_load > other.cpu_load


# Question 46

class Character:
    def __init__(self, id, mana_points):
        self.id = id
        self.mana_points = mana_points

    def cast_spell(self):
        print(f"Character {self.id} cast_spell executed")


# Question 47

class Character:
    def __init__(self, id, mana_points):
        self.id = id
        self.mana_points = mana_points

    @property
    def mana_points(self):
        return self._mana_points

    @mana_points.setter
    def mana_points(self, value):
        if value < 0:
            raise ValueError("Mana_points cannot be negative")
        self._mana_points = value


# Question 48

class Mage(Character):
    def __init__(self, id, mana_points, special_flag):
        super().__init__(id, mana_points)
        self.special_flag = special_flag


# Question 49

class Mage(Character):
    def __init__(self, id, mana_points, special_flag):
        super().__init__(id, mana_points)
        self.special_flag = special_flag

    def cast_spell(self):
        print(f"Mage {self.id} custom cast_spell executed")

def process_all(entities):
    for entity in entities:
        entity.cast_spell()


# Question 50

class Character:
    def __init__(self, id, mana_points):
        self.id = id
        self.mana_points = mana_points

    def __str__(self):
        return f"Character {self.id}: {self.mana_points}"

    def __gt__(self, other):
        return self.mana_points > other.mana_points


# Intermediate OOP Scenarios - 50 Industry Challenges


# Challenge 1

class Product:
    def __init__(self, sku, price=0):
        self.sku = sku
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


# Challenge 2

class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

class MarginAccount(Account):
    def __init__(self, account_id, balance, special_flag):
        super().__init__(account_id, balance)
        self.special_flag = special_flag


# Challenge 3

from abc import ABC, abstractmethod

class Patient(ABC):
    @abstractmethod
    def record_vitals(self):
        pass

class ICUPatient(Patient):
    def record_vitals(self):
        return "Vitals recorded for ICU Patient"


# Challenge 4

class Device:
    def __init__(self, mac_address, temperature):
        self.mac_address = mac_address
        self.temperature = temperature

    @staticmethod
    def validate_mac_address(mac_address):
        return len(str(mac_address)) > 3

    @classmethod
    def from_string(cls, data_str):
        attr2, attr1 = data_str.split("-")
        return cls(attr1, attr2)


# Challenge 5

class Shipment:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return f"Shipment: [{self.weight}]"

    def __add__(self, other):
        return self.weight + other.weight

    def __gt__(self, other):
        return self.weight > other.weight


# Challenge 6

class Post:
    def __init__(self, post_id, likes=0):
        self.post_id = post_id
        self.likes = likes

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, value):
        if value < 0:
            raise ValueError("Likes cannot be negative")
        self._likes = value


# Challenge 7

class Course:
    def __init__(self, course_code, enrollment):
        self.course_code = course_code
        self.enrollment = enrollment

class Bootcamp(Course):
    def __init__(self, course_code, enrollment, special_flag):
        super().__init__(course_code, enrollment)
        self.special_flag = special_flag


# Challenge 8

from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def take_damage(self):
        pass

class BossCharacter(Character):
    def take_damage(self):
        return "Damage applied to boss"


# Challenge 9

class Server:
    def __init__(self, ip_address, cpu_load):
        self.ip_address = ip_address
        self.cpu_load = cpu_load

    @staticmethod
    def validate_ip_address(ip_address):
        return len(str(ip_address)) > 3

    @classmethod
    def from_string(cls, data_str):
        attr2, attr1 = data_str.split("-")
        return cls(attr1, attr2)


# Challenge 10

class Flight:
    def __init__(self, flight_number, seats_available):
        self.flight_number = flight_number
        self.seats_available = seats_available

    def __str__(self):
        return f"Flight: [{self.seats_available}]"

    def __add__(self, other):
        return self.seats_available + other.seats_available

    def __gt__(self, other):
        return self.seats_available > other.seats_available


# Challenge 11

class Product:
    def __init__(self, sku, price=0):
        self.sku = sku
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


# Challenge 12

class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

class MarginAccount(Account):
    def __init__(self, account_id, balance, special_flag):
        super().__init__(account_id, balance)
        self.special_flag = special_flag


# Challenge 13

from abc import ABC, abstractmethod

class Patient(ABC):
    @abstractmethod
    def record_vitals(self):
        pass

class ICUPatient(Patient):
    def record_vitals(self):
        return "Vitals recorded for ICU Patient"


# Challenge 14

class Device:
    def __init__(self, mac_address, temperature):
        self.mac_address = mac_address
        self.temperature = temperature

    @staticmethod
    def validate_mac_address(mac_address):
        return len(str(mac_address)) > 3

    @classmethod
    def from_string(cls, data_str):
        attr2, attr1 = data_str.split("-")
        return cls(attr1, attr2)


# Challenge 15

class Shipment:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return f"Shipment: [{self.weight}]"

    def __add__(self, other):
        return self.weight + other.weight

    def __gt__(self, other):
        return self.weight > other.weight


# Challenge 16

class Post:
    def __init__(self, post_id, likes=0):
        self.post_id = post_id
        self.likes = likes

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, value):
        if value < 0:
            raise ValueError("Likes cannot be negative")
        self._likes = value


# Challenge 17

class Course:
    def __init__(self, course_code, enrollment):
        self.course_code = course_code
        self.enrollment = enrollment

class Bootcamp(Course):
    def __init__(self, course_code, enrollment, special_flag):
        super().__init__(course_code, enrollment)
        self.special_flag = special_flag


# Challenge 18

from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def take_damage(self):
        pass

class BossCharacter(Character):
    def take_damage(self):
        return "Damage applied to boss"


# Challenge 19

class Server:
    def __init__(self, ip_address, cpu_load):
        self.ip_address = ip_address
        self.cpu_load = cpu_load

    @staticmethod
    def validate_ip_address(ip_address):
        return len(str(ip_address)) > 3

    @classmethod
    def from_string(cls, data_str):
        attr2, attr1 = data_str.split("-")
        return cls(attr1, attr2)


# Challenge 20

class Flight:
    def __init__(self, flight_number, seats_available):
        self.flight_number = flight_number
        self.seats_available = seats_available

    def __str__(self):
        return f"Flight: [{self.seats_available}]"

    def __add__(self, other):
        return self.seats_available + other.seats_available

    def __gt__(self, other):
        return self.seats_available > other.seats_available


# Challenge 21

class Product:
    def __init__(self, sku, price=0):
        self.sku = sku
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


# Challenge 22

class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

class MarginAccount(Account):
    def __init__(self, account_id, balance, special_flag):
        super().__init__(account_id, balance)
        self.special_flag = special_flag


# Challenge 23

from abc import ABC, abstractmethod

class Patient(ABC):
    @abstractmethod
    def record_vitals(self):
        pass

class ICUPatient(Patient):
    def record_vitals(self):
        return "Vitals recorded for ICU Patient"


# Challenge 24

class Device:
    def __init__(self, mac_address, temperature):
        self.mac_address = mac_address
        self.temperature = temperature

    @staticmethod
    def validate_mac_address(mac_address):
        return len(str(mac_address)) > 3

    @classmethod
    def from_string(cls, data_str):
        attr2, attr1 = data_str.split("-")
        return cls(attr1, attr2)


# Challenge 25

class Shipment:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return f"Shipment: [{self.weight}]"

    def __add__(self, other):
        return self.weight + other.weight

    def __gt__(self, other):
        return self.weight > other.weight


# Challenge 26

class Post:
    def __init__(self, post_id, likes=0):
        self.post_id = post_id
        self.likes = likes

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, value):
        if value < 0:
            raise ValueError("Likes cannot be negative")
        self._likes = value


# Challenge 27

class Course:
    def __init__(self, course_code, enrollment):
        self.course_code = course_code
        self.enrollment = enrollment

class Bootcamp(Course):
    def __init__(self, course_code, enrollment, special_flag):
        super().__init__(course_code, enrollment)
        self.special_flag = special_flag


# Challenge 28

from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def take_damage(self):
        pass

class BossCharacter(Character):
    def take_damage(self):
        return "Damage applied to boss"


# Challenge 29

class Server:
    def __init__(self, ip_address, cpu_load):
        self.ip_address = ip_address
        self.cpu_load = cpu_load

    @staticmethod
    def validate_ip_address(ip_address):
        return len(str(ip_address)) > 3

    @classmethod
    def from_string(cls, data_str):
        attr2, attr1 = data_str.split("-")
        return cls(attr1, attr2)


# Challenge 30

class Flight:
    def __init__(self, flight_number, seats_available):
        self.flight_number = flight_number
        self.seats_available = seats_available

    def __str__(self):
        return f"Flight: [{self.seats_available}]"

    def __add__(self, other):
        return self.seats_available + other.seats_available

    def __gt__(self, other):
        return self.seats_available > other.seats_available


# Challenge 31

class Product:
    def __init__(self, sku, price=0):
        self.sku = sku
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


# Challenge 32

class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

class MarginAccount(Account):
    def __init__(self, account_id, balance, special_flag):
        super().__init__(account_id, balance)
        self.special_flag = special_flag


# Challenge 33

from abc import ABC, abstractmethod

class Patient(ABC):
    @abstractmethod
    def record_vitals(self):
        pass

class ICUPatient(Patient):
    def record_vitals(self):
        return "Vitals recorded for ICU Patient"


# Challenge 34

class Device:
    def __init__(self, mac_address, temperature):
        self.mac_address = mac_address
        self.temperature = temperature

    @staticmethod
    def validate_mac_address(mac_address):
        return len(str(mac_address)) > 3

    @classmethod
    def from_string(cls, data_str):
        attr2, attr1 = data_str.split("-")
        return cls(attr1, attr2)


# Challenge 35

class Shipment:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return f"Shipment: [{self.weight}]"

    def __add__(self, other):
        return self.weight + other.weight

    def __gt__(self, other):
        return self.weight > other.weight


# Challenge 36

class Post:
    def __init__(self, post_id, likes=0):
        self.post_id = post_id
        self.likes = likes

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, value):
        if value < 0:
            raise ValueError("Likes cannot be negative")
        self._likes = value


# Challenge 37

class Course:
    def __init__(self, course_code, enrollment):
        self.course_code = course_code
        self.enrollment = enrollment

class Bootcamp(Course):
    def __init__(self, course_code, enrollment, special_flag):
        super().__init__(course_code, enrollment)
        self.special_flag = special_flag


# Challenge 38

from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def take_damage(self):
        pass

class BossCharacter(Character):
    def take_damage(self):
        return "Damage applied to boss"


# Challenge 39

class Server:
    def __init__(self, ip_address, cpu_load):
        self.ip_address = ip_address
        self.cpu_load = cpu_load

    @staticmethod
    def validate_ip_address(ip_address):
        return len(str(ip_address)) > 3

    @classmethod
    def from_string(cls, data_str):
        attr2, attr1 = data_str.split("-")
        return cls(attr1, attr2)


# Challenge 40

class Flight:
    def __init__(self, flight_number, seats_available):
        self.flight_number = flight_number
        self.seats_available = seats_available

    def __str__(self):
        return f"Flight: [{self.seats_available}]"

    def __add__(self, other):
        return self.seats_available + other.seats_available

    def __gt__(self, other):
        return self.seats_available > other.seats_available


# Challenge 41

class Product:
    def __init__(self, sku, price=0):
        self.sku = sku
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


# Challenge 42

class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

class MarginAccount(Account):
    def __init__(self, account_id, balance, special_flag):
        super().__init__(account_id, balance)
        self.special_flag = special_flag


# Challenge 43

from abc import ABC, abstractmethod

class Patient(ABC):
    @abstractmethod
    def record_vitals(self):
        pass

class ICUPatient(Patient):
    def record_vitals(self):
        return "Vitals recorded for ICU Patient"


# Challenge 44

class Device:
    def __init__(self, mac_address, temperature):
        self.mac_address = mac_address
        self.temperature = temperature

    @staticmethod
    def validate_mac_address(mac_address):
        return len(str(mac_address)) > 3

    @classmethod
    def from_string(cls, data_str):
        attr2, attr1 = data_str.split("-")
        return cls(attr1, attr2)


# Challenge 45

class Shipment:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return f"Shipment: [{self.weight}]"

    def __add__(self, other):
        return self.weight + other.weight

    def __gt__(self, other):
        return self.weight > other.weight


# Challenge 46

class Post:
    def __init__(self, post_id, likes=0):
        self.post_id = post_id
        self.likes = likes

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, value):
        if value < 0:
            raise ValueError("Likes cannot be negative")
        self._likes = value


# Challenge 47

class Course:
    def __init__(self, course_code, enrollment):
        self.course_code = course_code
        self.enrollment = enrollment

class Bootcamp(Course):
    def __init__(self, course_code, enrollment, special_flag):
        super().__init__(course_code, enrollment)
        self.special_flag = special_flag


# Challenge 48

from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def take_damage(self):
        pass

class BossCharacter(Character):
    def take_damage(self):
        return "Damage applied to boss"


# Challenge 49

class Server:
    def __init__(self, ip_address, cpu_load):
        self.ip_address = ip_address
        self.cpu_load = cpu_load

    @staticmethod
    def validate_ip_address(ip_address):
        return len(str(ip_address)) > 3

    @classmethod
    def from_string(cls, data_str):
        attr2, attr1 = data_str.split("-")
        return cls(attr1, attr2)


# Challenge 50

class Flight:
    def __init__(self, flight_number, seats_available):
        self.flight_number = flight_number
        self.seats_available = seats_available

    def __str__(self):
        return f"Flight: [{self.seats_available}]"

    def __add__(self, other):
        return self.seats_available + other.seats_available

    def __gt__(self, other):
        return self.seats_available > other.seats_available
