# ---
# # Part 2: Intermediate OOP Scenarios (50 Multi-Step Industry Challenges)
# Based on **Intermediate OOP Scenarios: 50 Multi-Step Industry Challenges Practice Workbook**.
# Each challenge focuses on specific advanced OOP mechanics:
# - Encapsulation & Properties (`@property`, setters, input validation)
# - Inheritance & `super()`
# - Abstract Base Classes (`abc.ABC`, `@abstractmethod`)
# - Class & Static Methods (`@classmethod`, `@staticmethod`)
# - Magic Methods (`__str__`, `__add__`, `__gt__`)
# ---

# ### Challenge 1: Encapsulation & Properties
# **Challenge Focus:** Product Pricing Integrity (Instance 1)

# Challenge 1 Solution
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
            raise ValueError(f"Price cannot be negative: {value}")
        self._price = value

# Verification
p = Product("SKU-9901", 149.99)
print(f"Product SKU: {p.sku}, Price: ${p.price}")
try:
    p.price = -20
except ValueError as err:
    print(f"Validation success: {err}")


# ### Challenge 2: Inheritance & super()
# **Challenge Focus:** Finance Platform Margin Accounts (Instance 1)

# Challenge 2 Solution
class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

class MarginAccount(Account):
    def __init__(self, account_id, balance, special_flag):
        super().__init__(account_id, balance)
        self.special_flag = special_flag

# Verification
ma = MarginAccount("ACC-7788", 50000.0, special_flag=True)
print(f"Account ID: {ma.account_id}, Balance: ${ma.balance:,.2f}, Special Flag: {ma.special_flag}")


# ### Challenge 3: Abstract Base Classes
# **Challenge Focus:** Healthcare Architecture ABC Guarantee (Instance 1)

# Challenge 3 Solution
from abc import ABC, abstractmethod

class Patient(ABC):
    def __init__(self, patient_id):
        self.patient_id = patient_id

    @abstractmethod
    def record_vitals(self):
        pass

class ICUPatient(Patient):
    def __init__(self, patient_id, heart_rate, oxygen_level):
        super().__init__(patient_id)
        self.heart_rate = heart_rate
        self.oxygen_level = oxygen_level

    def record_vitals(self):
        return f"ICU Patient {self.patient_id} Vitals: HR={self.heart_rate} bpm, SpO2={self.oxygen_level}%"

# Verification
icu = ICUPatient("P-104", 72, 98)
print(icu.record_vitals())


# ### Challenge 4: Class & Static Methods
# **Challenge Focus:** Smart Home API Parsing & MAC Validation (Instance 1)

# Challenge 4 Solution
class Device:
    def __init__(self, mac_address, temperature):
        self.mac_address = mac_address
        self.temperature = float(temperature)

    @staticmethod
    def validate_mac_address(mac_str):
        return len(str(mac_str)) > 3

    @classmethod
    def from_string(cls, raw_str):
        # String formatted as 'attr2-attr1' -> 'temperature-mac_address'
        parts = raw_str.split("-", 1)
        attr2 = parts[0]
        attr1 = parts[1]
        return cls(mac_address=attr1, temperature=attr2)

# Verification
valid = Device.validate_mac_address("00:1A:2B")
print(f"MAC Valid? {valid}")
dev = Device.from_string("72.5-AA:BB:CC:DD")
print(f"Parsed Device -> MAC: {dev.mac_address}, Temp: {dev.temperature}°F")


# ### Challenge 5: Magic Methods
# **Challenge Focus:** Logistics Shipment Aggregation & Comparison (Instance 1)

# Challenge 5 Solution
class Shipment:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return f"Shipment: [{self.weight}]"

    def __add__(self, other):
        if isinstance(other, Shipment):
            return self.weight + other.weight
        return self.weight + other

    def __gt__(self, other):
        if isinstance(other, Shipment):
            return self.weight > other.weight
        return self.weight > other

# Verification
s1 = Shipment("New York", 150)
s2 = Shipment("London", 275)
print(str(s1))
print(f"Total Weight: {s1 + s2} kg")
print(f"Is s2 heavier than s1? {s2 > s1}")


# ### Challenge 6: Encapsulation & Properties
# **Challenge Focus:** Social Media Post Likes Guard (Instance 1)

# Challenge 6 Solution
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
            raise ValueError(f"Likes cannot be negative: {value}")
        self._likes = value

# Verification
post = Post("POST-1002", 50)
print(f"Post {post.post_id} has {post.likes} likes")
try:
    post.likes = -5
except ValueError as e:
    print(f"Caught negative likes validation: {e}")


