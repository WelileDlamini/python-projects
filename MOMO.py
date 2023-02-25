
# how momo works

class MobileMoney:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print( f"You have deposited {amount} units. Your new balance is {self.balance} units." )

    def withdraw(self, amount):
        if self.balance < amount:
            print( "Insufficient funds!" )
        else:
            self.balance -= amount
            print( f"You have withdrawn {amount} units. Your new balance is {self.balance} units." )

    def send_money(self, recipient, amount):
        if self.balance < amount:
            print( "Insufficient funds!" )
        else:
            self.balance -= amount
            recipient.deposit( amount )
            print( f"You have sent {amount} units to {recipient.name}. Your new balance is {self.balance} units." )
