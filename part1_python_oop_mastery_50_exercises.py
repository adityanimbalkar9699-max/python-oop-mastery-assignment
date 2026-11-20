# ---
# # Part 1: Python OOP Mastery (50 Scenario-Based Exercises)
# Based on **Python OOP Mastery: 50 Scenario-Based Exercises Question Workbook**.
# Divided across 10 Real-World Domains covering:
# 1. Classes and Objects
# 2. Encapsulation & Properties
# 3. Inheritance & `super()`
# 4. Polymorphism
# 5. Magic Methods (`__str__`, `__gt__`)
# ---

# ### Question 1: Classes and Objects (Beginner) - Smart Home Hub
# **Scenario:** In the Smart Home Hub project, the team needs to represent the core entity: `Device`.
# **Task:** Create a basic `Device` class initializing with `id` and `temperature`. Add a method `trigger()` that prints a status message.

class Device:
    def __init__(self, id, temperature):
        self.id = id
        self.temperature = temperature

    def trigger(self):
        print(f"[Device {self.id}] Device triggered and functioning.")

# Test Question 1
obj_1 = Device(101, 50)
obj_1.trigger()


# ### Question 2: Encapsulation & Properties (Intermediate) - Smart Home Hub
# **Scenario:** Security audits revealed `temperature` was being altered maliciously or accidentally.
# **Task:** Modify `Device` to make `temperature` private (`_temperature`). Provide a property getter and setter that raises `ValueError` if negative.

class DeviceEncapsulated:
    def __init__(self, id, temperature):
        self.id = id
        self.temperature = temperature  # Triggers the property setter

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < 0:
            raise ValueError(f"'temperature' cannot be negative: {value}")
        self._temperature = value

# Test Question 2
enc_2 = DeviceEncapsulated(102, 75)
print(f"Valid temperature: {enc_2.temperature}")
try:
    enc_2.temperature = -10
except ValueError as e:
    print(f"Caught expected error: {e}")


# ### Question 3: Inheritance (Intermediate) - Smart Home Hub
# **Scenario:** The platform is expanding. Standard `Device` objects aren't enough. We need specialized behaviors for `Thermostat`.
# **Task:** Create subclass `Thermostat` that inherits from `Device`. Add attribute `special_flag` and override `__init__` using `super()`.

class Thermostat(Device):
    def __init__(self, id, temperature, special_flag):
        super().__init__(id, temperature)
        self.special_flag = special_flag

# Test Question 3
sub_obj_3 = Thermostat(103, 80, special_flag=True)
print(f"Created Thermostat: ID={sub_obj_3.id}, temperature={sub_obj_3.temperature}, special_flag={sub_obj_3.special_flag}")


# ### Question 4: Polymorphism (Industry) - Smart Home Hub
# **Scenario:** An orchestrator module needs to process a list of different `Device` types seamlessly.
# **Task:** Override `trigger()` in `Thermostat` to implement custom behavior. Write `process_all(entities)` that accepts a list and triggers `trigger()` on all.

class ThermostatPolymorphic(Device):
    def __init__(self, id, temperature, special_flag):
        super().__init__(id, temperature)
        self.special_flag = special_flag

    def trigger(self):
        print(f"[Thermostat {self.id} | Flag: {self.special_flag}] Thermostat adjusting temperature regulation.")

def process_all_smart_home_hub(entities):
    for entity in entities:
        entity.trigger()

# Test Question 4
sample_list_4 = [
    Device(101, 40),
    ThermostatPolymorphic(102, 60, special_flag=True)
]
process_all_smart_home_hub(sample_list_4)


# ### Question 5: Magic Methods (Industry) - Smart Home Hub
# **Scenario:** Logs are cluttered with memory addresses. Devops needs readable logging, and analysts want to compare performance based on `temperature`.
# **Task:** Implement `__str__` for `Device` to return a readable string, and `__gt__` to compare two objects based on `temperature`.

class DeviceComplete(Device):
    def __str__(self):
        return f"Device(id={self.id}, temperature={self.temperature})"

    def __gt__(self, other):
        if not isinstance(other, Device):
            return NotImplemented
        return self.temperature > other.temperature

# Test Question 5
item_a_5 = DeviceComplete(1, 45)
item_b_5 = DeviceComplete(2, 85)

print("Readable String representation:", str(item_a_5))
print(f"Is Item B > Item A? {item_b_5 > item_a_5}")


# ### Question 6: Classes and Objects (Beginner) - FinTech Engine
# **Scenario:** In the FinTech Engine project, the team needs to represent the core entity: `Account`.
# **Task:** Create a basic `Account` class initializing with `id` and `balance`. Add a method `process_trade()` that prints a status message.

class Account:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance

    def process_trade(self):
        print(f"[Account {self.id}] Trade processed successfully.")

# Test Question 6
obj_6 = Account(101, 50)
obj_6.process_trade()


