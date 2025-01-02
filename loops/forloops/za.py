# 36. removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython

bad_chars=[';',':','!','*']
str="Hello;S:am*rid!dha:;"
print("Removing bad characters:")
for i in str:
    if(i not in bad_chars):
        print(i,end="")
