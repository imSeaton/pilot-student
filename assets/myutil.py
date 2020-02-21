from math import sqrt

def is_prime(n):
    """Return a boolean value based upon whether the argument n is a prime number."""
    if n < 2:
        return False
    
    if n in (2, 3):
        return True

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True

def say_hi(*names, greeting='Hi', capitalized=False):
    """
    Print a string, with a greeting to everyone.
    :param *names: tuple of names to be greeted.
    :param greeting: 'Hello' as default.
    :param capitalized: Whether name should be converted to capitalized before print. False as default.
    :returns: None
    """
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')
    
print("this senstence_1 has been excutated")
print(f"in this module, the __name__ of the module is {__name__}")
if __name__ == '__main__' :       
    print("this senstence_2 has been excutated")
    