# ### Challenge 7: Inheritance & super()
# **Challenge Focus:** EdTech Course & Bootcamp Extension (Instance 1)

# Challenge 7 Solution
class Course:
    def __init__(self, course_code, enrollment):
        self.course_code = course_code
        self.enrollment = enrollment

class Bootcamp(Course):
    def __init__(self, course_code, enrollment, special_flag):
        super().__init__(course_code, enrollment)
        self.special_flag = special_flag

# Verification
bc = Bootcamp("PY-OOP-301", 120, special_flag=True)
print(f"Course: {bc.course_code}, Enrollment: {bc.enrollment}, Special Flag: {bc.special_flag}")


# ### Challenge 8: Abstract Base Classes
# **Challenge Focus:** Gaming Architecture Damage Protocol (Instance 1)

# Challenge 8 Solution
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    @abstractmethod
    def take_damage(self, amount):
        pass

class BossCharacter(Character):
    def __init__(self, name, health=500, shield=50):
        super().__init__(name, health)
        self.shield = shield

    def take_damage(self, amount):
        effective_damage = max(0, amount - self.shield)
        self.health -= effective_damage
        return f"{self.name} took {effective_damage} damage (shield absorbed {min(amount, self.shield)}). Health remaining: {self.health}"

# Verification
boss = BossCharacter("Malakor the Destroyer", 1000, shield=40)
print(boss.take_damage(100))


# ### Challenge 9: Class & Static Methods
# **Challenge Focus:** Cloud Server IP Validation & String Factory (Instance 1)

# Challenge 9 Solution
class Server:
    def __init__(self, ip_address, cpu_load):
        self.ip_address = ip_address
        self.cpu_load = float(cpu_load)

    @staticmethod
    def validate_ip_address(ip_str):
        return len(str(ip_str)) > 3

    @classmethod
    def from_string(cls, raw_str):
        # Formatted as 'attr2-attr1' -> 'cpu_load-ip_address'
        parts = raw_str.split("-", 1)
        attr2 = parts[0]
        attr1 = parts[1]
        return cls(ip_address=attr1, cpu_load=attr2)

# Verification
print(f"Valid IP? {Server.validate_ip_address('192.168.1.1')}")
srv = Server.from_string("84.2-10.0.0.1")
print(f"Server IP: {srv.ip_address}, CPU Load: {srv.cpu_load}%")


# ### Challenge 10: Magic Methods
# **Challenge Focus:** Travel Flight Aggregation & Seat Availability (Instance 1)

# Challenge 10 Solution
class Flight:
    def __init__(self, flight_number, seats_available):
        self.flight_number = flight_number
        self.seats_available = seats_available

    def __str__(self):
        return f"Flight: [{self.seats_available}]"

    def __add__(self, other):
        if isinstance(other, Flight):
            return self.seats_available + other.seats_available
        return self.seats_available + other

    def __gt__(self, other):
        if isinstance(other, Flight):
            return self.seats_available > other.seats_available
        return self.seats_available > other

# Verification
f1 = Flight("AI-101", 45)
f2 = Flight("BA-202", 120)
print(str(f1))
print(f"Combined Available Seats: {f1 + f2}")
print(f"Does f2 have more seats than f1? {f2 > f1}")


# ### Challenge 11: Encapsulation & Properties
# **Challenge Focus:** Product Pricing Integrity (Instance 2)

# Challenge 11 Solution
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
            raise ValueError(f"Price cannot be negative: {value}")
        self._price = value

# Verification
p = Product("SKU-9901", 149.99)
print(f"Product SKU: {p.sku}, Price: ${p.price}")
try:
    p.price = -20
except ValueError as err:
    print(f"Validation success: {err}")


# ### Challenge 12: Inheritance & super()
# **Challenge Focus:** Finance Platform Margin Accounts (Instance 2)

# Challenge 12 Solution
class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

class MarginAccount(Account):
    def __init__(self, account_id, balance, special_flag):
        super().__init__(account_id, balance)
        self.special_flag = special_flag

# Verification
ma = MarginAccount("ACC-7788", 50000.0, special_flag=True)
print(f"Account ID: {ma.account_id}, Balance: ${ma.balance:,.2f}, Special Flag: {ma.special_flag}")


# ### Challenge 13: Abstract Base Classes
# **Challenge Focus:** Healthcare Architecture ABC Guarantee (Instance 2)

# Challenge 13 Solution
from abc import ABC, abstractmethod

class Patient(ABC):
    def __init__(self, patient_id):
        self.patient_id = patient_id

    @abstractmethod
    def record_vitals(self):
        pass

