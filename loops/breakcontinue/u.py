# 28. Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam

list=['ram','shyam',1,2,'sita']
for i in list:
    if(isinstance(i,str)):
        if(i.isalpha()):
            print('Hello {}'.format(i))
