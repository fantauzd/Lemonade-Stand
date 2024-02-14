# Author: Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 10/7/2023
# Description: Represents a Lemonade Stand with functions to track its profit and Menu,
# could also be used for a restaurant

class MenuItem:
    """
    Represents a menu item to be offered for sale at the lemonade stand.
    """

    def __init__(self, name, wholesale_cost, selling_price):
        """
        Creates a MenuItem object with a name, wholesale cost, and selling price
        """
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        """
        Returns the name of the MenuItem object
        """
        return self._name

    def get_wholesale_cost(self):
        """
        Returns the wholesale cost of the MenuItem object
        """
        return self._wholesale_cost

    def get_selling_price(self):
        """
        Returns the selling price of the MenuItem object
        """
        return self._selling_price


class SalesForDay:
    """
    Represents the sales for a particular day at the lemonade stand
    """

    def __init__(self, day, sales_dict):
        """
        Creates a SalesForDay object with an integer for the number of days the stand has been open so far and a
        dictionary whose keys are the names of the items sold and
        whose values are the numbers of those items sold that day
        """
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        """
        Returns an integer for the number of days the stand has been open so far
        """
        return self._day

    def get_sales_dict(self):
        """
        Returns a dictionary whose keys are the names of the items sold and
        whose values are the numbers of those items sold that day
        """
        return self._sales_dict


class InvalidSalesItemError(Exception):
    """
    user-defined exception for when the name of a sold item does
    not match any MenuItem in the dictionary of MenuItem objects
    """
    pass


class LemonadeStand:
    """
    Represents a classic lemonade stand
    """

    def __init__(self, name):
        """
        Creates a LemonadeStand object with a string for the name of the stand; initializes the name to that value,
        initializes current day to zero, initializes the menu to an empty dictionary,
        and initializes the sales record to an empty list
        """
        self._name = name
        self._day = 0
        self._menu = {}
        self._sales_record = []

    def get_name(self):
        """
        Returns the name of the lemonade stand
        """
        return self._name

    def add_menu_item(self, menu_item):
        """
        Takes as a parameter a MenuItem object and adds it to the menu dictionary
        """
        self._menu[menu_item.get_name()] = menu_item  # adds menu item by defining new key and value in dictionary

    def enter_sales_for_today(self, sales_dict):
        """
        Takes as a parameter a dictionary where the keys are names of items sold and
        the corresponding values are how many of the item were sold. Creates a SalesFor Day object
        from dictionary and adds it to the sales record. Increments day.
        """
        menu_list = []  # initializes an empty list
        for name in self._menu:  # iterates over keys in menu dictionary
            menu_list.append(name)  # creates a list of each menu item name
        for name in sales_dict:
            if name not in menu_list:  # finds any menu item name not in self._menu
                raise InvalidSalesItemError

        sales_day_obj = SalesForDay(self._day, sales_dict)  # creates SalesForDay object
        self._sales_record.append(sales_day_obj)  # adds new object to sales record
        self._day += 1  # increments current day by 1

    def sales_of_menu_item_for_day(self, day, desired_item_name):
        """
        Takes as parameters an integer representing a particular day and a string for the name of a menu item
        Returns the number of that item sold on that day
        """
        obj = self._sales_record[day]  # accesses the SaleForDay object for the specific day
        req_day_record = obj.get_sales_dict()  # accesses the requested sales dictionary for that day
        for item_name in req_day_record:
            if desired_item_name == item_name:
                return req_day_record[item_name]  # returns the amount of the desired_item_name that was sold on the day
            elif item_name not in req_day_record:
                return 0

    def total_sales_for_menu_item(self, desired_item_name):
        """
        Takes as a parameter a string for the name of a menu item and returns
        the total number of that item sold over the history of the stand
        """
        sales = 0  # initializes sales variable
        last_day = self._day
        for day in range(0, last_day):
            sales += self.sales_of_menu_item_for_day(day,
                                                     desired_item_name)  # adds the amount sold on each day of operation
        return sales

    def total_profit_for_menu_item(self, desired_item_name):
        """
        Takes as a parameter a string for the name of a menu item and
        returns the total profit on that item over the history of the stand
        """
        item = self._menu[desired_item_name]  # accesses the MenuItem object
        buy_price = item.get_wholesale_cost()
        sell_price = item.get_selling_price()
        item_profit = sell_price - buy_price
        quantity = self.total_sales_for_menu_item(desired_item_name)
        total_profit = item_profit * quantity
        return total_profit

    def total_profit_for_stand(self):
        stand_profit = 0  # initializes the stand's profit
        for menu_item in self._menu:  # iterates for every menu item by menu item name
            stand_profit += self.total_profit_for_menu_item(
                menu_item)  # adds the total profit of each item to the stand_profit
        return stand_profit


def main():
    stand = LemonadeStand("Irwin's Lemonade")  # Create a new LemonadeStand callled "Irwin's Lemonade"
    item1 = MenuItem('Lemur Love Lemonade', 1.63, 4.99)
    stand.add_menu_item(item1)
    item2 = MenuItem('Big Bear Brownie', 1.14, 5)
    stand.add_menu_item(item2)
    item3 = MenuItem('Crikey Cookies', 2.31, 6.25)
    stand.add_menu_item(item3)
    item4 = MenuItem('Roasted Crikey Crickets', .25, 2.99)
    stand.add_menu_item(item4)

    # The below dictionaries record sales for three days
    day_0_sales = {'Lemur Love Lemonade': 19, 'Big Bear Brownie': 6,
                   'Crikey Cookies': 18, 'Roasted Crikey Crickets': 2, 'Water': 4}  # contains an item not on the Menu
    day_1_sales = {'Lemur Love Lemonade': 19, 'Big Bear Brownie': 1,
                   'Crikey Cookies': 17, 'Roasted Crikey Crickets': 6}
    day_2_sales = {'Lemur Love Lemonade': 22, 'Big Bear Brownie': 8,
                   'Crikey Cookies': 23, 'Roasted Crikey Crickets': 17}

    try:
        stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero
    except InvalidSalesItemError:
        print('The sales dictionary contains an item that is not in the menu, cannot accept input.')

    stand.enter_sales_for_today(day_1_sales)  # Record the sales for day one
    stand.enter_sales_for_today(day_2_sales)  # Record the sales for day two

    print(f"Irwin's Lemonade has made {stand.total_profit_for_stand()}")  # print the total profit so far
    print(f"Lemur Love Lemonade profit = {stand.total_profit_for_menu_item('Lemur Love Lemonade')}")
    print(f"Big Bear Brownie = {stand.total_profit_for_menu_item('Big Bear Brownie')}")
    print(f"Crikey Cookies = {stand.total_profit_for_menu_item('Crikey Cookies')}")
    print(f"Roasted Crikey Crickets = {stand.total_profit_for_menu_item('Roasted Crikey Crickets')}")


if __name__ == '__main__':
    main()