class ICUPatient(Patient):
    def __init__(self, patient_id, heart_rate, oxygen_level):
        super().__init__(patient_id)
        self.heart_rate = heart_rate
        self.oxygen_level = oxygen_level

    def record_vitals(self):
        return f"ICU Patient {self.patient_id} Vitals: HR={self.heart_rate} bpm, SpO2={self.oxygen_level}%"

# Verification
icu = ICUPatient("P-104", 72, 98)
print(icu.record_vitals())


# ### Challenge 14: Class & Static Methods
# **Challenge Focus:** Smart Home API Parsing & MAC Validation (Instance 2)

# Challenge 14 Solution
class Device:
    def __init__(self, mac_address, temperature):
        self.mac_address = mac_address
        self.temperature = float(temperature)

    @staticmethod
    def validate_mac_address(mac_str):
        return len(str(mac_str)) > 3

    @classmethod
    def from_string(cls, raw_str):
        # String formatted as 'attr2-attr1' -> 'temperature-mac_address'
        parts = raw_str.split("-", 1)
        attr2 = parts[0]
        attr1 = parts[1]
        return cls(mac_address=attr1, temperature=attr2)

# Verification
valid = Device.validate_mac_address("00:1A:2B")
print(f"MAC Valid? {valid}")
dev = Device.from_string("72.5-AA:BB:CC:DD")
print(f"Parsed Device -> MAC: {dev.mac_address}, Temp: {dev.temperature}°F")


# ### Challenge 15: Magic Methods
# **Challenge Focus:** Logistics Shipment Aggregation & Comparison (Instance 2)

# Challenge 15 Solution
class Shipment:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return f"Shipment: [{self.weight}]"

    def __add__(self, other):
        if isinstance(other, Shipment):
            return self.weight + other.weight
        return self.weight + other

    def __gt__(self, other):
        if isinstance(other, Shipment):
            return self.weight > other.weight
        return self.weight > other

# Verification
s1 = Shipment("New York", 150)
s2 = Shipment("London", 275)
print(str(s1))
print(f"Total Weight: {s1 + s2} kg")
print(f"Is s2 heavier than s1? {s2 > s1}")


# ### Challenge 16: Encapsulation & Properties
# **Challenge Focus:** Social Media Post Likes Guard (Instance 2)

# Challenge 16 Solution
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
            raise ValueError(f"Likes cannot be negative: {value}")
        self._likes = value

# Verification
post = Post("POST-1002", 50)
print(f"Post {post.post_id} has {post.likes} likes")
try:
    post.likes = -5
except ValueError as e:
    print(f"Caught negative likes validation: {e}")


# ### Challenge 17: Inheritance & super()
# **Challenge Focus:** EdTech Course & Bootcamp Extension (Instance 2)

# Challenge 17 Solution
class Course:
    def __init__(self, course_code, enrollment):
        self.course_code = course_code
        self.enrollment = enrollment

class Bootcamp(Course):
    def __init__(self, course_code, enrollment, special_flag):
        super().__init__(course_code, enrollment)
        self.special_flag = special_flag

# Verification
bc = Bootcamp("PY-OOP-301", 120, special_flag=True)
print(f"Course: {bc.course_code}, Enrollment: {bc.enrollment}, Special Flag: {bc.special_flag}")


# ### Challenge 18: Abstract Base Classes
# **Challenge Focus:** Gaming Architecture Damage Protocol (Instance 2)

# Challenge 18 Solution
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    @abstractmethod
    def take_damage(self, amount):
        pass

class BossCharacter(Character):
    def __init__(self, name, health=500, shield=50):
        super().__init__(name, health)
        self.shield = shield

    def take_damage(self, amount):
        effective_damage = max(0, amount - self.shield)
        self.health -= effective_damage
        return f"{self.name} took {effective_damage} damage (shield absorbed {min(amount, self.shield)}). Health remaining: {self.health}"

# Verification
boss = BossCharacter("Malakor the Destroyer", 1000, shield=40)
print(boss.take_damage(100))


# ### Challenge 19: Class & Static Methods
# **Challenge Focus:** Cloud Server IP Validation & String Factory (Instance 2)

# Challenge 19 Solution
class Server:
    def __init__(self, ip_address, cpu_load):
        self.ip_address = ip_address
        self.cpu_load = float(cpu_load)

    @staticmethod
    def validate_ip_address(ip_str):
        return len(str(ip_str)) > 3

    @classmethod
    def from_string(cls, raw_str):
        # Formatted as 'attr2-attr1' -> 'cpu_load-ip_address'
        parts = raw_str.split("-", 1)
        attr2 = parts[0]
        attr1 = parts[1]
        return cls(ip_address=attr1, cpu_load=attr2)

