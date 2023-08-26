# This file contains the account type classes used by stock_menu.py

from stock_class import Stock


class RetirementAccount:
    def __init__(self, balance, number):
        self.balance = balance
        self.number = number


class Traditional:
    def __init__(self, balance, number):
        self.balance = balance
        self.number = number

    def add_stock(self, stock_list):
        stock_list.append(self)


class Robo:
    def __init__(self, balance, number, years):
        self.balance = balance
        self.number = number
        self.years = years

    def investment_return(self):
        return self.years * self.balance * 1.05


# Unit Testing
def main():
    error_count = 0
    error_list = []
    print("Unit Testing Starting---")
    # Test Add Traditional
    stock_list = []
    test_stock = Stock("TEST", "Test Company", 200)
    stock_list.append(test_stock)
    print("Testing Add Retirement Account...", end="")
    try:
        testRetire = RetirementAccount(200, "12345")
        print("Successful!")
    except:
        print("***Adding retirement Account Failed!")
        error_count = error_count + 1
        error_list.append("Retirement Constructor Error")
    print("Testing Add Traditional Account...", end="")
    try:
        test_traditional = Traditional(200, "12345")
        test_traditional.add_stock(stock_list)
        print("Successful!")
    except:
        print("***Adding Traditional Account Failed!")
        error_count = error_count + 1
        error_list.append("Traditional Constructor Error")

    # Test Change Balance
    print("Test Change Balance...", end="")
    try:
        test_traditional.balance = 1000
        if test_traditional.balance == 1000:
            print("Successful!")
        else:
            print("***ERROR! Balance change unsuccessful.")
            error_count = error_count + 1
            error_list.append("Balance Change Error")
    except:
        print("***ERROR! Balance change failed.")
        error_count = error_count + 1
        error_list.append("Balance Change Failure")

    # Test Change Number
    print("Test Change Number...", end="")
    try:
        test_traditional.number = "99999"
        if test_traditional.number == "99999":
            print("Successful!")
        else:
            print("***ERROR! Number change unsuccessful.")
            error_count = error_count + 1
            error_list.append("Number Change Error")
    except:
        print("***ERROR! Number change failed.")
        error_count = error_count + 1
        error_list.append("Number Change Failure")

    print("Testing Add Robo Account...", end="")
    try:
        test_robo = Robo(200, "12345", 5)
        print("Successful!")
    except:
        print("***Adding Robo Account Failed!")
        error_count = error_count + 1
        error_list.append("Robo Constructor Error")

    # Test Change years
    print("Test Change Balance...", end="")
    try:
        test_robo.years = 1000

        if test_robo.years == 1000:
            print("Successful!")
        else:
            print("***ERROR! Years change unsuccessful.")
            error_count = error_count + 1
            error_list.append("Years Change Error")
    except:
        print("***ERROR! Years change failed.")
        error_count = error_count + 1
        error_list.append("Years Change Failure")

    # Test investment return
    print("Test investment return...", end="")
    try:
        test_robo.years = 1000
        test_robo.balance = 1
        if test_robo.investment_return() == 1050:
            print("Successful!")
        else:
            print("***ERROR!Investment return unsuccessful.")
            error_count = error_count + 1
            error_list.append("investment return Error")
    except:
        print("***ERROR! investment return failed.")
        error_count = error_count + 1
        error_list.append("Investment Return Failure")

    if error_count == 0:
        print("Congratulations - All Tests Passed")
    else:
        print("-=== Problem List - Please Fix ===-")
        for em in error_list:
            print(em)
    print("Goodbye")


# Program Starts Here
if __name__ == "__main__":
    # run unit testing only if run as a stand-alone script
    main()
