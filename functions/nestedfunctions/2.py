from math import *

# pi=10  #global

def outer():
    # pi=20  #nonlocal
    def inner():
        # pi=30  #local
        print(pi)
    inner()

outer()