# Verification
print(f"Valid IP? {Server.validate_ip_address('192.168.1.1')}")
srv = Server.from_string("84.2-10.0.0.1")
print(f"Server IP: {srv.ip_address}, CPU Load: {srv.cpu_load}%")


# ### Challenge 20: Magic Methods
# **Challenge Focus:** Travel Flight Aggregation & Seat Availability (Instance 2)

# Challenge 20 Solution
class Flight:
    def __init__(self, flight_number, seats_available):
        self.flight_number = flight_number
        self.seats_available = seats_available

    def __str__(self):
        return f"Flight: [{self.seats_available}]"

    def __add__(self, other):
        if isinstance(other, Flight):
            return self.seats_available + other.seats_available
        return self.seats_available + other

    def __gt__(self, other):
        if isinstance(other, Flight):
            return self.seats_available > other.seats_available
        return self.seats_available > other

# Verification
f1 = Flight("AI-101", 45)
f2 = Flight("BA-202", 120)
print(str(f1))
print(f"Combined Available Seats: {f1 + f2}")
print(f"Does f2 have more seats than f1? {f2 > f1}")


# ### Challenge 21: Encapsulation & Properties
# **Challenge Focus:** Product Pricing Integrity (Instance 3)

# Challenge 21 Solution
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
            raise ValueError(f"Price cannot be negative: {value}")
        self._price = value

# Verification
p = Product("SKU-9901", 149.99)
print(f"Product SKU: {p.sku}, Price: ${p.price}")
try:
    p.price = -20
except ValueError as err:
    print(f"Validation success: {err}")


# ### Challenge 22: Inheritance & super()
# **Challenge Focus:** Finance Platform Margin Accounts (Instance 3)

# Challenge 22 Solution
class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

class MarginAccount(Account):
    def __init__(self, account_id, balance, special_flag):
        super().__init__(account_id, balance)
        self.special_flag = special_flag

# Verification
ma = MarginAccount("ACC-7788", 50000.0, special_flag=True)
print(f"Account ID: {ma.account_id}, Balance: ${ma.balance:,.2f}, Special Flag: {ma.special_flag}")


# ### Challenge 23: Abstract Base Classes
# **Challenge Focus:** Healthcare Architecture ABC Guarantee (Instance 3)

# Challenge 23 Solution
from abc import ABC, abstractmethod

class Patient(ABC):
    def __init__(self, patient_id):
        self.patient_id = patient_id

    @abstractmethod
    def record_vitals(self):
        pass

class ICUPatient(Patient):
    def __init__(self, patient_id, heart_rate, oxygen_level):
        super().__init__(patient_id)
        self.heart_rate = heart_rate
        self.oxygen_level = oxygen_level

    def record_vitals(self):
        return f"ICU Patient {self.patient_id} Vitals: HR={self.heart_rate} bpm, SpO2={self.oxygen_level}%"

# Verification
icu = ICUPatient("P-104", 72, 98)
print(icu.record_vitals())


# ### Challenge 24: Class & Static Methods
# **Challenge Focus:** Smart Home API Parsing & MAC Validation (Instance 3)

# Challenge 24 Solution
class Device:
    def __init__(self, mac_address, temperature):
        self.mac_address = mac_address
        self.temperature = float(temperature)

    @staticmethod
    def validate_mac_address(mac_str):
        return len(str(mac_str)) > 3

    @classmethod
    def from_string(cls, raw_str):
        # String formatted as 'attr2-attr1' -> 'temperature-mac_address'
        parts = raw_str.split("-", 1)
        attr2 = parts[0]
        attr1 = parts[1]
        return cls(mac_address=attr1, temperature=attr2)

# Verification
valid = Device.validate_mac_address("00:1A:2B")
print(f"MAC Valid? {valid}")
dev = Device.from_string("72.5-AA:BB:CC:DD")
print(f"Parsed Device -> MAC: {dev.mac_address}, Temp: {dev.temperature}°F")


# ### Challenge 25: Magic Methods
# **Challenge Focus:** Logistics Shipment Aggregation & Comparison (Instance 3)

# Challenge 25 Solution
class Shipment:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return f"Shipment: [{self.weight}]"

    def __add__(self, other):
        if isinstance(other, Shipment):
            return self.weight + other.weight
        return self.weight + other

    def __gt__(self, other):
        if isinstance(other, Shipment):
            return self.weight > other.weight
        return self.weight > other

