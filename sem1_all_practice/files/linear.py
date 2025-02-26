def line(arr,search):
    '''This function searches for a number in linear search algorithm of time complexity 0(n)'''
    index=0
    for i in arr:
        if(search==i):
            print(f'Found at index {index}')
            break
        else:
            index+=1
    else:
        print("Not in list")

line([1,2,3,4,5,6],4)