# ### Question 7: Encapsulation & Properties (Intermediate) - FinTech Engine
# **Scenario:** Security audits revealed `balance` was being altered maliciously or accidentally.
# **Task:** Modify `Account` to make `balance` private (`_balance`). Provide a property getter and setter that raises `ValueError` if negative.

class AccountEncapsulated:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance  # Triggers the property setter

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError(f"'balance' cannot be negative: {value}")
        self._balance = value

# Test Question 7
enc_7 = AccountEncapsulated(102, 75)
print(f"Valid balance: {enc_7.balance}")
try:
    enc_7.balance = -10
except ValueError as e:
    print(f"Caught expected error: {e}")


# ### Question 8: Inheritance (Intermediate) - FinTech Engine
# **Scenario:** The platform is expanding. Standard `Account` objects aren't enough. We need specialized behaviors for `MarginAccount`.
# **Task:** Create subclass `MarginAccount` that inherits from `Account`. Add attribute `special_flag` and override `__init__` using `super()`.

class MarginAccount(Account):
    def __init__(self, id, balance, special_flag):
        super().__init__(id, balance)
        self.special_flag = special_flag

# Test Question 8
sub_obj_8 = MarginAccount(103, 80, special_flag=True)
print(f"Created MarginAccount: ID={sub_obj_8.id}, balance={sub_obj_8.balance}, special_flag={sub_obj_8.special_flag}")


# ### Question 9: Polymorphism (Industry) - FinTech Engine
# **Scenario:** An orchestrator module needs to process a list of different `Account` types seamlessly.
# **Task:** Override `process_trade()` in `MarginAccount` to implement custom behavior. Write `process_all(entities)` that accepts a list and triggers `process_trade()` on all.

class MarginAccountPolymorphic(Account):
    def __init__(self, id, balance, special_flag):
        super().__init__(id, balance)
        self.special_flag = special_flag

    def process_trade(self):
        print(f"[MarginAccount {self.id} | Flag: {self.special_flag}] Margin trade executed with collateral verification.")

def process_all_fintech_engine(entities):
    for entity in entities:
        entity.process_trade()

# Test Question 9
sample_list_9 = [
    Account(101, 40),
    MarginAccountPolymorphic(102, 60, special_flag=True)
]
process_all_fintech_engine(sample_list_9)


# ### Question 10: Magic Methods (Industry) - FinTech Engine
# **Scenario:** Logs are cluttered with memory addresses. Devops needs readable logging, and analysts want to compare performance based on `balance`.
# **Task:** Implement `__str__` for `Account` to return a readable string, and `__gt__` to compare two objects based on `balance`.

class AccountComplete(Account):
    def __str__(self):
        return f"Account(id={self.id}, balance={self.balance})"

    def __gt__(self, other):
        if not isinstance(other, Account):
            return NotImplemented
        return self.balance > other.balance

# Test Question 10
item_a_10 = AccountComplete(1, 45)
item_b_10 = AccountComplete(2, 85)

print("Readable String representation:", str(item_a_10))
print(f"Is Item B > Item A? {item_b_10 > item_a_10}")


# ### Question 11: Classes and Objects (Beginner) - Health Portal
# **Scenario:** In the Health Portal project, the team needs to represent the core entity: `Patient`.
# **Task:** Create a basic `Patient` class initializing with `id` and `heart_rate`. Add a method `update_vitals()` that prints a status message.

class Patient:
    def __init__(self, id, heart_rate):
        self.id = id
        self.heart_rate = heart_rate

    def update_vitals(self):
        print(f"[Patient {self.id}] Patient vitals updated in portal.")

# Test Question 11
obj_11 = Patient(101, 50)
obj_11.update_vitals()


# ### Question 12: Encapsulation & Properties (Intermediate) - Health Portal
# **Scenario:** Security audits revealed `heart_rate` was being altered maliciously or accidentally.
# **Task:** Modify `Patient` to make `heart_rate` private (`_heart_rate`). Provide a property getter and setter that raises `ValueError` if negative.

class PatientEncapsulated:
    def __init__(self, id, heart_rate):
        self.id = id
        self.heart_rate = heart_rate  # Triggers the property setter

    @property
    def heart_rate(self):
        return self._heart_rate

    @heart_rate.setter
    def heart_rate(self, value):
        if value < 0:
            raise ValueError(f"'heart_rate' cannot be negative: {value}")
        self._heart_rate = value

# Test Question 12
enc_12 = PatientEncapsulated(102, 75)
print(f"Valid heart_rate: {enc_12.heart_rate}")
try:
    enc_12.heart_rate = -10
except ValueError as e:
    print(f"Caught expected error: {e}")


# ### Question 13: Inheritance (Intermediate) - Health Portal
# **Scenario:** The platform is expanding. Standard `Patient` objects aren't enough. We need specialized behaviors for `ICUPatient`.
# **Task:** Create subclass `ICUPatient` that inherits from `Patient`. Add attribute `special_flag` and override `__init__` using `super()`.

