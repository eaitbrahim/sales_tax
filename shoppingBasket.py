import sys, math
from product import Product

class ShoppingBasket(dict):
    nearest_rounded_up = 0.05

    def __init__(self):
        self.reset_totals()

    def add_basket_item(self, key_item, basket_item):
        try:
            item = Product.from_string(basket_item)
            self[key_item].append(item)
        except KeyError:
            self.update({key_item: [item]})

    def checkout(self):
        for key in self:
            self.print_receipt_header(key)
            
            for item in self[key]:
                if(item.is_exempted(item.name)):
                    item.sales_tax_rate = 0.0

                if(item.is_imported(item.name)):
                    item.sales_tax_rate = item.sales_tax_rate + 0.05

                sales_tax = self.calc_sales_tax(item.price, item.sales_tax_rate)
                self.total_sales_taxes += sales_tax
                self.total_price = item.quantity * (item.price + sales_tax)
                self.totals += self.total_price

                self.print_receipt_body(item.quantity, item.name)

            self.print_receipt_footer()
            self.reset_totals()
                

    def calc_sales_tax(self, price, sales_tax_rate):
        return ShoppingBasket.nearest_rounded_up *  math.ceil(price * sales_tax_rate / ShoppingBasket.nearest_rounded_up)

    def print_receipt_header(self, shopping_list_name):
        print('')
        print('--- Shopping list for {} ---'.format(shopping_list_name))
        
        
    def print_receipt_body(self, quantity, name, ):
        print("{} {} {}".format(quantity, name, self.total_price)) 
    
    def print_receipt_footer(self):
        print('Sales Taxes: {}'.format(self.total_sales_taxes))
        print('Total: {}'.format(self.totals))
    
    def reset_totals(self):
        self.total_sales_taxes = 0
        self.total_price = 0
        self.totals = 0
            

