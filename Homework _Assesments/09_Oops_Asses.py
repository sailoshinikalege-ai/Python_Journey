#Q1 .SMARTDEVICES

class SmartDevice:
    device_name = 'Smart Light'
    device_type = 'Lighting'

d1 = SmartDevice()

print("Device Name:", d1.device_name)
print("Device Type:", d1.device_type)

#Q2. MENU

class FoodItem:
    food_name='Chicken Biryani'
    quantity=2
    price=500

f1 = FoodItem()

print('Food item :',f1.food_name)
print('Quantity:',f1.quantity)
print('Price:',f1.price)

#Q3

class FitnessTracker:
    user ='Nikky'
    steps =1000

u1 = FitnessTracker()

print('UserName:',u1.user)
print('Steps:',u1.steps)

#Q4
class MovieTicket:
    movie_name = 'Paradise'
    seat_num = 'K9'

m1 = MovieTicket()

print('Movie Name:',m1.movie_name)
print('Seat Number:',m1.seat_num)

#Q5

class DigitalWallet:
    owner = 'Nikky'
    balance = 2000

o1 = DigitalWallet()

print('Owner Nmae:',o1.owner)
print('Balnace:',o1.balance)

#Q6

class Pet:
    pet_name = 'Bruno'
    pet_type = 'Dog'
    age = 3

p1 = Pet()

print("Pet Name:", p1.pet_name)
print("Pet Type:", p1.pet_type)
print("Age:", p1.age)

#Q7

class TravelPackage:
    destination ='New York'
    days = 'One way'
    price ='1.5 lakh'

t1 = TravelPackage()

print("Destination:",t1.destination)
print("Days:",t1.days)
print("Price:",t1.price)

#Q8

class LibraryMember:
    member_name ='Loshini'
    member_id = 1804
    books_issued= 3

l1 = LibraryMember()

print("Member Name:",l1.member_id)
print('Member Id:',l1.member_id)
print('Books Issued:',l1.books_issued)

#Q9
class OnlineCourse():
    course_name = 'Python'
    instructor = 'Akansha'
    duration = '9 months'

c1 = OnlineCourse()

print('Course Name:',c1.course_name)
print('Instructor:',c1.instructor)
print('Duration:',c1.duration)

#Q10

class ElectricScooter:
    brand = 'Ola'
    battery_level = '90%'
    range = '120km' 

e1 = ElectricScooter()

print('Brand Name:', e1.brand)
print('Battery Level:',e1.battery_level)
print('Range:',e1.range)

#Q11. Menu

class MenuItem:
    item = ""
    price = 0

item1 = MenuItem()
item1.item = "Burger"
item1.price = 150

item2 = MenuItem()
item2.item = "Pasta"
item2.price = 200

item3 = MenuItem()
item3.item = "Pizza"
item3.price = 250

print("Item 1:", item1.item, "-", item1.price)
print("Item 2:", item2.item, "-", item2.price)
print("Item 3:", item3.item, "-", item3.price)

# Q12. Patient List

class Patient:
    patient_name = ''
    disease = ''

p1 = Patient()
p1.patient_name = 'Pradeep'
p1.disease = 'Lung Cancer'

p2 = Patient()
p2.patient_name = 'Somya'
p2.disease = 'Pneumonia'

print('Patient 1:', p1.patient_name, ',', p1.disease)
print('Patient 2:', p2.patient_name, ',', p2.disease)

# Q13. Flight Booking

class Flight:
    flight_number = ""
    destination = ""


flight1 = Flight()
flight1.flight_number = "AI101"
flight1.destination = "Delhi"

flight2 = Flight()
flight2.flight_number = "AI202"
flight2.destination = "Mumbai"

flight3 = Flight()
flight3.flight_number = "AI303"
flight3.destination = "Chennai"

print("Flight 1:", flight1.flight_number, ",", flight1.destination)
print("Flight 2:", flight2.flight_number, ",", flight2.destination)
print("Flight 3:", flight3.flight_number, ",", flight3.destination)


