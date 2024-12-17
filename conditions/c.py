dict_this={
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"

}

a=eval(input("Enter from 1 to 12:"))
if(a>12 or a<1):
    print("Invalid number")
else:
    print(dict_this[a])