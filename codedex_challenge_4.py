# Codedex Challenge 4: Seasons of the Year

print(''' Seasons of the year:
      ⛄ Winter 
      🌼 Spring 
      🌞 Summer   
      🍂 Autumn ''')

month = int(input('\nEnter number of the current month: '))

if month == 1 or month == 2 or month == 3:
    print('Season is Winter ⛄')
elif month == 4 or month == 5 or month == 6:
    print('Season is Spring 🌼')
elif month == 7 or month == 8 or month == 9:
    print('Season is Summer 🌞')
elif month == 10 or month == 11 or month == 12:
    print('Season is Autumn 🍂')
else:
    print('Invalid, year have only 12 months')