class ICUPatient(Patient):
    def __init__(self, id, heart_rate, special_flag):
        super().__init__(id, heart_rate)
        self.special_flag = special_flag

# Test Question 13
sub_obj_13 = ICUPatient(103, 80, special_flag=True)
print(f"Created ICUPatient: ID={sub_obj_13.id}, heart_rate={sub_obj_13.heart_rate}, special_flag={sub_obj_13.special_flag}")


# ### Question 14: Polymorphism (Industry) - Health Portal
# **Scenario:** An orchestrator module needs to process a list of different `Patient` types seamlessly.
# **Task:** Override `update_vitals()` in `ICUPatient` to implement custom behavior. Write `process_all(entities)` that accepts a list and triggers `update_vitals()` on all.

class ICUPatientPolymorphic(Patient):
    def __init__(self, id, heart_rate, special_flag):
        super().__init__(id, heart_rate)
        self.special_flag = special_flag

    def update_vitals(self):
        print(f"[ICUPatient {self.id} | Flag: {self.special_flag}] ICU urgent vitals logged with priority alert.")

def process_all_health_portal(entities):
    for entity in entities:
        entity.update_vitals()

# Test Question 14
sample_list_14 = [
    Patient(101, 40),
    ICUPatientPolymorphic(102, 60, special_flag=True)
]
process_all_health_portal(sample_list_14)


# ### Question 15: Magic Methods (Industry) - Health Portal
# **Scenario:** Logs are cluttered with memory addresses. Devops needs readable logging, and analysts want to compare performance based on `heart_rate`.
# **Task:** Implement `__str__` for `Patient` to return a readable string, and `__gt__` to compare two objects based on `heart_rate`.

class PatientComplete(Patient):
    def __str__(self):
        return f"Patient(id={self.id}, heart_rate={self.heart_rate})"

    def __gt__(self, other):
        if not isinstance(other, Patient):
            return NotImplemented
        return self.heart_rate > other.heart_rate

# Test Question 15
item_a_15 = PatientComplete(1, 45)
item_b_15 = PatientComplete(2, 85)

print("Readable String representation:", str(item_a_15))
print(f"Is Item B > Item A? {item_b_15 > item_a_15}")


# ### Question 16: Classes and Objects (Beginner) - E-Commerce Cart
# **Scenario:** In the E-Commerce Cart project, the team needs to represent the core entity: `Product`.
# **Task:** Create a basic `Product` class initializing with `id` and `price`. Add a method `apply_discount()` that prints a status message.

class Product:
    def __init__(self, id, price):
        self.id = id
        self.price = price

    def apply_discount(self):
        print(f"[Product {self.id}] Standard discount applied to product.")

# Test Question 16
obj_16 = Product(101, 50)
obj_16.apply_discount()


# ### Question 17: Encapsulation & Properties (Intermediate) - E-Commerce Cart
# **Scenario:** Security audits revealed `price` was being altered maliciously or accidentally.
# **Task:** Modify `Product` to make `price` private (`_price`). Provide a property getter and setter that raises `ValueError` if negative.

class ProductEncapsulated:
    def __init__(self, id, price):
        self.id = id
        self.price = price  # Triggers the property setter

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError(f"'price' cannot be negative: {value}")
        self._price = value

# Test Question 17
enc_17 = ProductEncapsulated(102, 75)
print(f"Valid price: {enc_17.price}")
try:
    enc_17.price = -10
except ValueError as e:
    print(f"Caught expected error: {e}")


# ### Question 18: Inheritance (Intermediate) - E-Commerce Cart
# **Scenario:** The platform is expanding. Standard `Product` objects aren't enough. We need specialized behaviors for `DigitalProduct`.
# **Task:** Create subclass `DigitalProduct` that inherits from `Product`. Add attribute `special_flag` and override `__init__` using `super()`.

class DigitalProduct(Product):
    def __init__(self, id, price, special_flag):
        super().__init__(id, price)
        self.special_flag = special_flag

# Test Question 18
sub_obj_18 = DigitalProduct(103, 80, special_flag=True)
print(f"Created DigitalProduct: ID={sub_obj_18.id}, price={sub_obj_18.price}, special_flag={sub_obj_18.special_flag}")


# ### Question 19: Polymorphism (Industry) - E-Commerce Cart
# **Scenario:** An orchestrator module needs to process a list of different `Product` types seamlessly.
# **Task:** Override `apply_discount()` in `DigitalProduct` to implement custom behavior. Write `process_all(entities)` that accepts a list and triggers `apply_discount()` on all.

class DigitalProductPolymorphic(Product):
    def __init__(self, id, price, special_flag):
        super().__init__(id, price)
        self.special_flag = special_flag

    def apply_discount(self):
        print(f"[DigitalProduct {self.id} | Flag: {self.special_flag}] Digital discount voucher verified and applied instantly.")

def process_all_e_commerce_cart(entities):
    for entity in entities:
        entity.apply_discount()

