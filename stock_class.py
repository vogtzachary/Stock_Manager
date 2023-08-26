# This file contains our Classes for this project, used in both stock_menu.py and stock_GUI.py.
# See uml_classes.png for additional information.

class Stock:
    def __init__(self, symbol, name, shares):
        self.symbol = symbol
        self.name = name
        self.shares = shares
        self.DataList = []

    def add_data(self, stock_data):
        self.DataList.append(stock_data)


class DailyData:
    def __init__(self, date, close, volume):
        self.date = date
        self.close = close
        self.volume = volume
