CART = [
    {'item': 'classic soda pop pack', 'size': '12 cans', 'price': 7.39},
    {'item': 'classic soda pop single', 'size': '1 bottle', 'price': 1.03},
    {'item': 'Lindt Intense Orange Dark Chocolate Bar', 'size': '1 bar', 'price': 4.59},
    {'item': 'Hershey Heath Bar Mini Bag', 'size': 'family pack', 'price': 3.89},
    {'item': 'Breyers Non-dairy Vanilla Ice Cream', 'size': 'tub', 'price': 6.99},
    {'item': 'Ben and Jerry\'s Cherry Garcia', 'size': 'pint', 'price': 5.99},
    {'item': 'frozen pizza, cheese', 'size': '10 inch', 'price': 5.99},
    {'item': 'California Pizza Company Thin Crust Meat Pizza', 'size': '10 inch', 'price': 9.89},
    {'item': 'Baby Carrots', 'size': '1lb bag', 'price': 2.25},
    {'item': 'Garlic Pickles', 'size': '1 bottle','price': 4.25},
    {'item': 'Dill Pickles', 'size': '1 bottle', 'price': 3.79},
    {'item': 'black olives', 'size': '1 can','price': 1.98},
    {'item': 'corn', 'size': '1 can', 'price': 0.67},
    {'item': 'romaine lettuce', 'size': '1 head', 'price': 2.25},
    {'item': 'green onions', 'size': '1 bundle', 'price': 1.98},
    {'item': 'garbanzo beans', 'size': '1 can', 'price': 1.25},
    {'item': 'kidney beans, dark red', 'size': '1 can', 'price': 1.25},
    {'item': 'grated cheddar cheese', 'size': '8 oz package', 'price': 4.98},
    {'item': 'Tillimook Sharp Cheddar cheese', 'size': '2lb block', 'price': 13.99},
    {'item': 'pet treats', 'size': '5 oz', 'price': 4.98}
]

def display_details():
    for item in CART:
        print(f'🔸 {item['item']} 🔹 {item['size']} 💲 {item['price']}')

def read_cart_from_file():
    try:
        with open('cart.txt', 'r') as file:
            print(f'*** Your cart ***\n{file.read()}\n')
    except:
        print('File not found')

def save_item_to_cart():
    with open('cart.txt', 'w') as file:
        for item in CART:
            file.write(f'> {item['item']} - {item['size']} $ {item['price']}\n')


def add_item_to_cart(item, size, price):
    CART.append({'item': item, 'size': size, 'price': price})

def remove_item_from_cart(): # ASK PAULA
    print(f'\n Which item would you like to remove?')

    for index, item in enumerate(CART):
        print(index, item['item'])

    choice = int(input('What is the line number of your choice?: '))

    CART.pop(choice)
    
    
def cart_management_system():
    try:

        while True:
            print('\n1. Add item to cart\n2. View cart\n3. Remove item from cart\n4. Exit')
            choice = input('Chose an option: ')

            if choice == '1':
                item = input('Enter the item name: ')
                size = input('Enter the package size: ')
                price =input('Enter the item price: ')

                if float(price) < 0.01:
                    raise Exception('That is not a valid price')

                add_item_to_cart(item, size, price)
                save_item_to_cart()

            elif choice == '2':
                read_cart_from_file()

            elif choice == '3':
                remove_item_from_cart()
                save_item_to_cart()

            elif choice == '4':
                break

    except Exception as error:
        print(error)


#display_details()
#add_item_to_cart('green onions', '1 bundle', 1.98)
#save_item_to_cart()
#remove_item_from_cart()
#display_details()
cart_management_system()