# Q14. Gaming Characters

class GameCharacter:
    character_name = ""
    power = 0


character1 = GameCharacter()
character1.character_name = "Warrior"
character1.power = 90

character2 = GameCharacter()
character2.character_name = "Wizard"
character2.power = 85

print("Character 1:", character1.character_name, ",", character1.power)
print("Character 2:", character2.character_name, ",", character2.power)


# Q15. Online Shopping Cart

class Product:
    product_name = ""
    price = 0
    quantity = 0


product1 = Product()
product1.product_name = "Laptop"
product1.price = 50000
product1.quantity = 1

product2 = Product()
product2.product_name = "Mouse"
product2.price = 800
product2.quantity = 2

product3 = Product()
product3.product_name = "Keyboard"
product3.price = 1500
product3.quantity = 1

print("Product 1:", product1.product_name, product1.price, product1.quantity)
print("Product 2:", product2.product_name, product2.price, product2.quantity)
print("Product 3:", product3.product_name, product3.price, product3.quantity)



# ============================================================
# SECTION D: GENERIC STATE
# ============================================================

# Q16. Smart Watch

class SmartWatch:
    brand = ""
    model = ""
    battery = ""


print("Brand")
print("Model")
print("Battery")


# Q17. Restaurant Table

class RestaurantTable:
    table_number = 0
    capacity = 0
    location = ""


print("Table Number")
print("Capacity")
print("Location")


# Q18. Electric Vehicle

class ElectricVehicle:
    brand = ""
    battery_capacity = ""
    charging_time = ""


print("Brand")
print("Battery Capacity")
print("Charging Time")


# Q19. Social Media Profile

class SocialMediaProfile:
    username = ""
    followers = 0
    account_type = ""


print("Username")
print("Followers")
print("Account Type")


# Q20. Hotel Room

class HotelRoom:
    room_number = 0
    room_type = ""
    price_per_night = 0


print("Room Number")
print("Room Type")
print("Price Per Night")



# ============================================================
# SECTION E: SPECIFIC STATE
# ============================================================

# Q21. Smart Watch Objects

class SmartWatch:
    brand = ""
    battery = ""


watch1 = SmartWatch()
watch1.brand = "Apple"
watch1.battery = "90%"

watch2 = SmartWatch()
watch2.brand = "Samsung"
watch2.battery = "75%"

print("Watch 1:")
print("Brand:", watch1.brand)
print("Battery:", watch1.battery)

print("Watch 2:")
print("Brand:", watch2.brand)
print("Battery:", watch2.battery)


# Q22. Hotel Room Objects

class HotelRoom:
    room_number = 0
    room_type = ""


room1 = HotelRoom()
room1.room_number = 101
room1.room_type = "Deluxe"

room2 = HotelRoom()
room2.room_number = 202
room2.room_type = "Suite"

print("Room 1:")
print("Number:", room1.room_number)
print("Type:", room1.room_type)

print("Room 2:")
print("Number:", room2.room_number)
print("Type:", room2.room_type)


# Q23. Gaming Characters

class GameCharacter:
    name = ""
    level = 0
    power = 0


character1 = GameCharacter()
character1.name = "Warrior"
character1.level = 10
character1.power = 90

character2 = GameCharacter()
character2.name = "Wizard"
character2.level = 8
character2.power = 85

print("Character 1:")
print("Name:", character1.name)
print("Level:", character1.level)
print("Power:", character1.power)

print("Character 2:")
print("Name:", character2.name)
print("Level:", character2.level)
print("Power:", character2.power)


# Q24. Travel Packages

class TravelPackage:
    destination = ""
    price = 0
    duration = 0


package1 = TravelPackage()
package1.destination = "Goa"
package1.price = 12000
package1.duration = 4

package2 = TravelPackage()
package2.destination = "Manali"
package2.price = 18000
package2.duration = 5