# Test Question 19
sample_list_19 = [
    Product(101, 40),
    DigitalProductPolymorphic(102, 60, special_flag=True)
]
process_all_e_commerce_cart(sample_list_19)


# ### Question 20: Magic Methods (Industry) - E-Commerce Cart
# **Scenario:** Logs are cluttered with memory addresses. Devops needs readable logging, and analysts want to compare performance based on `price`.
# **Task:** Implement `__str__` for `Product` to return a readable string, and `__gt__` to compare two objects based on `price`.

class ProductComplete(Product):
    def __str__(self):
        return f"Product(id={self.id}, price={self.price})"

    def __gt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price > other.price

# Test Question 20
item_a_20 = ProductComplete(1, 45)
item_b_20 = ProductComplete(2, 85)

print("Readable String representation:", str(item_a_20))
print(f"Is Item B > Item A? {item_b_20 > item_a_20}")


# ### Question 21: Classes and Objects (Beginner) - Warehouse Bot
# **Scenario:** In the Warehouse Bot project, the team needs to represent the core entity: `Robot`.
# **Task:** Create a basic `Robot` class initializing with `id` and `battery_level`. Add a method `move_item()` that prints a status message.

class Robot:
    def __init__(self, id, battery_level):
        self.id = id
        self.battery_level = battery_level

    def move_item(self):
        print(f"[Robot {self.id}] Item moved to designated storage bay.")

# Test Question 21
obj_21 = Robot(101, 50)
obj_21.move_item()


# ### Question 22: Encapsulation & Properties (Intermediate) - Warehouse Bot
# **Scenario:** Security audits revealed `battery_level` was being altered maliciously or accidentally.
# **Task:** Modify `Robot` to make `battery_level` private (`_battery_level`). Provide a property getter and setter that raises `ValueError` if negative.

class RobotEncapsulated:
    def __init__(self, id, battery_level):
        self.id = id
        self.battery_level = battery_level  # Triggers the property setter

    @property
    def battery_level(self):
        return self._battery_level

    @battery_level.setter
    def battery_level(self, value):
        if value < 0:
            raise ValueError(f"'battery_level' cannot be negative: {value}")
        self._battery_level = value

# Test Question 22
enc_22 = RobotEncapsulated(102, 75)
print(f"Valid battery_level: {enc_22.battery_level}")
try:
    enc_22.battery_level = -10
except ValueError as e:
    print(f"Caught expected error: {e}")


# ### Question 23: Inheritance (Intermediate) - Warehouse Bot
# **Scenario:** The platform is expanding. Standard `Robot` objects aren't enough. We need specialized behaviors for `DroneBot`.
# **Task:** Create subclass `DroneBot` that inherits from `Robot`. Add attribute `special_flag` and override `__init__` using `super()`.

class DroneBot(Robot):
    def __init__(self, id, battery_level, special_flag):
        super().__init__(id, battery_level)
        self.special_flag = special_flag

# Test Question 23
sub_obj_23 = DroneBot(103, 80, special_flag=True)
print(f"Created DroneBot: ID={sub_obj_23.id}, battery_level={sub_obj_23.battery_level}, special_flag={sub_obj_23.special_flag}")


# ### Question 24: Polymorphism (Industry) - Warehouse Bot
# **Scenario:** An orchestrator module needs to process a list of different `Robot` types seamlessly.
# **Task:** Override `move_item()` in `DroneBot` to implement custom behavior. Write `process_all(entities)` that accepts a list and triggers `move_item()` on all.

class DroneBotPolymorphic(Robot):
    def __init__(self, id, battery_level, special_flag):
        super().__init__(id, battery_level)
        self.special_flag = special_flag

    def move_item(self):
        print(f"[DroneBot {self.id} | Flag: {self.special_flag}] DroneBot navigating 3D airspace to relocate item.")

def process_all_warehouse_bot(entities):
    for entity in entities:
        entity.move_item()

# Test Question 24
sample_list_24 = [
    Robot(101, 40),
    DroneBotPolymorphic(102, 60, special_flag=True)
]
process_all_warehouse_bot(sample_list_24)


# ### Question 25: Magic Methods (Industry) - Warehouse Bot
# **Scenario:** Logs are cluttered with memory addresses. Devops needs readable logging, and analysts want to compare performance based on `battery_level`.
# **Task:** Implement `__str__` for `Robot` to return a readable string, and `__gt__` to compare two objects based on `battery_level`.

class RobotComplete(Robot):
    def __str__(self):
        return f"Robot(id={self.id}, battery_level={self.battery_level})"

    def __gt__(self, other):
        if not isinstance(other, Robot):
            return NotImplemented
        return self.battery_level > other.battery_level

# Test Question 25
item_a_25 = RobotComplete(1, 45)
item_b_25 = RobotComplete(2, 85)

print("Readable String representation:", str(item_a_25))
print(f"Is Item B > Item A? {item_b_25 > item_a_25}")


