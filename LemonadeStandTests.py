# Author: Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 10/7/2023
# Description: A unit test file for LemonadeStand.py with at least five unit tests
# and uses at least two different assert functions

import unittest
from LemonadeStand import *

class TestLemonadeStand(unittest.TestCase): #  creates a class that inherits from unittest.TestCase
    def test_1(self):
        #  tests special case where none of an item are sold
        stand = LemonadeStand('Yvonne Lime in a Lemon')
        item1 = MenuItem('Lemonade', 0.75, 7.99)
        stand.add_menu_item(item1)

        day_0_sales = {'Lemonade': 0}
        stand.enter_sales_for_today(day_0_sales)

        day_1_sales = {'Lemonade': 0}
        stand.enter_sales_for_today(day_1_sales)

        self.assertEqual(stand.total_profit_for_menu_item('Lemonade'), 0)


    def test_2(self):
        #  tests special case where enter_sales_for_today() is
        #  passed a sales dictionary with no items on the menu, should raise an InvalidSalesItemError
        stand = LemonadeStand("Lollipop Lemonade")  # Create a new LemonadeStand callled "Irwin's Lemonade"
        item1 = MenuItem('Extra Sweet Lemonade', 3, 6.99)
        stand.add_menu_item(item1)

        day_0_sales = {'Lemur Love Lemonade': 19, 'Big Bear Brownie': 6,
                       'Crikey Cookies': 18, 'Roasted Crikey Crickets': 2, 'Water': 4}

        try:
            stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero
        except InvalidSalesItemError:
            test_result = 125

        self.assertEqual(test_result, 125)


    def test_3(self):
        #  unit test for add_menu_item() method
        stand = LemonadeStand('Le Petit Citron')
        item1 = MenuItem('French Limonade', 0.85, 25)
        stand.add_menu_item(item1)

        self.assertEqual(stand._menu, {'French Limonade' : item1})

    def test_4(self):
        #  unit test for get_name() method
        stand = LemonadeStand('CyberLemon')

        self.assertEqual(stand.get_name(), 'CyberLemon')

    def test_5(self):
        #  unit test for incrementing the day properly
        stand = LemonadeStand('Frozen Lemon')
        item1 = MenuItem('Lemon Slushie', 2, 8)
        stand.add_menu_item(item1)

        day_0_sales = {"Lemon Slushie" : 3}
        stand.enter_sales_for_today(day_0_sales)

        day_1_sales = {"Lemon Slushie" : 3}
        stand.enter_sales_for_today(day_1_sales)

        day_2_sales = {"Lemon Slushie" : 3}
        stand.enter_sales_for_today(day_2_sales)

        day_3_sales = {"Lemon Slushie" : 3}
        stand.enter_sales_for_today(day_3_sales)

        self.assertEqual(stand._day, 4)

    def test_6(self):
        #  unit test for multiple stands running
        stand_1 = LemonadeStand('Zesty Cactina')
        item1 = MenuItem('Limeade in a Cactus', 4, 12.99)
        stand_1.add_menu_item(item1)

        stand_2 = LemonadeStand('Frozen Lemon')
        item2 = MenuItem('Lemon Slushie', 2, 8)
        stand_2.add_menu_item(item2)

        day_0_sales = {"Limeade in a Cactus" : 58}
        stand_1.enter_sales_for_today(day_0_sales)

        day_0_sales = {'Lemon Slushie' : 101}
        stand_2.enter_sales_for_today(day_0_sales)

        self.assertNotIn('Limeade in a Cactus', stand_2._menu)



    def test_7(self):
        #  partial integration test for total_profit_for_menu_item() method when menu has multiple items
        stand = LemonadeStand('Zesty Cactina')
        item1 = MenuItem('Limeade in a Cactus', 4, 12.99)
        stand.add_menu_item(item1)
        item2 = MenuItem('Lemon Tacos', 6.12, 8.57)
        stand.add_menu_item(item2)

        day_0_sales = {"Limeade in a Cactus" : 58, "Lemon Tacos" : 122}
        stand.enter_sales_for_today(day_0_sales)
        day_1_sales = {"Limeade in a Cactus" : 68, "Lemon Tacos" : 91}
        stand.enter_sales_for_today(day_1_sales)

        self.assertAlmostEqual(stand.total_profit_for_menu_item('Lemon Tacos'), ((91 + 122)*(8.57 - 6.12)))

    def test_8(self):
        #  large integration test for total_profit_for_stand() method
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
                       'Crikey Cookies': 18, 'Roasted Crikey Crickets': 2}
        day_1_sales = {'Lemur Love Lemonade': 19, 'Big Bear Brownie': 1,
                       'Crikey Cookies': 17, 'Roasted Crikey Crickets': 6}
        day_2_sales = {'Lemur Love Lemonade': 22, 'Big Bear Brownie': 8,
                       'Crikey Cookies': 23, 'Roasted Crikey Crickets': 17}


        stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero
        stand.enter_sales_for_today(day_1_sales)  # Record the sales for day one
        stand.enter_sales_for_today(day_2_sales)  # Record the sales for day two

        #  calculates expected profit for testing
        expected_profit = (19+19+22)*(4.99-1.63)+(6+1+8)*(5-1.14)+(18+17+23)*(6.25-2.31)+(2+6+17)*(2.99-0.25)

        self.assertAlmostEqual(stand.total_profit_for_stand(),expected_profit)


