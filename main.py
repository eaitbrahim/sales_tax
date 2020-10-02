from shoppingBasket import ShoppingBasket

def main():
    shoppingBasket = ShoppingBasket()
    shoppingBasket.load_items('inputs.txt')
    
    shoppingBasket.checkout()

if __name__ == '__main__':
    main()
        