# ### Question 26: Classes and Objects (Beginner) - StreamMax Video
# **Scenario:** In the StreamMax Video project, the team needs to represent the core entity: `Media`.
# **Task:** Create a basic `Media` class initializing with `id` and `bitrate`. Add a method `buffer_data()` that prints a status message.

class Media:
    def __init__(self, id, bitrate):
        self.id = id
        self.bitrate = bitrate

    def buffer_data(self):
        print(f"[Media {self.id}] Media chunk buffered into memory.")

# Test Question 26
obj_26 = Media(101, 50)
obj_26.buffer_data()


# ### Question 27: Encapsulation & Properties (Intermediate) - StreamMax Video
# **Scenario:** Security audits revealed `bitrate` was being altered maliciously or accidentally.
# **Task:** Modify `Media` to make `bitrate` private (`_bitrate`). Provide a property getter and setter that raises `ValueError` if negative.

class MediaEncapsulated:
    def __init__(self, id, bitrate):
        self.id = id
        self.bitrate = bitrate  # Triggers the property setter

    @property
    def bitrate(self):
        return self._bitrate

    @bitrate.setter
    def bitrate(self, value):
        if value < 0:
            raise ValueError(f"'bitrate' cannot be negative: {value}")
        self._bitrate = value

# Test Question 27
enc_27 = MediaEncapsulated(102, 75)
print(f"Valid bitrate: {enc_27.bitrate}")
try:
    enc_27.bitrate = -10
except ValueError as e:
    print(f"Caught expected error: {e}")


# ### Question 28: Inheritance (Intermediate) - StreamMax Video
# **Scenario:** The platform is expanding. Standard `Media` objects aren't enough. We need specialized behaviors for `LiveStream`.
# **Task:** Create subclass `LiveStream` that inherits from `Media`. Add attribute `special_flag` and override `__init__` using `super()`.

class LiveStream(Media):
    def __init__(self, id, bitrate, special_flag):
        super().__init__(id, bitrate)
        self.special_flag = special_flag

# Test Question 28
sub_obj_28 = LiveStream(103, 80, special_flag=True)
print(f"Created LiveStream: ID={sub_obj_28.id}, bitrate={sub_obj_28.bitrate}, special_flag={sub_obj_28.special_flag}")


# ### Question 29: Polymorphism (Industry) - StreamMax Video
# **Scenario:** An orchestrator module needs to process a list of different `Media` types seamlessly.
# **Task:** Override `buffer_data()` in `LiveStream` to implement custom behavior. Write `process_all(entities)` that accepts a list and triggers `buffer_data()` on all.

class LiveStreamPolymorphic(Media):
    def __init__(self, id, bitrate, special_flag):
        super().__init__(id, bitrate)
        self.special_flag = special_flag

    def buffer_data(self):
        print(f"[LiveStream {self.id} | Flag: {self.special_flag}] LiveStream real-time low-latency buffering active.")

def process_all_streammax_video(entities):
    for entity in entities:
        entity.buffer_data()

# Test Question 29
sample_list_29 = [
    Media(101, 40),
    LiveStreamPolymorphic(102, 60, special_flag=True)
]
process_all_streammax_video(sample_list_29)


# ### Question 30: Magic Methods (Industry) - StreamMax Video
# **Scenario:** Logs are cluttered with memory addresses. Devops needs readable logging, and analysts want to compare performance based on `bitrate`.
# **Task:** Implement `__str__` for `Media` to return a readable string, and `__gt__` to compare two objects based on `bitrate`.

class MediaComplete(Media):
    def __str__(self):
        return f"Media(id={self.id}, bitrate={self.bitrate})"

    def __gt__(self, other):
        if not isinstance(other, Media):
            return NotImplemented
        return self.bitrate > other.bitrate

# Test Question 30
item_a_30 = MediaComplete(1, 45)
item_b_30 = MediaComplete(2, 85)

print("Readable String representation:", str(item_a_30))
print(f"Is Item B > Item A? {item_b_30 > item_a_30}")


# ### Question 31: Classes and Objects (Beginner) - RideHailing
# **Scenario:** In the RideHailing project, the team needs to represent the core entity: `Driver`.
# **Task:** Create a basic `Driver` class initializing with `id` and `rating`. Add a method `accept_ride()` that prints a status message.

class Driver:
    def __init__(self, id, rating):
        self.id = id
        self.rating = rating

    def accept_ride(self):
        print(f"[Driver {self.id}] Ride accepted by driver.")

# Test Question 31
obj_31 = Driver(101, 50)
obj_31.accept_ride()


# ### Question 32: Encapsulation & Properties (Intermediate) - RideHailing
# **Scenario:** Security audits revealed `rating` was being altered maliciously or accidentally.
# **Task:** Modify `Driver` to make `rating` private (`_rating`). Provide a property getter and setter that raises `ValueError` if negative.