# Verification
s1 = Shipment("New York", 150)
s2 = Shipment("London", 275)
print(str(s1))
print(f"Total Weight: {s1 + s2} kg")
print(f"Is s2 heavier than s1? {s2 > s1}")


# ### Challenge 26: Encapsulation & Properties
# **Challenge Focus:** Social Media Post Likes Guard (Instance 3)

# Challenge 26 Solution
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
            raise ValueError(f"Likes cannot be negative: {value}")
        self._likes = value

# Verification
post = Post("POST-1002", 50)
print(f"Post {post.post_id} has {post.likes} likes")
try:
    post.likes = -5
except ValueError as e:
    print(f"Caught negative likes validation: {e}")


# ### Challenge 27: Inheritance & super()
# **Challenge Focus:** EdTech Course & Bootcamp Extension (Instance 3)

# Challenge 27 Solution
class Course:
    def __init__(self, course_code, enrollment):
        self.course_code = course_code
        self.enrollment = enrollment

class Bootcamp(Course):
    def __init__(self, course_code, enrollment, special_flag):
        super().__init__(course_code, enrollment)
        self.special_flag = special_flag

# Verification
bc = Bootcamp("PY-OOP-301", 120, special_flag=True)
print(f"Course: {bc.course_code}, Enrollment: {bc.enrollment}, Special Flag: {bc.special_flag}")


# ### Challenge 28: Abstract Base Classes
# **Challenge Focus:** Gaming Architecture Damage Protocol (Instance 3)

# Challenge 28 Solution
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    @abstractmethod
    def take_damage(self, amount):
        pass

class BossCharacter(Character):
    def __init__(self, name, health=500, shield=50):
        super().__init__(name, health)
        self.shield = shield

    def take_damage(self, amount):
        effective_damage = max(0, amount - self.shield)
        self.health -= effective_damage
        return f"{self.name} took {effective_damage} damage (shield absorbed {min(amount, self.shield)}). Health remaining: {self.health}"

# Verification
boss = BossCharacter("Malakor the Destroyer", 1000, shield=40)
print(boss.take_damage(100))


# ### Challenge 29: Class & Static Methods
# **Challenge Focus:** Cloud Server IP Validation & String Factory (Instance 3)

# Challenge 29 Solution
class Server:
    def __init__(self, ip_address, cpu_load):
        self.ip_address = ip_address
        self.cpu_load = float(cpu_load)

    @staticmethod
    def validate_ip_address(ip_str):
        return len(str(ip_str)) > 3

    @classmethod
    def from_string(cls, raw_str):
        # Formatted as 'attr2-attr1' -> 'cpu_load-ip_address'
        parts = raw_str.split("-", 1)
        attr2 = parts[0]
        attr1 = parts[1]
        return cls(ip_address=attr1, cpu_load=attr2)

# Verification
print(f"Valid IP? {Server.validate_ip_address('192.168.1.1')}")
srv = Server.from_string("84.2-10.0.0.1")
print(f"Server IP: {srv.ip_address}, CPU Load: {srv.cpu_load}%")


# ### Challenge 30: Magic Methods
# **Challenge Focus:** Travel Flight Aggregation & Seat Availability (Instance 3)

# Challenge 30 Solution
class Flight:
    def __init__(self, flight_number, seats_available):
        self.flight_number = flight_number
        self.seats_available = seats_available

    def __str__(self):
        return f"Flight: [{self.seats_available}]"

    def __add__(self, other):
        if isinstance(other, Flight):
            return self.seats_available + other.seats_available
        return self.seats_available + other

    def __gt__(self, other):
        if isinstance(other, Flight):
            return self.seats_available > other.seats_available
        return self.seats_available > other

# Verification
f1 = Flight("AI-101", 45)
f2 = Flight("BA-202", 120)
print(str(f1))
print(f"Combined Available Seats: {f1 + f2}")
print(f"Does f2 have more seats than f1? {f2 > f1}")


# ### Challenge 31: Encapsulation & Properties
# **Challenge Focus:** Product Pricing Integrity (Instance 4)

# Challenge 31 Solution
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
            raise ValueError(f"Price cannot be negative: {value}")
        self._price = value

# Verification
p = Product("SKU-9901", 149.99)
print(f"Product SKU: {p.sku}, Price: ${p.price}")
try:
    p.price = -20
except ValueError as err:
    print(f"Validation success: {err}")


# ### Challenge 32: Inheritance & super()
# **Challenge Focus:** Finance Platform Margin Accounts (Instance 4)

# Challenge 32 Solution
class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

