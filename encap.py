# Encapsulation :- with the help of Encapsulation we can deside that what kind of attribute show or hide as well as protect
from constructor_method import name1


# Using the class
class User:
    def __init__(self, email, password):
        self.__email = email  # Private variable
        self.__password = password  # Private variable

    def set_email(self, email):
        # Email validation can be added here
        self.__email = email

    def get_email(self):
        return self.__email  # Getter method

    def set_password(self, password):
        # Password validation can be added here
        self.__password = password

    def get_password(self):
        return "Access Denied"  # Avoid returning the actual password

user = User("user@example.com", "securepassword")

# Accessing the email
print(user.get_email())  # Output: user@example.com

# Attempt to access the password directly (will raise an error)
# print(user.__password)  # AttributeError

# Accessing the password using the getter method (but it denies access)
print(user.get_password())  # Output: Access Denied

# Changing the email and password
user.set_email("new_email@example.com")
user.set_password("new_securepassword")

print(user.get_email())  # Output: new_email@example.com
print()



# next example of Encapsulation
class BankingAccount:

    def __init__(self,owner,balance =0):
        self.owner = owner
        self.__balance = balance


    def deposite(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposite: {amount}.Available Balance: {self.__balance}")
        else:
            print("No transaction")


    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Debited amount: {amount},Available balance: {self.__balance} ")
        else:
            print("Insufficient Balance, Try next time...")


    def get_balance(self):
        return(self.__balance)

ac = BankingAccount("Mac",75500)
ac.deposite(25000)
ac.withdraw(500)
print(f"Available Balance:{ac.get_balance()}")
print()


class School:

    def __init__(self):
        self.__name = ""

    def get_name(self):
        return self.__name

    def set_name(self,oxford):
        self.__name = oxford

obj = School()
obj.set_name("Howard")
print(obj.get_name())
print()


class Student:
    def __init__(self):
        self.__name = ""

    def get_name(self):
        return self.__name

    def set_name(self,vikas):
        self.__name = vikas

obj1 = Student()
obj1.set_name("Dhamma")
print(obj1.get_name())