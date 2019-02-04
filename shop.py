####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = 'Cupcake Shop'
signature_flavors = ["Cinampn", "Pistachio", "Coconut", "Espresso"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    for item in menu:
        print("%s: %s" % (item, menu[item]))


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    
    for product in original_flavors:
        print (product)



def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for item in signature_flavors:
        print (item)

def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order in menu or order in original_flavors or order in signature_flavors:
        return True
    else: 
        return False



def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    
    order = input("What's your order? (Enter the exact spelling of the item you want. Type 'Exit' to end your order.")
    while order != 'exit':
        if is_valid_order(order):
            order_list.append(order)
        else:
            print ("Try again..")
        order = input("What else would you like? ")
    
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here! 
    if total >= 5:
        return True
    else: 
        return False

def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for order in order_list:
        if order in menu:
           total += menu[order]
        elif order in original_flavors:
           total += original_price
        else:
           total += signature_price
    return total



def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    for order in order_list:
        print (order)

    total = get_total_price(order_list)
    print ("Your total is: %s KD" % (total))

    if accept_credit_card(total):
        print ("You can pay by either the credit card or cash")
    else: 
        print ("You can pay using cash only")
    print ("Thank you for shopping from %s" % (cupcake_shop_name))