class MarginAccount(Account):
    def __init__(self, account_id, balance, special_flag):
        super().__init__(account_id, balance)
        self.special_flag = special_flag

# Verification
ma = MarginAccount("ACC-7788", 50000.0, special_flag=True)
print(f"Account ID: {ma.account_id}, Balance: ${ma.balance:,.2f}, Special Flag: {ma.special_flag}")


# ### Challenge 33: Abstract Base Classes
# **Challenge Focus:** Healthcare Architecture ABC Guarantee (Instance 4)

# Challenge 33 Solution
from abc import ABC, abstractmethod

class Patient(ABC):
    def __init__(self, patient_id):
        self.patient_id = patient_id

    @abstractmethod
    def record_vitals(self):
        pass

class ICUPatient(Patient):
    def __init__(self, patient_id, heart_rate, oxygen_level):
        super().__init__(patient_id)
        self.heart_rate = heart_rate
        self.oxygen_level = oxygen_level

    def record_vitals(self):
        return f"ICU Patient {self.patient_id} Vitals: HR={self.heart_rate} bpm, SpO2={self.oxygen_level}%"

# Verification
icu = ICUPatient("P-104", 72, 98)
print(icu.record_vitals())


# ### Challenge 34: Class & Static Methods
# **Challenge Focus:** Smart Home API Parsing & MAC Validation (Instance 4)

# Challenge 34 Solution
class Device:
    def __init__(self, mac_address, temperature):
        self.mac_address = mac_address
        self.temperature = float(temperature)

    @staticmethod
    def validate_mac_address(mac_str):
        return len(str(mac_str)) > 3

    @classmethod
    def from_string(cls, raw_str):
        # String formatted as 'attr2-attr1' -> 'temperature-mac_address'
        parts = raw_str.split("-", 1)
        attr2 = parts[0]
        attr1 = parts[1]
        return cls(mac_address=attr1, temperature=attr2)

# Verification
valid = Device.validate_mac_address("00:1A:2B")
print(f"MAC Valid? {valid}")
dev = Device.from_string("72.5-AA:BB:CC:DD")
print(f"Parsed Device -> MAC: {dev.mac_address}, Temp: {dev.temperature}°F")


# ### Challenge 35: Magic Methods
# **Challenge Focus:** Logistics Shipment Aggregation & Comparison (Instance 4)

# Challenge 35 Solution
class Shipment:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return f"Shipment: [{self.weight}]"

    def __add__(self, other):
        if isinstance(other, Shipment):
            return self.weight + other.weight
        return self.weight + other

    def __gt__(self, other):
        if isinstance(other, Shipment):
            return self.weight > other.weight
        return self.weight > other

# Verification
s1 = Shipment("New York", 150)
s2 = Shipment("London", 275)
print(str(s1))
print(f"Total Weight: {s1 + s2} kg")
print(f"Is s2 heavier than s1? {s2 > s1}")


# ### Challenge 36: Encapsulation & Properties
# **Challenge Focus:** Social Media Post Likes Guard (Instance 4)

# Challenge 36 Solution
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
            raise ValueError(f"Likes cannot be negative: {value}")
        self._likes = value

# Verification
post = Post("POST-1002", 50)
print(f"Post {post.post_id} has {post.likes} likes")
try:
    post.likes = -5
except ValueError as e:
    print(f"Caught negative likes validation: {e}")


# ### Challenge 37: Inheritance & super()
# **Challenge Focus:** EdTech Course & Bootcamp Extension (Instance 4)

# Challenge 37 Solution
class Course:
    def __init__(self, course_code, enrollment):
        self.course_code = course_code
        self.enrollment = enrollment

class Bootcamp(Course):
    def __init__(self, course_code, enrollment, special_flag):
        super().__init__(course_code, enrollment)
        self.special_flag = special_flag

# Verification
bc = Bootcamp("PY-OOP-301", 120, special_flag=True)
print(f"Course: {bc.course_code}, Enrollment: {bc.enrollment}, Special Flag: {bc.special_flag}")


# ### Challenge 38: Abstract Base Classes
# **Challenge Focus:** Gaming Architecture Damage Protocol (Instance 4)

# Challenge 38 Solution
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    @abstractmethod
    def take_damage(self, amount):
        pass

class BossCharacter(Character):
    def __init__(self, name, health=500, shield=50):
        super().__init__(name, health)
        self.shield = shield

    def take_damage(self, amount):
        effective_damage = max(0, amount - self.shield)
        self.health -= effective_damage
        return f"{self.name} took {effective_damage} damage (shield absorbed {min(amount, self.shield)}). Health remaining: {self.health}"

