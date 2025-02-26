def primesam(start,stop):
    '''This function prints all prime numbers within a given range.'''
    while(start<=stop):
        i=2
        c=False
        while(i<=(start//2)):
            if(start%i==0):
                c=True
                break
            i+=1
        if(not c):
            print(f'{start}:Prime')
        c=False
        start+=1

primesam(10,20)