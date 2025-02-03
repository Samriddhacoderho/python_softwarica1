def outer():
    pocket_money=10
    print(pocket_money)
    def inner():
        c=pocket_money+40
        print(c)
    return inner

(outer())()