print("Package 1:")
print("Destination:", package1.destination)
print("Price:", package1.price)
print("Duration:", package1.duration)

print("Package 2:")
print("Destination:", package2.destination)
print("Price:", package2.price)
print("Duration:", package2.duration)


# Q25. Digital Wallets

class DigitalWallet:
    owner = ""
    balance = 0


wallet1 = DigitalWallet()
wallet1.owner = "Rahul"
wallet1.balance = 2500

wallet2 = DigitalWallet()
wallet2.owner = "Priya"
wallet2.balance = 4000

print("Wallet 1:")
print("Owner:", wallet1.owner)
print("Balance:", wallet1.balance)

print("Wallet 2:")
print("Owner:", wallet2.owner)
print("Balance:", wallet2.balance)



# ============================================================
# SECTION F: CONSTRUCTOR
# ============================================================

# Q26. Food Delivery Order

class FoodOrder:

    def __init__(self, customer_name, food_name, amount):
        self.customer_name = customer_name
        self.food_name = food_name
        self.amount = amount


order1 = FoodOrder("Rahul", "Pizza", 250)
order2 = FoodOrder("Priya", "Burger", 180)

print("Customer:", order1.customer_name)
print("Food:", order1.food_name)
print("Amount:", order1.amount)

print("Customer:", order2.customer_name)
print("Food:", order2.food_name)
print("Amount:", order2.amount)


# Q27. Movie Ticket Booking

class MovieTicket:

    def __init__(self, movie_name, seat_number, ticket_price):
        self.movie_name = movie_name
        self.seat_number = seat_number
        self.ticket_price = ticket_price


ticket1 = MovieTicket("Avengers", "A12", 250)
ticket2 = MovieTicket("Avatar", "B15", 300)

print("Movie:", ticket1.movie_name)
print("Seat:", ticket1.seat_number)
print("Price:", ticket1.ticket_price)

print("Movie:", ticket2.movie_name)
print("Seat:", ticket2.seat_number)
print("Price:", ticket2.ticket_price)


# Q28. Hospital Appointment

class Appointment:

    def __init__(self, patient_name, doctor_name, appointment_time):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.appointment_time = appointment_time


appointment1 = Appointment("Anu", "Dr. Raj", "10:30 AM")
appointment2 = Appointment("Rahul", "Dr. Kumar", "11:30 AM")

print("Patient:", appointment1.patient_name)
print("Doctor:", appointment1.doctor_name)
print("Time:", appointment1.appointment_time)

print("Patient:", appointment2.patient_name)
print("Doctor:", appointment2.doctor_name)
print("Time:", appointment2.appointment_time)


# Q29. Online Shopping Order

