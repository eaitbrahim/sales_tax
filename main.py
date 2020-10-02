from shoppingBasket import ShoppingBasket

def main():
    shoppingBasket = ShoppingBasket()
    with open("inputs.txt") as inputs:
        key = ''
        for line in inputs:
            loweredLine = line.rstrip("\n").lower()
            if 'input' in loweredLine:
                key = loweredLine.strip(':')
            elif loweredLine != '' and loweredLine != ' ':
                shoppingBasket.add_basket_item(key, loweredLine)
    
    shoppingBasket.checkout()

if __name__ == '__main__':
    main()
        
