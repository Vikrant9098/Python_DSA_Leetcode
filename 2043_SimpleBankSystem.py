class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balance = balance  # Store all account balances

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        # Check if both accounts are valid
        if not self.is_valid(account1) or not self.is_valid(account2):
            return False
        # Check if account1 has enough balance
        if self.balance[account1 - 1] < money:
            return False
        # Perform the transfer
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        # Check if account is valid
        if not self.is_valid(account):
            return False
        # Add money to the account
        self.balance[account - 1] += money
        return True

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        # Check if account is valid
        if not self.is_valid(account):
            return False
        # Check if account has enough balance
        if self.balance[account - 1] < money:
            return False
        # Deduct money
        self.balance[account - 1] -= money
        return True

    def is_valid(self, account):
        # Helper function to check valid account number
        return 1 <= account <= len(self.balance)


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1, account2, money)
# param_2 = obj.deposit(account, money)
# param_3 = obj.withdraw(account, money)
