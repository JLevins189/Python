"""CA2 by Jack Levins (C19335843)
Throughout the program the "shopping cart" may be referred to as a "basket"
This program was built to replicate an online store with
    a shopping cart
    product list
    customer differentiation
    checkout
    and much more
This program aims to allow user to shop as they would online
It is based off a command line interface to provide the customer with options continuously
until the user chooses to quit
"""

# import
import time
import random
import sys


# classes

# customers
class Customer():
    def __init__(self, name="", address="", acc_ID1=0, currency_type='eur'):
        """this method initialises the key arguments of the class initialisation

           Keywords:                                Defaults:
           name: customer's name                    Blank String
           address: customer's address              Blank String
           acc_ID1: customer's ID                   0
           currency_type: customer's currency used  Euro
           """
        self.name1 = name  # customer's name
        self.address = address  # customer's address
        self.acc_ID = acc_ID1  # customer's ID
        self.currency_type = currency_type  # customer's preferred currency to pay

    def __str__(self):
        """this method displays the contents of the init function in a user-friendly way to the customer
           """
        return "Customer Name: {}\nCustomer Address: {}\nAccount ID: {}\nCurrency: {}\n".format(self.name1, self.address,
                                                                                                self.acc_ID, self.currency_type)


class BargainHunter(Customer):
    def __init__(self, name="", address="", acc_num=0, currency_type='eur'):
        """this method initialises the key arguments of the class initialisation
           using the master customer class' init function
           it adds the exclusive variable to be used as an argument to the shopping functions
           to allow or disallow access to exclusive products
        """
        Customer.__init__(self, name, address, acc_num, currency_type)
        self.exclusive = False  # not technically private as it is chosen based on menu system

    def __str__(self):
        """this method using function from the master Customer() class and
           adds the a string if the user is allowed to buy exclusive products or not
           """
        result_str = Customer.__str__(self)
        result_str += "Exclusive Product Access: {}\n".format("No")  # add the exclusive product string to the master string
        return result_str


class LoyalCustomer(Customer):
    def __init__(self, name="", address="", acc_num=0, currency_type='eur'):
        """this method initialises the key arguments of the class initialisation
           using the master customer class' init function
           it adds the exclusive variable to be used as an argument to the shopping functions
           to allow or disallow access to exclusive products
        """
        Customer.__init__(self, name, address, acc_num, currency_type)
        self.exclusive = True  # not technically private as it is chosen based on menu system

    def __str__(self):
        """this method uses the string function from the master Customer() class and
         adds the a string if the user is allowed to buy exclusive products or not"""
        result_str = Customer.__str__(self)
        result_str += "Exclusive Product Access: {}\n".format("Yes")  # add the exclusive product string to the master string
        return result_str


