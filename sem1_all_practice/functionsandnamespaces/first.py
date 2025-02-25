global_var=10

def outer():
    nonlocal_var=11

    def inner():
        local_var=12
        local_var=local_var+1

        global global_var
        global_var+=1

        nonlocal nonlocal_var
        nonlocal_var+=1
        
        return global_var,nonlocal_var,local_var
    return inner

a,b,c=outer()()
print(a,b,c)