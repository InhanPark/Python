# account.py
"""Account class definition"""
from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance."""
    def __init__(self, name, balance):
        """Initialize an Account object."""
        # 이 부분에서 실제저장장소가 memory 에 만들어지므로 constructor 라고 부른다.
                
        # if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')

        # 이 부분이 class 라는 custom data structure 이다.
        # 이 부분은 Account class 가 사용될때마다 memory 에 만들어진다.
        self.name = name
        self.balance = balance
 
    # function 에 해당하는 method 들은 실제로는 memory 의 code 영역에 한번만 만들고 모든 Account class 들이 공유하여 사용한다.
    # library function 을 쓰는것과 같다. 단 사용할때 이름을 붙이는 방법이 다를뿐이다.
    def deposit(self, amount):
        """Deposit money to the account"""

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')
        
        self.balance += amount
        
    def withdraw(self, amount):
        """Withdraw money from the account"""
        
        # if amount is greater than balance, raise an exception
        if amount > self.balance:
            raise ValueError('amount must be <= to balance.')
        elif amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')
        
        self.balance -= amount


# class test
if __name__ == '__main__':

    account1 = Account('Donald Duck', Decimal('50.00'))
    print(account1.name, account1.balance)