class DriverEncapsulated:
    def __init__(self, id, rating):
        self.id = id
        self.rating = rating  # Triggers the property setter

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if value < 0:
            raise ValueError(f"'rating' cannot be negative: {value}")
        self._rating = value

# Test Question 32
enc_32 = DriverEncapsulated(102, 75)
print(f"Valid rating: {enc_32.rating}")
try:
    enc_32.rating = -10
except ValueError as e:
    print(f"Caught expected error: {e}")


# ### Question 33: Inheritance (Intermediate) - RideHailing
# **Scenario:** The platform is expanding. Standard `Driver` objects aren't enough. We need specialized behaviors for `PremiumDriver`.
# **Task:** Create subclass `PremiumDriver` that inherits from `Driver`. Add attribute `special_flag` and override `__init__` using `super()`.

class PremiumDriver(Driver):
    def __init__(self, id, rating, special_flag):
        super().__init__(id, rating)
        self.special_flag = special_flag

# Test Question 33
sub_obj_33 = PremiumDriver(103, 80, special_flag=True)
print(f"Created PremiumDriver: ID={sub_obj_33.id}, rating={sub_obj_33.rating}, special_flag={sub_obj_33.special_flag}")


# ### Question 34: Polymorphism (Industry) - RideHailing
# **Scenario:** An orchestrator module needs to process a list of different `Driver` types seamlessly.
# **Task:** Override `accept_ride()` in `PremiumDriver` to implement custom behavior. Write `process_all(entities)` that accepts a list and triggers `accept_ride()` on all.

class PremiumDriverPolymorphic(Driver):
    def __init__(self, id, rating, special_flag):
        super().__init__(id, rating)
        self.special_flag = special_flag

    def accept_ride(self):
        print(f"[PremiumDriver {self.id} | Flag: {self.special_flag}] Premium luxury ride confirmed with white-glove dispatch.")

def process_all_ridehailing(entities):
    for entity in entities:
        entity.accept_ride()

# Test Question 34
sample_list_34 = [
    Driver(101, 40),
    PremiumDriverPolymorphic(102, 60, special_flag=True)
]
process_all_ridehailing(sample_list_34)


# ### Question 35: Magic Methods (Industry) - RideHailing
# **Scenario:** Logs are cluttered with memory addresses. Devops needs readable logging, and analysts want to compare performance based on `rating`.
# **Task:** Implement `__str__` for `Driver` to return a readable string, and `__gt__` to compare two objects based on `rating`.

class DriverComplete(Driver):
    def __str__(self):
        return f"Driver(id={self.id}, rating={self.rating})"

    def __gt__(self, other):
        if not isinstance(other, Driver):
            return NotImplemented
        return self.rating > other.rating

# Test Question 35
item_a_35 = DriverComplete(1, 45)
item_b_35 = DriverComplete(2, 85)

print("Readable String representation:", str(item_a_35))
print(f"Is Item B > Item A? {item_b_35 > item_a_35}")


# ### Question 36: Classes and Objects (Beginner) - Social Connect
# **Scenario:** In the Social Connect project, the team needs to represent the core entity: `User`.
# **Task:** Create a basic `User` class initializing with `id` and `follower_count`. Add a method `post_update()` that prints a status message.

class User:
    def __init__(self, id, follower_count):
        self.id = id
        self.follower_count = follower_count

    def post_update(self):
        print(f"[User {self.id}] User update posted to timeline.")

# Test Question 36
obj_36 = User(101, 50)
obj_36.post_update()


# ### Question 37: Encapsulation & Properties (Intermediate) - Social Connect
# **Scenario:** Security audits revealed `follower_count` was being altered maliciously or accidentally.
# **Task:** Modify `User` to make `follower_count` private (`_follower_count`). Provide a property getter and setter that raises `ValueError` if negative.

class UserEncapsulated:
    def __init__(self, id, follower_count):
        self.id = id
        self.follower_count = follower_count  # Triggers the property setter

    @property
    def follower_count(self):
        return self._follower_count

    @follower_count.setter
    def follower_count(self, value):
        if value < 0:
            raise ValueError(f"'follower_count' cannot be negative: {value}")
        self._follower_count = value

# Test Question 37
enc_37 = UserEncapsulated(102, 75)
print(f"Valid follower_count: {enc_37.follower_count}")
try:
    enc_37.follower_count = -10
except ValueError as e:
    print(f"Caught expected error: {e}")


# ### Question 38: Inheritance (Intermediate) - Social Connect
# **Scenario:** The platform is expanding. Standard `User` objects aren't enough. We need specialized behaviors for `VerifiedUser`.
# **Task:** Create subclass `VerifiedUser` that inherits from `User`. Add attribute `special_flag` and override `__init__` using `super()`.

class VerifiedUser(User):
    def __init__(self, id, follower_count, special_flag):
        super().__init__(id, follower_count)
        self.special_flag = special_flag

