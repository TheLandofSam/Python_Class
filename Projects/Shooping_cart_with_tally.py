CART = [
    {'item': 'classic soda pop pack', 'count': 2, 'price': 7.39},
    {'item': 'classic soda pop single', 'count': 1, 'price': 1.03},
    {'item': 'Lindt Intense Orange Dark Chocolate Bar', 'count': 4, 'price': 4.59},
    {'item': 'Hershey Heath Bar Mini Bag', 'count': 1, 'price': 3.89},
    {'item': 'Breyers Non-dairy Vanilla Ice Cream', 'count': 1, 'price': 6.99},
    {'item': 'Lactaid Cottage Cheese', 'count': 2, 'price': 3.49},
    {'item': 'frozen pizza, cheese', 'count': 1, 'price': 5.99},
    {'item': 'California Pizza Company Thin Crust Meat Pizza', 'count': 1, 'price': 9.89},
    {'item': 'Baby Carrots', 'count': 1, 'price': 2.25},
    {'item': 'Garlic Pickles', 'count': 1,'price': 4.25},
    {'item': 'Harvest Wheat Crackers', 'count': 1, 'price': 3.79},
    {'item': 'black olives', 'count': 1,'price': 1.98},
    {'item': 'corn', 'count': 1, 'price': 0.67},
    {'item': 'romaine lettuce', 'count': 1, 'price': 2.25},
    {'item': 'green onions', 'count': 1, 'price': 1.98},
    {'item': 'garbanzo beans', 'count': 2, 'price': 1.25},
    {'item': 'kidney beans, dark red', 'count': 2, 'price': 1.25},
    {'item': 'grated cheddar cheese', 'count': 2, 'price': 4.98},
    {'item': 'Tillimook Sharp Cheddar cheese', 'count': 1, 'price': 13.99},
    {'item': 'pet treats', 'count': 1, 'price': 4.98}
]

def display_details():
    for item in CART:
        print(f'🔸 {item['item']} 🔹 {item['count']} 💲 {item['price']} 💲💲 {item['line_item_total']}')

def read_cart_from_file():
    try:
        with open('cart.txt', 'r') as file:
            print(f'*** Your cart ***\n{file.read()}\n')
    except:
        print('File not found')

def save_item_to_cart(subtotal):
    with open('cart.txt', 'w') as file:
        for item in CART:
            file.write(f'> {item['item']} - {item['count']} $ {item['price']} $$ {item['line_item_total']}\n')
    with open('cart.txt', 'a') as file:
        file.write(f'$$ SUBTOTAL: {subtotal:.2f}')
        

def add_item_to_cart(item, count, price):
    CART.append({'item': item, 'count': count, 'price': price})

def remove_item_from_cart(): # ASK PAULA
    print(f'\n Which item would you like to remove?')

    for index, item in enumerate(CART):
        print(index, item['item'])

    choice = int(input('What is the line number of your choice?: '))

    CART.pop(choice)

def tally():
    
    subtotal = 0

    for item in CART:
        item['line_item_total']= (item['count'] * item['price']) # can't create a new key with list comprehension
        subtotal += item['line_item_total']

    return subtotal
      
    
def cart_management_system():
    try:

        while True:
            print('\n1. Add item to cart\n2. View cart\n3. Remove item from cart\n4. Exit')
            choice = input('Chose an option: ')

            if choice == '1':
                item = input('Enter the item name: ')
                count = input('Enter the package count: ')
                price =input('Enter the item price: ')

                if float(price) < 0.01:
                    raise Exception('That is not a valid price')

                add_item_to_cart(item, count, price)
                save_item_to_cart()

            elif choice == '2':
                subtotal = tally()
                save_item_to_cart(subtotal)
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

cart_management_system()