# shopping items
class ShoppingCart():
    def __init__(self, customer=BargainHunter()):  # default to a non-exclusive customer
        """this method initialises the key arguments of the class initialisation

           Keywords:                                Defaults:
           products_quantity                        Empty dictionary
           total_products: list of items in basket  Empty List
           amount: total cost of basket             0
           customer: customer using basket          BargainHunter ... i.e. non-exclusive
           exclusive1: exclusive product access     False
           currency_type: customer's currency used  Euro
           """
        self.products_quantity = {}  # basket product and quantity in basket (public)
        self.total_products = []  # list of products in basket (public)
        self.amount = 0  # amount to pay (private until checkout)
        self.customer = customer  # (private)
        self.exclusive1 = customer.exclusive  # check if the customer has exclusive access (printed on customer creation)
        self.currency_type = customer.currency_type  # printed on customer creation

    def __str__(self):  # get for basket/cart
        """This method displays the items in basket list as well as the subtotal before delivery
           The amount given is in the user's preferred currency
        """
        if self.currency_type == 'eur':
            return "Items in basket: {} \nBasket Total: €{} \n".format(', '.join(self.total_products), self.amount)
        elif self.currency_type == 'usd':
            return "Items in basket: {} \nBasket Total: ${} \n".format(', '.join(self.total_products), self.amount)
        elif self.currency_type == 'gbp':
            return "Items in basket: {} \nBasket Total: £{} \n".format(', '.join(self.total_products), self.amount)

    def get_amount(self):  # to see price of basket
        return self.amount

    def get_customer(self):  # to see the customer
        return self.customer

    def add_item(self, item):  # set for basket/cart items using amount, products_quantity
        """This function allows a customer to add an item in the products list available
           to them
           This function checks the type of customer using the function to know what products they have access to
           The function also adds prices and keeps track of quantity of each products and updates all relevant variables
           displayed in the str method
           """
        viewableprods = Products(self.customer)  # base viewable products off customer type
        if item in viewableprods.products:  # check if item exists
            amount = int(viewableprods.products.get(item))  # find the amount of the product
            self.amount += amount  # add prices
            if item in self.products_quantity.keys():  # check if item in basket
                self.products_quantity[item] += 1  # add quantity by 1 if in basket
            else:
                self.products_quantity[item] = 1  # add to basket if not in basket
                self.total_products.append(item)  # add to current cart list for (str) method
        else:
            print("Item not found. Try listing items to find what you need.\n")

    def remove_item(self, item):  # removing item from basket
        """This function allows a customer to remove an item in the products list available
           to them
           This function checks the type of customer using the function to know what products they have access to
           The function also subs prices and keeps track of quantity of each products and updates all relevant variables
           displayed in the str method
           If an item is removed and the quantity is now 0 its dictionary entry is removed
           """
        viewableprods = Products(self.customer)  # base viewable products off customer type
        if item in viewableprods.products:  # check if item exists
            amount = int(viewableprods.products.get(item))  # get price of item from product list
            self.amount -= amount  # sub prices
            # sub quantity by 1 if in basket
            if item in self.products_quantity.keys():  # check if item is in basket
                self.products_quantity[item] -= 1  # reduce quantity by 1
                if self.products_quantity[item] == 0:  # if quantity remaining is 0 remove entry from basket
                    self.total_products.remove(item)  # remove item from basket product name list
                    del self.products_quantity[item]  # remove from basket product/quantity dict if no longer in basket
            else:  # if item not in basket
                print("Item not in basket")  # item not in basket
        else:  # if item is not in customer's list of products or typo
            print("Item not found. Try listing items to find what you need.\n")

    def __add__(self, item):
        self.add_item(item)

    def __sub__(self, item):
        self.remove_item(item)

    def get_basket_quantity(self):
        """This method will find the total quantity of items in basket
            this includes items with quantity 2+ being included as 2+
            This is used to calculate delivery cost"""
        sum1 = 0
        for value in self.products_quantity.values():
            sum1 += int(value)  # adds up all quantity values of each item in basket
        return sum1

    def checkout(self):
        """This function allows a customer to checkout with the items in their basket
           a delivery fee will be added after a shipping method is chosen
           The customer must confirm they are happy to checkout
           The price and items will be shown before this
           If they are happy to proceed a thank you message is displayed
           The program will then stop
           """
        if len(self.total_products) > 0:  # only execute if at least 1 product in basket
            quantity = self.get_basket_quantity()
            if quantity > 3:  # if more than 3 items additional fee charged
                delivery_fee = 3  # add 3 to delivery price
            else:
                delivery_fee = 0  # charge nothing extra for 3 or less items
            print("Choose shipping Method:\n1. Priority(Next-Day)\n2. Standard(3-5 Days)\n")
            try:
                delivery_selection = int(input())  # choosing delivery type
                if delivery_selection == 1:  # priority
                    delivery_fee += 7
                elif delivery_selection == 2:  # standard
                    delivery_fee += 3
                else:
                    while delivery_selection > 2 or currency_int < 1:
                        print("Please enter a valid option!\n")
                        delivery_fee = int(input())
            except TypeError:
                print("Non-Int Given! Enter 1 or 2!\n")  # wrong input
            self.amount += delivery_fee  # add delivery fee to amount due
            print(self)  # print basket items and price before checkout
            print("Including delivery fee: {}\n".format(delivery_fee))
            # Selection
            confirmation = input("Are you sure you want to buy (y/n)?\n")
            confirmation = confirmation.lower()  # prevent case sensitive errors
            if confirmation == 'y':
                order_confirmed = True
            elif confirmation == 'n':
                order_confirmed = False  # stop checkout
            else:
                print("Input not recognised!\nReturning...")
                order_confirmed = False  # stop checkout
            if order_confirmed is True:  # continue with checkout
                print("Thank you for shopping with us! Order confirmed")  # customer message
                print("Your order items are:")
                # Print basket before emptying and exiting
                for key, value in self.products_quantity.items():  # print items bought
                    print("Item: {}\nQuantity: {}".format(key, value))
                self.products_quantity = {}  # empty basket
                self.total_products = []  # empty basket
                time.sleep(2.5)
                sys.exit()  # exit program after checkout
            else:
                self.amount -= delivery_fee  # remove delivery fee if not buying
                print("OK! Enjoy shopping with us!\n")  # if checkout is stopped
        else:
            print("Basket is empty\n You must add products to basket first!\n")  # do not allow without items


