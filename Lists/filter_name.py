'''
Create a function filter_name() that takes a list of countries names as argument. Take name of country as user input and check 
if the country is present in the list. If present, display the name of the country and the index position in the list, otherwise display "Invalid country name"
'''

def filter_name(countries):
    a=input("Enter a country name: ")
    if countries == list:
        countries.index(a)
        print(countries)
    else:
        print("Invalid country name")
list=["USA", "UK", "Israel", "Romania", "Moldova", "India", "Ireland", "France", "Germany", "Spain", "Andorra", "Portugal", "Swizerland"]
filter_name(list)
