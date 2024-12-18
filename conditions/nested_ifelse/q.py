str=input("Enter a city:").lower()
dict={
    'delhi':'Red Fort',
    'agra':'Taj Mahal',
    'jaipur':'Jal Mahal'
}
if(str not in dict):
    print("invalid city")
else:
    print(f'Monument of {str} is {dict[str]}')