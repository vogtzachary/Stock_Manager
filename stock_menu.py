from stock_class import Stock, DailyData
from account_class import Traditional, Robo
import matplotlib.pyplot as plt
import csv


def add_stock(stock_list):
    option = ""
    while not option:
        print("Add Stock ---")
        add_symbol = input("Enter Ticker Symbol: ")
        if not add_symbol:
            print(f"Invalid Entry. Returning to Menu.\n")
            break
        add_symbol = add_symbol.upper()
        add_name = input("Enter Company Name: ")
        if not add_name:
            print(f"Invalid Entry. Returning to Menu.\n")
            break
        add_name = add_name.title()
        add_shares = input("Enter Number of Shares: ")
        if not add_shares:
            print(f"Invalid Entry. Returning to Menu.\n")
            break
        add_shares = float(add_shares)
        new_stock = Stock(add_symbol, add_name, add_shares)
        stock_list.append(new_stock)
        print(f"{new_stock.name} Successfully Added to stock list.")
        option = input("Enter to Add More, 0 to Stop.")


# Remove stock and all daily data
def delete_stock(stock_list):
    print(f"Delete Stock ----\n"
          f"Stock List: [", end=" ")
    for stock in stock_list:
        print(f"{stock.symbol} ", end=" ")
    print(f"]")
    stock_to_delete = input("Enter Symbol to Delete:\n").upper()
    i = 0
    found = False
    for stock in stock_list:
        if stock.symbol == stock_to_delete:
            stock_list.pop(i)
            print(f"{stock_to_delete} was removed.")
            found = True
        i += 1
        if not found:
            print(f"Stock not found.")


# List stocks being tracked
def list_stocks(stock_list):
    print(f"Stock List ----\n"
          f"SYMBOL          NAME                    SHARES\n"
          f"______________________________________________\n")
    for stock in stock_list:
        print(stock.symbol + (" " * (15-len(stock.symbol))), stock.name + (" " * (23-len(stock.name))), stock.shares)


# Add daily stock data
def add_stock_data(stock_list):
    print("Add Daily Stock Data ----")
    print("Stock List: [", end="")
    for stock in stock_list:
        print(stock.symbol, " ", end="")
    print("]")
    symbol = input("Which stock do you want to use?: ").upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found:
        print("Ready to add data for: ", symbol)
        print("Enter Data Separated by Commas - Do Not use Spaces")
        print("Enter a Blank Line to Quit")
        print("Enter Date,Price,Volume")
        print("Example: 8/28/20,47.85,10550")
        data = input("Enter Date,Price,Volume: ")
        while data != "":
            date, price, volume = data.split(",")
            daily_data = DailyData(date, float(price), float(volume))

            current_stock.add_data(daily_data)
            data = input("Enter Date,Price,Volume: ")
        print("Date Entry Complete")
    else:
        print("Symbol Not Found ***")
    _ = input("Press Enter to Continue ***")


def investment_type(stock_list):
    print("Investment Account ---")
    balance = float(input("What is your initial balance: "))
    number = input("What is your account number: ")
    acct = input("Do you want a Traditional (t) or Robo (r) account: ")
    if acct.lower() == "r":
        years = float(input("How many years until retirement: "))
        robo_acct = Robo(balance, number, years)
        print("Your investment return is ", robo_acct.investment_return())
        print("\n\n")
    elif acct.lower() == "t":
        trad_acct = Traditional(balance, number)
        temp_list = []
        print("Choose stocks from the list below: ")
        while True:
            print("Stock List: [", end="")
            for stock in stock_list:
                print(stock.symbol, " ", end="")
            print("]")
            symbol = input("Which stock do you want to purchase, 0 to quit: ").upper()
            if symbol == "0":
                break
            shares = float(input("How many shares do you want to buy?: "))
            found = False
            for stock in stock_list:
                if stock.symbol == symbol:
                    found = True
                    current_stock = stock
            if found:
                current_stock.shares += shares
                temp_list.append(current_stock)
                print("Bought ", shares, "of", symbol)
            else:
                print("Symbol Not Found ***")
        trad_acct.add_stock(temp_list)