# Verification
boss = BossCharacter("Malakor the Destroyer", 1000, shield=40)
print(boss.take_damage(100))


# ### Challenge 39: Class & Static Methods
# **Challenge Focus:** Cloud Server IP Validation & String Factory (Instance 4)

# Challenge 39 Solution
class Server:
    def __init__(self, ip_address, cpu_load):
        self.ip_address = ip_address
        self.cpu_load = float(cpu_load)

    @staticmethod
    def validate_ip_address(ip_str):
        return len(str(ip_str)) > 3

    @classmethod
    def from_string(cls, raw_str):
        # Formatted as 'attr2-attr1' -> 'cpu_load-ip_address'
        parts = raw_str.split("-", 1)
        attr2 = parts[0]
        attr1 = parts[1]
        return cls(ip_address=attr1, cpu_load=attr2)

# Verification
print(f"Valid IP? {Server.validate_ip_address('192.168.1.1')}")
srv = Server.from_string("84.2-10.0.0.1")
print(f"Server IP: {srv.ip_address}, CPU Load: {srv.cpu_load}%")


# ### Challenge 40: Magic Methods
# **Challenge Focus:** Travel Flight Aggregation & Seat Availability (Instance 4)

# Challenge 40 Solution
class Flight:
    def __init__(self, flight_number, seats_available):
        self.flight_number = flight_number
        self.seats_available = seats_available

    def __str__(self):
        return f"Flight: [{self.seats_available}]"

    def __add__(self, other):
        if isinstance(other, Flight):
            return self.seats_available + other.seats_available
        return self.seats_available + other

    def __gt__(self, other):
        if isinstance(other, Flight):
            return self.seats_available > other.seats_available
        return self.seats_available > other

# Verification
f1 = Flight("AI-101", 45)
f2 = Flight("BA-202", 120)
print(str(f1))
print(f"Combined Available Seats: {f1 + f2}")
print(f"Does f2 have more seats than f1? {f2 > f1}")


# ### Challenge 41: Encapsulation & Properties
# **Challenge Focus:** Product Pricing Integrity (Instance 5)

# Challenge 41 Solution
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
            raise ValueError(f"Price cannot be negative: {value}")
        self._price = value

# Verification
p = Product("SKU-9901", 149.99)
print(f"Product SKU: {p.sku}, Price: ${p.price}")
try:
    p.price = -20
except ValueError as err:
    print(f"Validation success: {err}")


# ### Challenge 42: Inheritance & super()
# **Challenge Focus:** Finance Platform Margin Accounts (Instance 5)

# Challenge 42 Solution
class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

class MarginAccount(Account):
    def __init__(self, account_id, balance, special_flag):
        super().__init__(account_id, balance)
        self.special_flag = special_flag

# Verification
ma = MarginAccount("ACC-7788", 50000.0, special_flag=True)
print(f"Account ID: {ma.account_id}, Balance: ${ma.balance:,.2f}, Special Flag: {ma.special_flag}")


# ### Challenge 43: Abstract Base Classes
# **Challenge Focus:** Healthcare Architecture ABC Guarantee (Instance 5)

# Challenge 43 Solution
from abc import ABC, abstractmethod

class Patient(ABC):
    def __init__(self, patient_id):
        self.patient_id = patient_id

    @abstractmethod
    def record_vitals(self):
        pass

class ICUPatient(Patient):
    def __init__(self, patient_id, heart_rate, oxygen_level):
        super().__init__(patient_id)
        self.heart_rate = heart_rate
        self.oxygen_level = oxygen_level

    def record_vitals(self):
        return f"ICU Patient {self.patient_id} Vitals: HR={self.heart_rate} bpm, SpO2={self.oxygen_level}%"

# Verification
icu = ICUPatient("P-104", 72, 98)
print(icu.record_vitals())


# ### Challenge 44: Class & Static Methods
# **Challenge Focus:** Smart Home API Parsing & MAC Validation (Instance 5)

# Challenge 44 Solution
class Device:
    def __init__(self, mac_address, temperature):
        self.mac_address = mac_address
        self.temperature = float(temperature)

    @staticmethod
    def validate_mac_address(mac_str):
        return len(str(mac_str)) > 3

    @classmethod
    def from_string(cls, raw_str):
        # String formatted as 'attr2-attr1' -> 'temperature-mac_address'
        parts = raw_str.split("-", 1)
        attr2 = parts[0]
        attr1 = parts[1]
        return cls(mac_address=attr1, temperature=attr2)

