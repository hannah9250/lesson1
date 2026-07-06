country = {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}
user = input("enter the country name: ")
code = country.get(user)
if code: 
    print("country code", code)
else: 
    print("country not found")