# Products
class Products():
    def __init__(self, customer=BargainHunter()):
        """this method initialises the key arguments of the class initialisation

        Keywords:                                Defaults:
        products: Dictionary of products available + prices to argued customer (standard products = default)
        customer: customer using basket          BargainHunter ... i.e. non-exclusive
        currency_type: customer's currency used  Euro
        """

        self.customer = customer
        self.currency_type = customer.currency_type  # to match products currency
        product_dict = {}  # for storing products and amount
        product_read = open(r"jacks_products.txt", "r").read()  # open file
        product_read = product_read.lower()  # prevent not finding word based on case-sensitivity
        product_list = product_read.split(', ')  # indicate separator between documents
        for x in range(len(product_list)):  # iterate over products
            temp = product_list[x].split(" <amount> ")  # split products into price and name in dictionary
            temp_product = temp[0]  # name of product
            temp_amount = float(temp[1])  # amount of product
            # Currency conversion if required
            if self.currency_type == 'eur':
                pass
            elif self.currency_type == 'usd':
                temp_amount = self.convert_currency(temp_amount)
            elif self.currency_type == 'gbp':
                temp_amount = self.convert_currency(temp_amount)
            # Add product to product list with correct currency
            product_dict[temp_product] = temp_amount  # add entry for product with price
        self.products = product_dict  # set dictionary to class instance

        # Exclusive Products Added
        if customer.exclusive is True:
            # add exclusive products
            product_dict = {}  # additional dictionary
            product_read = open(r"jacks_exclproducts.txt", "r").read()  # open file
            product_read = product_read.lower()  # prevent not finding word based on case-sensitivity
            product_list = product_read.split(', ')  # indicate separator between documents
            for x in range(len(product_list)):  # iterate over products
                temp = product_list[x].split(" <amount> ")  # split products into price and name in dictionary
                temp_product = temp[0]  # name of product
                temp_amount = float(temp[1])  # amount of product
                # Currency conversion if required
                if self.currency_type == 'eur':
                    pass
                elif self.currency_type == 'usd':
                    temp_amount = self.convert_currency(temp_amount)
                elif self.currency_type == 'gbp':
                    temp_amount = self.convert_currency(temp_amount)
                # Add product to product list with correct currency
                product_dict[temp_product] = temp_amount  # add entry for product and price
                self.products.update(product_dict)  # add additional products to original product dictionary for this instance

    def __str__(self):
        """This method displays the products and their price in the customer's preferred currency
           This is used to list all products in the program"""
        return_str = ''
        for key, value in self.products.items():  # iterate through products the user is allowed use
            if self.currency_type == 'eur':
                return_str += "{}    €{}\n".format(key, value)
            elif self.currency_type == 'usd':
                return_str += "{}    ${}\n".format(key, value)
            elif self.currency_type == 'gbp':
                return_str += "{}    £{}\n".format(key, value)
        return return_str

    def convert_currency(self, amount2):
        """This function is a basic currency converter that will convert an amount from the default
            to the user's preferred currency
            This is called upon during product initialisation
            """
        # conversion rates
        eur_to_usd = 1.22
        eur_to_gbp = 0.91
        if self.currency_type == 'eur':  # same currency
            pass
        elif self.currency_type == 'gbp':
            conv_amount = amount2 * eur_to_gbp  # convert amount using provided rates
            return conv_amount  # return the converted amount to the function accessing this function
        elif self.currency_type == 'usd':
            conv_amount = amount2 * eur_to_usd  # convert amount using provided rates
            return conv_amount  # return the converted amount to the function accessing this function