# Test Question 38
sub_obj_38 = VerifiedUser(103, 80, special_flag=True)
print(f"Created VerifiedUser: ID={sub_obj_38.id}, follower_count={sub_obj_38.follower_count}, special_flag={sub_obj_38.special_flag}")


# ### Question 39: Polymorphism (Industry) - Social Connect
# **Scenario:** An orchestrator module needs to process a list of different `User` types seamlessly.
# **Task:** Override `post_update()` in `VerifiedUser` to implement custom behavior. Write `process_all(entities)` that accepts a list and triggers `post_update()` on all.

class VerifiedUserPolymorphic(User):
    def __init__(self, id, follower_count, special_flag):
        super().__init__(id, follower_count)
        self.special_flag = special_flag

    def post_update(self):
        print(f"[VerifiedUser {self.id} | Flag: {self.special_flag}] Verified high-reach update broadcasted with checkmark badge.")

def process_all_social_connect(entities):
    for entity in entities:
        entity.post_update()

# Test Question 39
sample_list_39 = [
    User(101, 40),
    VerifiedUserPolymorphic(102, 60, special_flag=True)
]
process_all_social_connect(sample_list_39)


# ### Question 40: Magic Methods (Industry) - Social Connect
# **Scenario:** Logs are cluttered with memory addresses. Devops needs readable logging, and analysts want to compare performance based on `follower_count`.
# **Task:** Implement `__str__` for `User` to return a readable string, and `__gt__` to compare two objects based on `follower_count`.

class UserComplete(User):
    def __str__(self):
        return f"User(id={self.id}, follower_count={self.follower_count})"

    def __gt__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.follower_count > other.follower_count

# Test Question 40
item_a_40 = UserComplete(1, 45)
item_b_40 = UserComplete(2, 85)

print("Readable String representation:", str(item_a_40))
print(f"Is Item B > Item A? {item_b_40 > item_a_40}")


# ### Question 41: Classes and Objects (Beginner) - Cloud Manager
# **Scenario:** In the Cloud Manager project, the team needs to represent the core entity: `Server`.
# **Task:** Create a basic `Server` class initializing with `id` and `cpu_load`. Add a method `allocate_ram()` that prints a status message.

class Server:
    def __init__(self, id, cpu_load):
        self.id = id
        self.cpu_load = cpu_load

    def allocate_ram(self):
        print(f"[Server {self.id}] RAM chunk allocated to workload.")

# Test Question 41
obj_41 = Server(101, 50)
obj_41.allocate_ram()


# ### Question 42: Encapsulation & Properties (Intermediate) - Cloud Manager
# **Scenario:** Security audits revealed `cpu_load` was being altered maliciously or accidentally.
# **Task:** Modify `Server` to make `cpu_load` private (`_cpu_load`). Provide a property getter and setter that raises `ValueError` if negative.

class ServerEncapsulated:
    def __init__(self, id, cpu_load):
        self.id = id
        self.cpu_load = cpu_load  # Triggers the property setter

    @property
    def cpu_load(self):
        return self._cpu_load

    @cpu_load.setter
    def cpu_load(self, value):
        if value < 0:
            raise ValueError(f"'cpu_load' cannot be negative: {value}")
        self._cpu_load = value

# Test Question 42
enc_42 = ServerEncapsulated(102, 75)
print(f"Valid cpu_load: {enc_42.cpu_load}")
try:
    enc_42.cpu_load = -10
except ValueError as e:
    print(f"Caught expected error: {e}")


# ### Question 43: Inheritance (Intermediate) - Cloud Manager
# **Scenario:** The platform is expanding. Standard `Server` objects aren't enough. We need specialized behaviors for `DatabaseServer`.
# **Task:** Create subclass `DatabaseServer` that inherits from `Server`. Add attribute `special_flag` and override `__init__` using `super()`.

class DatabaseServer(Server):
    def __init__(self, id, cpu_load, special_flag):
        super().__init__(id, cpu_load)
        self.special_flag = special_flag

# Test Question 43
sub_obj_43 = DatabaseServer(103, 80, special_flag=True)
print(f"Created DatabaseServer: ID={sub_obj_43.id}, cpu_load={sub_obj_43.cpu_load}, special_flag={sub_obj_43.special_flag}")


# ### Question 44: Polymorphism (Industry) - Cloud Manager
# **Scenario:** An orchestrator module needs to process a list of different `Server` types seamlessly.
# **Task:** Override `allocate_ram()` in `DatabaseServer` to implement custom behavior. Write `process_all(entities)` that accepts a list and triggers `allocate_ram()` on all.

class DatabaseServerPolymorphic(Server):
    def __init__(self, id, cpu_load, special_flag):
        super().__init__(id, cpu_load)
        self.special_flag = special_flag

    def allocate_ram(self):
        print(f"[DatabaseServer {self.id} | Flag: {self.special_flag}] Database buffer pool memory pre-allocated with ACID guarantees.")

def process_all_cloud_manager(entities):
    for entity in entities:
        entity.allocate_ram()

