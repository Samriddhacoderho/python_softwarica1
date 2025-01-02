# 13. Accept string from the user and display only those characters which are 
# present at an even index.

str="programming"
for i in range(0,len(str),2):
    print(str[i],"=",i)