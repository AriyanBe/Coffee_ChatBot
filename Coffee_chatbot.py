def coffee_bot():
    """Greet the customer, take their order, and provide them with extra options."""
    print('Welcome to the cafe!')

    # Get the customer's order
    size = get_size()
    drink_type = get_drink_type()
    print('Alright, that\'s a {} {}!'.format(size, drink_type))

    # Provide extra options
    extra_options()

    # Get the customer's name and tell them their drink will be ready shortly
    name = input('Can I get your name please? \n> ')
    print('Thanks, {}! Your drink will be ready shortly.'.format(name))


def get_size():
    """Get the size of the drink from the customer."""
    res = input('What size drink can I get for you? \n [a] Small \n[b] Medium \n[c] Large \n> ')

    # Return the corresponding size
    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        # If the customer's input is invalid, ask for their input again
        print_message()
        return get_size()


def get_drink_type():
    """Get the type of drink from the customer."""
    res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

    # Return the corresponding drink type
    if res == 'a':
        return 'brewed coffee'
    elif res == 'b':
        return 'mocha'
    elif res == 'c':
        return order_latte()
    else:
        # If the customer's input is invalid, ask for their input again
        print_message()
        return get_drink_type()


def order_latte():
    """Get the type of milk for the latte from the customer."""
    res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')

    # Return the corresponding latte with milk type
    if res == 'a':
        return 'latte'
    elif res == 'b':
        return 'non-fat latte'
    elif res == 'c':
        return 'soy latte'
    else:
        # If the customer's input is invalid, ask for their input again
        print_message()
        return order_latte()


def extra_options():
    """Ask the customer if they need a plastic cup or have their own reusable cup."""
    res = input('Would you like a plastic cup or did you bring your own reusable cup? \n[a] I\'ll need a cup. \n[b] Brought my own! \n> ')

    # Provide the corresponding extra option
    if res == 'a':
        print('Okay, no problem! We\'ll get you a plastic cup.')
    elif res == 'b':
        print('Great! We\'ll fill up your reusable cup.')
    else:
        # If the customer's input is invalid, ask for their input again
        print_message()
        return extra_options()


def print_message():
    """Print an error message if the customer's input is invalid."""
    print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')
