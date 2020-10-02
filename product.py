class Product:
    sales_tax_rate = 0.1

    def __init__(self, quantity, name, price, imported = False):
        self.quantity = quantity 
        self.imported = imported
        self.name = name
        self.price = price
    
    @classmethod
    def from_string(cls, product_str):
        list_data = product_str.split(' ')
        length = len(list_data)
        qty = 0
        name = ''
        price = 0.00
        try:
            for i in range(length):
                if i == 0:
                    qty = int(list_data[i])
                elif i == length - 1:
                    price = float(list_data[i])
                elif list_data[i].lower() != 'at':
                    name = name + list_data[i] + ' '
        except ValueError:
            raise ValueError('Invalid input for quantity or price!')

        return cls(qty, name, price)

    @staticmethod
    def is_exempted(name):
        exempted = False
        with open("exemptedProducts.txt") as exempted_goods:
            for item in exempted_goods:
                if item.rstrip("\n") in name:
                    exempted = True
                    break
        return exempted
    
    @staticmethod
    def is_imported(name):
        return 'imported' in name.lower()
    
    def set_sales_tax_rate(self):
        if(self.is_exempted(self.name)):
            self.sales_tax_rate = 0.0
        if(self.is_imported(self.name)):
            self.sales_tax_rate = self.sales_tax_rate + 0.05