# Verification
valid = Device.validate_mac_address("00:1A:2B")
print(f"MAC Valid? {valid}")
dev = Device.from_string("72.5-AA:BB:CC:DD")
print(f"Parsed Device -> MAC: {dev.mac_address}, Temp: {dev.temperature}°F")


# ### Challenge 45: Magic Methods
# **Challenge Focus:** Logistics Shipment Aggregation & Comparison (Instance 5)

# Challenge 45 Solution
class Shipment:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return f"Shipment: [{self.weight}]"

    def __add__(self, other):
        if isinstance(other, Shipment):
            return self.weight + other.weight
        return self.weight + other

    def __gt__(self, other):
        if isinstance(other, Shipment):
            return self.weight > other.weight
        return self.weight > other

# Verification
s1 = Shipment("New York", 150)
s2 = Shipment("London", 275)
print(str(s1))
print(f"Total Weight: {s1 + s2} kg")
print(f"Is s2 heavier than s1? {s2 > s1}")


# ### Challenge 46: Encapsulation & Properties
# **Challenge Focus:** Social Media Post Likes Guard (Instance 5)

# Challenge 46 Solution
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
            raise ValueError(f"Likes cannot be negative: {value}")
        self._likes = value

# Verification
post = Post("POST-1002", 50)
print(f"Post {post.post_id} has {post.likes} likes")
try:
    post.likes = -5
except ValueError as e:
    print(f"Caught negative likes validation: {e}")


# ### Challenge 47: Inheritance & super()
# **Challenge Focus:** EdTech Course & Bootcamp Extension (Instance 5)

# Challenge 47 Solution
class Course:
    def __init__(self, course_code, enrollment):
        self.course_code = course_code
        self.enrollment = enrollment

class Bootcamp(Course):
    def __init__(self, course_code, enrollment, special_flag):
        super().__init__(course_code, enrollment)
        self.special_flag = special_flag

# Verification
bc = Bootcamp("PY-OOP-301", 120, special_flag=True)
print(f"Course: {bc.course_code}, Enrollment: {bc.enrollment}, Special Flag: {bc.special_flag}")


# ### Challenge 48: Abstract Base Classes
# **Challenge Focus:** Gaming Architecture Damage Protocol (Instance 5)

# Challenge 48 Solution
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    @abstractmethod
    def take_damage(self, amount):
        pass

class BossCharacter(Character):
    def __init__(self, name, health=500, shield=50):
        super().__init__(name, health)
        self.shield = shield

    def take_damage(self, amount):
        effective_damage = max(0, amount - self.shield)
        self.health -= effective_damage
        return f"{self.name} took {effective_damage} damage (shield absorbed {min(amount, self.shield)}). Health remaining: {self.health}"

# Verification
boss = BossCharacter("Malakor the Destroyer", 1000, shield=40)
print(boss.take_damage(100))


# ### Challenge 49: Class & Static Methods
# **Challenge Focus:** Cloud Server IP Validation & String Factory (Instance 5)

# Challenge 49 Solution
class Server:
    def __init__(self, ip_address, cpu_load):
        self.ip_address = ip_address
        self.cpu_load = float(cpu_load)

    @staticmethod
    def validate_ip_address(ip_str):
        return len(str(ip_str)) > 3

    @classmethod
    def from_string(cls, raw_str):
        # Formatted as 'attr2-attr1' -> 'cpu_load-ip_address'
        parts = raw_str.split("-", 1)
        attr2 = parts[0]
        attr1 = parts[1]
        return cls(ip_address=attr1, cpu_load=attr2)

# Verification
print(f"Valid IP? {Server.validate_ip_address('192.168.1.1')}")
srv = Server.from_string("84.2-10.0.0.1")
print(f"Server IP: {srv.ip_address}, CPU Load: {srv.cpu_load}%")


# ### Challenge 50: Magic Methods
# **Challenge Focus:** Travel Flight Aggregation & Seat Availability (Instance 5)

# Challenge 50 Solution
class Flight:
    def __init__(self, flight_number, seats_available):
        self.flight_number = flight_number
        self.seats_available = seats_available

    def __str__(self):
        return f"Flight: [{self.seats_available}]"

    def __add__(self, other):
        if isinstance(other, Flight):
            return self.seats_available + other.seats_available
        return self.seats_available + other

    def __gt__(self, other):
        if isinstance(other, Flight):
            return self.seats_available > other.seats_available
        return self.seats_available > other

# Verification
f1 = Flight("AI-101", 45)
f2 = Flight("BA-202", 120)
print(str(f1))
print(f"Combined Available Seats: {f1 + f2}")
print(f"Does f2 have more seats than f1? {f2 > f1}")