class ShoppingOrder:

    def __init__(self, product_name, quantity, price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price


order1 = ShoppingOrder("Laptop", 1, 50000)
order2 = ShoppingOrder("Mouse", 2, 800)

print("Product:", order1.product_name)
print("Quantity:", order1.quantity)
print("Price:", order1.price)

print("Product:", order2.product_name)
print("Quantity:", order2.quantity)
print("Price:", order2.price)


# Q30. Cab Booking

class CabBooking:

    def __init__(self, passenger_name, pickup_location, destination):
        self.passenger_name = passenger_name
        self.pickup_location = pickup_location
        self.destination = destination


cab1 = CabBooking("Rahul", "MG Road", "Airport")
cab2 = CabBooking("Priya", "Banjara Hills", "Secunderabad")

print("Passenger:", cab1.passenger_name)
print("Pickup:", cab1.pickup_location)
print("Destination:", cab1.destination)

print("Passenger:", cab2.passenger_name)
print("Pickup:", cab2.pickup_location)
print("Destination:", cab2.destination)



# ============================================================
# SECTION G: OBJECT METHOD
# ============================================================

# Q31. Food Order Bill

class FoodOrder:

    def __init__(self, food_name, price, quantity):
        self.food_name = food_name
        self.price = price
        self.quantity = quantity

    def calculate_bill(self):
        return self.price * self.quantity


food_order = FoodOrder("Burger", 150, 3)

print("Food:", food_order.food_name)
print("Price:", food_order.price)
print("Quantity:", food_order.quantity)
print("Total Bill:", food_order.calculate_bill())


# Q32. Fitness Tracker

class FitnessTracker:

    def __init__(self, user_name, steps):
        self.user_name = user_name
        self.steps = steps

    def display_steps(self):
        print("User:", self.user_name)
        print("Steps:", self.steps)


tracker = FitnessTracker("Rahul", 8000)

tracker.display_steps()


# Q33. Bank Account

class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Updated Balance:", self.balance)


account = BankAccount("Priya", 5000)

print("Account Holder:", account.account_holder)
print("Initial Balance:", account.balance)

account.deposit(2000)


# Q34. Electricity Bill

class ElectricityBill:

    def __init__(self, customer_name, units):
        self.customer_name = customer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 5
        else:
            bill = self.units * 8

        return bill


electricity = ElectricityBill("Rahul", 150)

print("Customer:", electricity.customer_name)
print("Units:", electricity.units)
print("Bill:", electricity.calculate_bill())


# Q35. Shopping Cart

class ShoppingCart:

    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity


cart = ShoppingCart("Keyboard", 1500, 2)

print("Product:", cart.product_name)
print("Price:", cart.price)
print("Quantity:", cart.quantity)
print("Total:", cart.calculate_total())



# ============================================================
# SECTION H: CLASS METHOD
# ============================================================

# Q36. Company Employee System

class Employee:
    company_name = "ABC Technologies"

    @classmethod
    def display_company(cls):
        print("Company Name:", cls.company_name)


Employee.display_company()


# Q37. School Information System

class Student:
    school_name = "Delhi Public School"

    @classmethod
    def display_school(cls):
        print("School Name:", cls.school_name)


Student.display_school()


# Q38. Bank Information System

class Bank:
    bank_name = "State Bank"

    @classmethod
    def display_bank(cls):
        print("Bank Name:", cls.bank_name)


Bank.display_bank()


# Q39. Restaurant Information System

class Restaurant:
    restaurant_name = "Food Corner"

    @classmethod
    def display_restaurant(cls):
        print("Restaurant Name:", cls.restaurant_name)


Restaurant.display_restaurant()


# Q40. Gaming Company

class Game:
    company_name = "GameZone"

    @classmethod
    def display_company(cls):
        print("Gaming Company:", cls.company_name)


Game.display_company()



# ============================================================
# SECTION I: STATIC METHOD
# ============================================================

# Q41. Electricity Unit Checker

class Electricity:

    @staticmethod
    def check_units(units):
        if units > 100:
            print("High Usage")
        else:
            print("Normal Usage")


Electricity.check_units(150)


# Q42. Food Delivery Discount

class FoodDelivery:

    @staticmethod
    def calculate_discount(amount):
        if amount > 1000:
            discount = amount * 10 / 100
        else:
            discount = 0

        final_amount = amount - discount

        print("Amount:", amount)
        print("Discount:", discount)
        print("Final Amount:", final_amount)


FoodDelivery.calculate_discount(1500)


# Q43. Age Eligibility Checker

class Eligibility:

    @staticmethod
    def check_age(age):
        if age >= 18:
            print("Eligible")
        else:
            print("Not Eligible")


Eligibility.check_age(20)


# Q44. Temperature Converter

class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 9 / 5) + 32

        print("Celsius:", celsius)
        print("Fahrenheit:", fahrenheit)


Temperature.celsius_to_fahrenheit(30)


# Q45. Parking Fee Calculator

class Parking:

    @staticmethod
    def calculate_fee(hours):
        if hours <= 2:
            fee = 50
        else:
            fee = hours * 30

        print("Hours:", hours)
        print("Parking Fee:", fee)


Parking.calculate_fee(4)

