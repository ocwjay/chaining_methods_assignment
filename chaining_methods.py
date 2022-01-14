#USING SAME CODE AS USER_ASSIGNMENT AND MODIFYING TO HAVE CHAINED METHODS
#Defining user class
class user():
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f'User: {self.name}, ${self.account_balance}')
        return self
    def transfer_money(self, otherUser, amount):
        print(f'{self.name} transferred ${amount} to {otherUser.name}')
        self.account_balance -= amount
        otherUser.account_balance += amount
        print(f'User: {self.name}, ${self.account_balance}')
        print(f'User: {otherUser.name}, ${otherUser.account_balance}')
        return self

#Making users
robert = user('Robert', 'robert@someaddress.com')
eric = user('Eric', 'eric@someaddress.com')
jay = user('Jay', 'jay@someaddress.com')

#the first user makes 3 deposits and one withdrawal. then we display their balance
robert.make_deposit(320).make_deposit(150).make_deposit(804).make_withdrawal(600).display_user_balance()
#the second user makes 2 deposits and 2 withdrawals. then we display their balance
eric.make_deposit(2400).make_deposit(780).make_withdrawal(48).make_withdrawal(206).display_user_balance()
#the third user makes 1 deposit and 3 withdrawals. then we display their balance
jay.make_deposit(964).make_withdrawal(94).make_withdrawal(200).make_withdrawal(63).display_user_balance()

#BONUS: create transfer method. Have the first user transfer money to the second user, and display both users' balances
robert.transfer_money(jay, 52)