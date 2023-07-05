# Codedex Challenge 5: Planet Weights

print('''To calculate your weight, indicate 
your weight on earth  and the number 
of the planet you are going to

Number	Planet	    Relative Gravity
  1	Mercury	        0.38
  2	Venus	        0.91
  3	Mars	        0.38
  4	Jupiter	        2.53
  5	Saturn	        1.07
  6	Uranus	        0.89
  7	Neptune	        1.14''')

earth_weight = float(input('\nEnter your weight on earth: '))
planet_number = int(input('Enter the planet number: '))

if planet_number == 1:
    relative_gravity = 0.38
elif planet_number == 2:
    relative_gravity = 0.91
elif planet_number == 3:
    relative_gravity = 0.38
elif planet_number == 4:
    relative_gravity = 2.53
elif planet_number == 5:
    relative_gravity = 1.07
elif planet_number == 6:
    relative_gravity = 0.89
elif planet_number == 7:
    relative_gravity == 1.14
else:
    print('Not Valid Planet Number')
    
destination_weight = earth_weight * relative_gravity
print('\nYour destination weight is: ', round(destination_weight, 2))