# Function to create stock chart
def display_stock_chart(stock_list, symbol):
    date = []
    price = []
    volume = []
    company = ""
    for stock in stock_list:
        if stock.symbol == symbol:
            company = stock.name
            for dailyData in stock.DataList:
                date.append(dailyData.date)
                price.append(dailyData.close)
                volume.append(dailyData.volume)

    plt.plot(date, price)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(company)
    plt.show()


# Display Chart
def display_chart(stock_list):
    option = ""
    while not option:
        print("Stock List: [", end='\n')
        for stock in stock_list:
            print(stock.symbol + " ")
        print("]")
        symbol = input("Enter a symbol: ").upper()
        found = False
        for stock in stock_list:
            if stock.symbol == symbol:
                found = True
                current_stock = stock
        if found:
            display_stock_chart(stock_list, symbol)
        else:
            option = input("Symbol not found. Enter to continue, or anything else to go back. : ")


# Get price and volume history from Yahoo! Finance using CSV import.
def import_stock_csv(stock_list):
    for stock in stock_list:
        print(f"{stock.symbol} ")
    print(f"]")
    symbol = str(input(f"Choose a Symbol: ")).upper()
    csv_file = symbol + '.csv'
    for stock in stock_list:
        with open(csv_file, 'r') as stock_data:
            datareader = csv.reader(stock_data, delimiter=',')
            next(datareader)
            for row in datareader:
                daily_data = DailyData(str(row[0]), float(row[4]), float(row[6]))
                stock.add_data(daily_data)
    display_report(stock_list)


# Display Report
def display_report(stock_list):
    for stock in stock_list:
        print(f"Report for: {stock.symbol}, {stock.name}\n"
              f"Shares: {stock.shares}\n")
        count = 0
        price_total = 0
        volume_total = 0
        low_price = 999999.99
        high_price = 0
        low_volume = 999999999999
        high_volume = 0

        for daily_data in stock.DataList:
            count += 1
            price_total = price_total + daily_data.close
            volume_total = volume_total + daily_data.volume
            if daily_data.close < low_price:
                low_price = daily_data.close
            if daily_data.close > high_price:
                high_price = daily_data.close
            if daily_data.volume < low_volume:
                low_volume = daily_data.volume
            if daily_data.volume > high_volume:
                high_volume = daily_data.volume

            price_change = high_price - low_price
        if count > 0:
            print(f"Summary ---\n"
                  f"Low Price: {low_price:.2f}\n"
                  f"High Price: {high_price:.2f}\n"
                  f"Average Price: {price_total/count:.2f}\n"
                  f"Low Volume: {low_volume}\n"
                  f"High Volume: {high_volume}\n"
                  f"Average Volume: {volume_total/count}\n"
                  f"Change in Price: {price_change:.2f}\n"
                  f"Max Potential Profit for {stock.shares} shares: {price_change * stock.shares:.2f}\n")
        else:
            print(f"No Daily History.\n\n\n")
        do_something_else = input("Report Complete. Enter to continue, or anything else to exit.")
        if not do_something_else:
            break


def main_menu(stock_list):
    option = ""
    while True:
        print("Stock Analyzer ---")
        print("1 - Add Stock")
        print("2 - Delete Stock")
        print("3 - List stocks")
        print("4 - Add Daily Stock Data (Date, Price, Volume)")
        print("5 - Show Chart")
        print("6 - Investor Type")
        print("7 - Load Data")
        print("0 - Exit Program")
        option = input("Enter Menu Option: ")
        if option == "0":
            print("Goodbye")
            break

        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            delete_stock(stock_list)
        elif option == "3":
            list_stocks(stock_list)
        elif option == "4":
            add_stock_data(stock_list)
        elif option == "5":
            display_chart(stock_list)
        elif option == "6":
            investment_type(stock_list)
        elif option == "7":
            import_stock_csv(stock_list)
        else:

            print("Goodbye")


# Begin program
def main():
    stock_list = []
    main_menu(stock_list)


# Program Starts Here
if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()