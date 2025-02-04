# f=open('/Users/suhritsatyal/Desktop/python_softwarica1/filehandling/demo.txt','r')
# f2=open('/Users/suhritsatyal/Desktop/python_softwarica1/filehandling/python.txt','w')
# f2.write(f.read())
# f2.close()
# f.close()

# with open('/Users/suhritsatyal/Desktop/python_softwarica1/filehandling/demo.txt','r') as f:
#     with open('/Users/suhritsatyal/Desktop/python_softwarica1/filehandling/python.txt','w') as f2:
#         f2.write(f.read())


with open("/Users/suhritsatyal/Desktop/python_softwarica1/filehandling/nice.txt","w") as f:
    x=['1,2,3','a,b,c']
    f.write(x)



