import unittest
from product import Product
from shoppingBasket import ShoppingBasket

class TestSalesTax(unittest.TestCase):
    def setUp(self):
        self.product_1 = Product(1, 'music CD', 14.99)
        self.product_2 = Product.from_string('1 imported box of chocolates at 10.00')
        self.shopping_basket = ShoppingBasket()
        self.shopping_basket.load_items('inputs.txt')

    def tearDown(self):
        pass

    def test_from_string(self):
       self.assertEqual(self.product_2.quantity, 1) 
       self.assertEqual(self.product_2.name.rstrip(), 'imported box of chocolates') 
       self.assertEqual(self.product_2.price, 10.00) 
       with self.assertRaises(ValueError):
           Product.from_string('x imported box of chocolates at 10.00')
       self.assertRaises(ValueError, Product.from_string, '3 imported box of chocolates at yy')

    def test_is_imported(self):
        self.assertFalse(self.product_1.is_imported(self.product_1.name))
        self.assertTrue(self.product_2.is_imported(self.product_2.name))
    
    def test_is_exempted(self):
        self.assertFalse(self.product_1.is_exempted(self.product_1.name))
        self.assertTrue(self.product_2.is_exempted(self.product_2.name))

    def test_calc_sales_tax(self):
        self.product_1.set_sales_tax_rate()
        sales_tax = self.shopping_basket.calc_sales_tax(self.product_1.price, self.product_1.sales_tax_rate)
        self.assertEqual(sales_tax, 1.5)
    
    

if __name__ == '__main__':
    unittest.main()