# Test Question 44
sample_list_44 = [
    Server(101, 40),
    DatabaseServerPolymorphic(102, 60, special_flag=True)
]
process_all_cloud_manager(sample_list_44)


# ### Question 45: Magic Methods (Industry) - Cloud Manager
# **Scenario:** Logs are cluttered with memory addresses. Devops needs readable logging, and analysts want to compare performance based on `cpu_load`.
# **Task:** Implement `__str__` for `Server` to return a readable string, and `__gt__` to compare two objects based on `cpu_load`.

class ServerComplete(Server):
    def __str__(self):
        return f"Server(id={self.id}, cpu_load={self.cpu_load})"

    def __gt__(self, other):
        if not isinstance(other, Server):
            return NotImplemented
        return self.cpu_load > other.cpu_load

# Test Question 45
item_a_45 = ServerComplete(1, 45)
item_b_45 = ServerComplete(2, 85)

print("Readable String representation:", str(item_a_45))
print(f"Is Item B > Item A? {item_b_45 > item_a_45}")


# ### Question 46: Classes and Objects (Beginner) - RPG Engine
# **Scenario:** In the RPG Engine project, the team needs to represent the core entity: `Character`.
# **Task:** Create a basic `Character` class initializing with `id` and `mana_points`. Add a method `cast_spell()` that prints a status message.

class Character:
    def __init__(self, id, mana_points):
        self.id = id
        self.mana_points = mana_points

    def cast_spell(self):
        print(f"[Character {self.id}] Standard spell cast successfully.")

# Test Question 46
obj_46 = Character(101, 50)
obj_46.cast_spell()


# ### Question 47: Encapsulation & Properties (Intermediate) - RPG Engine
# **Scenario:** Security audits revealed `mana_points` was being altered maliciously or accidentally.
# **Task:** Modify `Character` to make `mana_points` private (`_mana_points`). Provide a property getter and setter that raises `ValueError` if negative.

class CharacterEncapsulated:
    def __init__(self, id, mana_points):
        self.id = id
        self.mana_points = mana_points  # Triggers the property setter

    @property
    def mana_points(self):
        return self._mana_points

    @mana_points.setter
    def mana_points(self, value):
        if value < 0:
            raise ValueError(f"'mana_points' cannot be negative: {value}")
        self._mana_points = value

# Test Question 47
enc_47 = CharacterEncapsulated(102, 75)
print(f"Valid mana_points: {enc_47.mana_points}")
try:
    enc_47.mana_points = -10
except ValueError as e:
    print(f"Caught expected error: {e}")


# ### Question 48: Inheritance (Intermediate) - RPG Engine
# **Scenario:** The platform is expanding. Standard `Character` objects aren't enough. We need specialized behaviors for `Mage`.
# **Task:** Create subclass `Mage` that inherits from `Character`. Add attribute `special_flag` and override `__init__` using `super()`.

class Mage(Character):
    def __init__(self, id, mana_points, special_flag):
        super().__init__(id, mana_points)
        self.special_flag = special_flag

# Test Question 48
sub_obj_48 = Mage(103, 80, special_flag=True)
print(f"Created Mage: ID={sub_obj_48.id}, mana_points={sub_obj_48.mana_points}, special_flag={sub_obj_48.special_flag}")


# ### Question 49: Polymorphism (Industry) - RPG Engine
# **Scenario:** An orchestrator module needs to process a list of different `Character` types seamlessly.
# **Task:** Override `cast_spell()` in `Mage` to implement custom behavior. Write `process_all(entities)` that accepts a list and triggers `cast_spell()` on all.

class MagePolymorphic(Character):
    def __init__(self, id, mana_points, special_flag):
        super().__init__(id, mana_points)
        self.special_flag = special_flag

    def cast_spell(self):
        print(f"[Mage {self.id} | Flag: {self.special_flag}] Mage conjures high-tier elemental arcane storm.")

def process_all_rpg_engine(entities):
    for entity in entities:
        entity.cast_spell()

# Test Question 49
sample_list_49 = [
    Character(101, 40),
    MagePolymorphic(102, 60, special_flag=True)
]
process_all_rpg_engine(sample_list_49)


# ### Question 50: Magic Methods (Industry) - RPG Engine
# **Scenario:** Logs are cluttered with memory addresses. Devops needs readable logging, and analysts want to compare performance based on `mana_points`.
# **Task:** Implement `__str__` for `Character` to return a readable string, and `__gt__` to compare two objects based on `mana_points`.

class CharacterComplete(Character):
    def __str__(self):
        return f"Character(id={self.id}, mana_points={self.mana_points})"

    def __gt__(self, other):
        if not isinstance(other, Character):
            return NotImplemented
        return self.mana_points > other.mana_points

# Test Question 50
item_a_50 = CharacterComplete(1, 45)
item_b_50 = CharacterComplete(2, 85)

print("Readable String representation:", str(item_a_50))
print(f"Is Item B > Item A? {item_b_50 > item_a_50}")