# Test Function - test() is for BargainHunters test2() is for loyal customers
def test():
    """This test functions initialises instances of each class with different combinations of arguments
       for non loyal customers are given
       items are added to basket and removed with the basket being printed most times to reflect the change in price
       the currency can also be altered and product price changes can be seen after this change
       the checkout function is also added"""
    # Customer
    standard_cust2 = BargainHunter("Lucas Rizzo", "Brazil", 1263713, "usd")  # test customer creation
    print(standard_cust2)  # bargain customer str
    # Product
    standard_prod2 = Products(standard_cust2)  # test standard product
    print(standard_prod2)  # test standard product listing
    # Shopping Cart
    standard_cart = ShoppingCart(standard_cust2)
    print("adding jeans")
    standard_cart+"jeans"
    print("adding jacket")
    standard_cart.add_item("jacket")
    print("adding exclusive item as bargain hunter")
    standard_cart.add_item("fridge")  # try adding exclusive product to standard customer
    print(standard_cart)
    print("Removing jeans")  # to test overloaded operator
    standard_cart-"jeans"
    print("GET AMOUNT-> GET CUSTOMER")
    print(standard_cart.get_amount())
    print(standard_cart.get_customer())
    print("adding jacket")
    standard_cart.add_item("jacket")
    print("adding jacket")
    standard_cart+"jacket"
    print("adding jacket")
    standard_cart.add_item("jacket")  # checking delivery value with more than 4 items
    print(standard_cart)  # remove items as you please to check delivery items
    print("checking out")
    # confirm or deny and choose delivery
    standard_cart.checkout()

# Test Function
def test2():
    """This test functions initialises instances of each class with different combinations of arguments
       for loyal customers are given
       items are added to basket and removed with the basket being printed most times to reflect the change in price
       the currency can also be altered and product price changes can be seen after this change
       the checkout function is also added"""
    # Customer
    loyal_cust = LoyalCustomer("Jack Levins", "Drogheda, IE", 1634534, "eur")  # test customer creation
    print(loyal_cust)  # loyal customer str
    # Product
    excl_prod1 = Products(loyal_cust)  # test exclusive product
    print(excl_prod1)  # test exclusive product listing
    # Shopping Cart
    standard_cart = ShoppingCart(loyal_cust)
    print("adding jeans")
    standard_cart+"jeans"
    print("adding jacket")
    standard_cart.add_item("jacket")
    print("adding exclusive item as loyal customer")
    standard_cart.add_item("fridge")  # try adding exclusive product to standard customer
    print("Removing jeans")  # to test overloaded operator
    standard_cart-"jeans"
    print(standard_cart)
    print("GET AMOUNT-> GET CUSTOMER")
    print(standard_cart.get_amount())
    print(standard_cart.get_customer())
    print("adding jacket")
    standard_cart.add_item("jacket")
    print("adding jacket")
    standard_cart+"jacket"
    print("adding jacket")
    standard_cart.add_item("jacket")  # checking delivery value with more than 4 items
    print(standard_cart)  # remove items as you please to check delivery items
    print("checking out")
    # confirm or deny and choose delivery
    standard_cart.checkout()




# main
program_run = 0  # only allow functions when customer is created

