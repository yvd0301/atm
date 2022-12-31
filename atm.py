import abc
import random
import itertools


class CardInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def check_pin(self, pin_number):
        pass

    @abc.abstractmethod
    def connect_account(self, account):
        pass

    @abc.abstractmethod
    def get_account_numbers(self):
        pass

    @abc.abstractmethod
    def get_account_number(self, account_number):
        pass

    @abc.abstractmethod
    def get_balance(self, account_number):
        pass

    @abc.abstractmethod
    def deposit(self, account_number, money):
        pass

    @abc.abstractmethod
    def withdraw(self, account_number, money):
        pass


class Card(CardInterface):
    __account = []

    def __init__(self):
        # generate card number by bank
        self.card_number = random.choice(list(itertools.combinations('123456789', 5)))
        self.__pin_number = 1234

    def check_pin(self, pin_number):
        return True if pin_number == self.__pin_number else False

    def connect_account(self, account):
        if isinstance(account, Account):
            self.__account.append(account)
        else:
            raise Exception('invalid account')

    def get_account_numbers(self):
        return [i.get_account_number() for i in self.__account]

    def get_account_number(self, account_number):
        accounts = self.get_account_numbers()
        if account_number in accounts:
            return account_number
        else:
            None

    def get_balance(self, account_number):
        return self.__account[account_number].get_balance()

    def deposit(self, account_number, money):
        self.__account[account_number].deposit(money)

    def withdraw(self, account_number, money):
        self.__account[account_number].withdraw(money)


class Account:

    def __init__(self):
        self.account_number = 0
        self.balance = 0

    def set_account(self, account_number):
        self.account_number = account_number

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance

    def deposit(self, money):
        self.balance = money

    def withdraw(self, money):
        if self.balance - money >= 0:
            self.balance -= money
        else:
            raise Exception("not enough balance")


class AtmInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def insert_card(self, card):
        pass

    @abc.abstractmethod
    def get_account_number(self, pin):
        pass

    @abc.abstractmethod
    def select_account(self, account_number):
        pass

    @abc.abstractmethod
    def see_balance(self, pin, account_number):
        pass


class Atm(AtmInterface):

    def insert_card(self, card):
        if isinstance(card, Card):
            self.__card = card
        else:
            raise Exception('invalid card')

    # input pin number
    def input_pin(self, pin):
        return True if self.__card.check_pin(pin) else False

    # For showing account number on ATM
    def get_account_number(self, pin):
        if self.input_pin(pin):
            return self.__card.get_account_numbers()

    # Select Account
    def select_account(self, account_number):
        return self.__card.get_account_number(account_number)

    # See balance
    def see_balance(self, pin, account_number):
        if self.input_pin(pin) and self.select_account(account_number):
            return self.__card.get_balance(account_number)
        else:
            raise Exception('invalid pin')

    # Deposit
    def deposit(self, pin, account_number, money):
        if self.input_pin(pin) and self.select_account(account_number):
            return self.__card.deposit(account_number, money)
        else:
            raise Exception('invalid pin')

    # Withdraw
    def withdraw(self, pin, account_number, money):
        if self.input_pin(pin) and self.select_account(account_number):
            return self.__card.withdraw(account_number, money)
        else:
            raise Exception('invalid pin')
