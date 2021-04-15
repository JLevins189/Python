#!/usr/bin/python3

# Use the exchangeratesapi.io to perform currency conversions.
# https://api.exchangeratesapi.io/latest?base=EUR&symbols=USD

import urllib.request
import json


class Currency:
    """This class allows an amount and a currency to be assigned to an instance
       Instances, floats and ints can be added to form sums of instances in a new instance
       The same can be done with subtractions and instances can be compared if they are greater than or not
       Currencies can be converted from one to another
       Cross currency addition and subtraction and greater than comparisons are allowed
       Ints or floats used with instances are assumed to be of the same currency as the said instance
       This program uses a database API for live conversions

    """

    VALID_CURRENCIES = ['USD', 'EUR', 'GBP', 'AUD', 'CAD',
                        'CNY', 'ILS', 'MXN', 'RUB', 'THB', 'BRL']

    def __init__(self, amount=1, currency_type='USD'):
        # a quick way of checking for valid currencies
        # for a limited subset of valid currencies
        if currency_type in Currency.VALID_CURRENCIES:
            self.amount = amount
            self.currency_type = currency_type
        else:
            print("Invalid currency type: %s\n", currency_type)
            self.amount = 0
            self.currency_type = ''

    def convert_to(self, new_currency_type):
        if new_currency_type == self.currency_type:
            # nothing to do
            return Currency(self.amount, self.currency_type)

        if new_currency_type not in Currency.VALID_CURRENCIES \
                or self.currency_type not in Currency.VALID_CURRENCIES:
            print("Conversion from {} to {} not allowed".format(self.currency_type, new_currency_type))
            return

        # prepare URL
        url = "https://api.exchangeratesapi.io/latest?base="
        url += self.currency_type
        url += "&symbols=" + new_currency_type
        conv = urllib.request.urlopen(url)
        # read() returns an array of bytes, we want a string decoded in UTF-8
        response = conv.read().decode('UTF-8')

        # Extract the exchange rate from the variable 'response' and finish the implementation of the method.
        # The return is given. Amount is the the correct converted amount that needs to be found

        # prepare/implement exchange
        master_dict = json.loads(response)  # creates outer dict from response
        inner_dict = master_dict["rates"]  # creates inner dict of "rates" dict
        exchange_rate1 = inner_dict[new_currency_type]
        amount = self.amount * exchange_rate1

        print("{} {} => {} {}".format(self.amount, self.currency_type, amount, new_currency_type))
        return Currency(amount, new_currency_type)

    def __str__(self):
        return "{} {}".format(self.amount, self.currency_type)

    def __repr__(self):
        return "{} {}".format(self.amount, self.currency_type)

    def __add__(self, other_curr):
        try:
            if self.currency_type == other_curr.currency_type:  # same currency
                sum1 = self.amount + other_curr.amount  # just add
                sum_return = Currency(sum1, self.currency_type)  # return sum
            else:
                temp_other_curr = other_curr.convert_to(self.currency_type)  # other_curr has different currency attribute
                sum1 = self.amount + temp_other_curr.amount  # add after conversion
                sum_return = Currency(sum1, self.currency_type)  # return sum
        except AttributeError:
            sum1 = self.amount + other_curr  # other curr is float/int and has no currency
            sum_return = Currency(sum1, self.currency_type)  # assume currency of float is same as first

        return sum_return  # return the sum and its currency

    def __sub__(self, other_curr):
        try:
            if self.currency_type == other_curr.currency_type:  # same currency
                sub1 = self.amount - other_curr.amount  # just sub
                sub_return = Currency(sub1, self.currency_type)  # return sub
            else:
                temp_other_curr = other_curr.convert_to(
                    self.currency_type)  # other_curr has different currency attribute
                sub1 = self.amount - temp_other_curr.amount  # sub after conversion
                sub_return = Currency(sub1, self.currency_type)  # return sub
        except AttributeError:
            sub1 = self.amount - other_curr  # other curr is float/int and has no currency
            sub_return = Currency(sub1, self.currency_type)  # assume currency of float is same as first

        return sub_return  # return the sum and its currency

    def __radd__(self, other_curr):
        try:
            if self == other_curr.currency_type:  # same currency
                sum1 = self.amount + other_curr.amount  # just add
                sum_return = Currency(sum1, self.currency_type)  # return sum
            else:
                temp_other_curr = other_curr.convert_to(
                    self.currency_type)  # other_curr has different currency attribute
                sum1 = self.amount + temp_other_curr.amount  # add after conversion
                sum_return = Currency(sum1, self.currency_type)  # return sum
        except AttributeError:
            sum1 = self.amount + other_curr  # other curr is float/int and has no currency
            sum_return = Currency(sum1, self.currency_type)  # assume currency of float is same as first

        return sum_return  # return the sum and its currency

    def __rsub__(self, other_curr):  # flip order of subtraction # a-b --> b-a
        try:
            if self.currency_type == other_curr.currency_type:  # same currency
                sub1 = other_curr.amount - self.amount  # just sub
                sub_return = Currency(sub1, self.currency_type)  # return sub
            else:
                temp_other_curr = other_curr.convert_to(self.currency_type)  # other_curr has different currency attribute
                sub1 = temp_other_curr.amount - self.amount  # sub after conversion
                sub_return = Currency(sub1, self.currency_type)  # return sub
        except AttributeError:
            sub1 = other_curr - self.amount  # other curr is float/int and has no currency
            sub_return = Currency(sub1, self.currency_type)  # assume currency of float is same as first

        return sub_return  # return the sum and its currency

    def __gt__(self, other_curr):
        try:
            if self.currency_type == other_curr.currency_type:  # same currency
                if self.amount > other_curr.amount:
                    return True
                else:
                    return False
            else:
                temp_other_curr = other_curr.convert_to(self.currency_type)  # other_curr has different currency attribute
                if self.amount > temp_other_curr.amount:
                    return True
                else:
                    return False
        except AttributeError:
            if self.amount > other_curr:  # assume same currency when none given
                return True
            else:
                return False


# This main is incomplete because not all methods are tested
# Some outputs are given by the comments next to the commands. Your code should be able to output these when
# you remove the '#' in the beginning of the lines

curr = Currency(7.50, 'USD')
print(curr)  # 7.50 USD
curr2 = Currency(2, 'EUR')
print(curr2)  # 2.00 EUR

# convert
print("\nconvert")
new_curr = curr2.convert_to(curr.currency_type)  # 2.000000 EUR => 2.211600 USD
print(new_curr)  # 2.21 USD

# add
print("\nadd")
sum_curr = curr + curr2  # 2.000000 EUR => 2.211600 USD
print(sum_curr)  # 9.71 USD

# sub
print("\nsub")
sub_curr = curr - curr2
print(sub_curr)  # 5.122 USD

# radd
print("\nradd")
sum_curr2 = 5.5 + curr
print(sum_curr2)  # 13.00 USD

# rsub
print("\nrsub")
sub_curr2 = 5.5 - curr2
print(sub_curr2)  # 3.50 EUR

# gt
print("\ngt")
gt1 = sub_curr > curr
print(gt1)