test()  # comment out to test main or say 'n' on checkout
#test2()  # comment out to test main or say 'n' on checkout

# The main is described in depth in the attached report
while 1:
    # Main Menu
    print("Please choose an option:")
    print("1.	Create a Customer")
    print("2.	List Products")
    print("3.	Add or remove products to cart")
    print("4.	See current cart")
    print("5.	Checkout")
    print("Press 6 to Quit")
    # Error Catching
    program_menu = 0
    try:
        program_menu = int(input())
    except ValueError:
        print("Non-Int given, please give an integer\n")

    if program_menu == 1:  # option1 - new customer
        if program_run == 0:  # only allow if customer doesn't exist
            program_run = 1  # do not allow another customer
            print("Create a Customer:")
            customer_name = input("Enter a name for the customer")
            customer_address = input("Enter an address for the customer")
            acc_ID = random.randint(0, 999999)  # random id
            # Bargain Hunter/Loyal/Standard
            print("Are you a loyal customer")
            print("Press 1 for Yes (3+ Years)")
            print("Press 2 for	No")
            try:  # error catching
                exclusive_int = int(input())
            except ValueError:
                print("Non-Int given, please give an integer\n")
            while exclusive_int > 2 or exclusive_int < 1:
                print("Please enter a valid option!\n")
                exclusive_int = int(input())
            print("Choose your currency")  # customer preferred currency
            print("Press 1 for EUR")
            print("Press 2 for USD")
            print("Press 3 for GBP")
            try:  # error catching
                currency_int = int(input())
            except ValueError:
                print("Non-Int given, please give an integer\n")
            while currency_int > 3 or currency_int < 1:
                print("Please enter a valid option!\n")
                currency_int = int(input())
            if currency_int == 1:
                currency_type = 'eur'
            elif currency_int == 2:
                currency_type = 'usd'
            elif currency_int == 3:
                currency_type = 'gbp'
            if exclusive_int == 1:
                customer = LoyalCustomer(customer_name, customer_address, acc_ID, currency_type)  # create customer
                products1 = Products(customer)  # create products visible to user
                cart1 = ShoppingCart(customer)  # create a user shopping cart
            elif exclusive_int == 2:
                customer = BargainHunter(customer_name, customer_address, acc_ID, currency_type)  # create customer
                products1 = Products(customer)  # create products visible to user
                cart1 = ShoppingCart(customer)  # create a user shopping cart
            else:  # error catching
                while exclusive_int > 2 or currency_int < 1:
                    print("Please enter a valid option!\n")
                    currency_int = int(input())
        else:
            print("Customer already created!\n")
    elif program_menu == 2:  # option2 - read products available
        if program_run == 1:  # if customer created
            print("List Products:")
            print(products1)  # str method
        else:
            print("Customer not created\n")
    elif program_menu == 3:  # option3 - add/remove items
        if program_run == 1:  # if customer created
            print("Add or remove products to cart")
            print("Would you like to add or remove items from cart?")
            add = ['+', 'add']
            remove = ['-', "remove"]
            response = input()
            response = response.lower()
            if response in add:  # add chosen
                item = input("Which item would you like to add to basket")
                cart1.add_item(item)
            elif response in remove:  # remove chosen
                item = input("Which item would you like to remove from basket")
                cart1.remove_item(item)
            else:
                print("Invalid option selected")  # error caught
        else:
            print("Customer not created\n")  # create customer first

    elif program_menu == 4:  # option4 - current cart
        if program_run == 1:  # if customer created
            print("Current cart")
            print(cart1)  # str method
        else:
            print("Customer not created\n")
    elif program_menu == 5:  # option5 - checkout
        if program_run == 1:  # if customer created
            print("Checkout:")
            cart1.checkout()  # checkout the current cart
        else:
            print("Customer not created\n")  # must create customer first
    elif program_menu == 6:  # option6 quit
        print("Quitting...:")
        time.sleep(1.5)  # make quitting a natural speed
        break
    else:  # invalid input for menu
        print("Please enter a valid option!")

# end of program
