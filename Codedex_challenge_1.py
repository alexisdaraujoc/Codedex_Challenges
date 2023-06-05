# Codedex Challenge 1: Create a food rating system

print('Welcome to the codedex restaurant food review page 🍔🍕🍟')
stars = int(input('\nEnter your food review ⭐⭐⭐⭐⭐ (1 to 5 stars): '))

if stars == 1:
    print('Poor ⭐')
elif stars == 2:
    print('Fair ⭐⭐')
elif stars == 3:
    print('Good ⭐⭐⭐')
elif stars == 4: 
    print('Excellent ⭐⭐⭐⭐')
elif stars == 5:
    print('Extraordinary ⭐⭐⭐⭐⭐')
else:
    print('Remember rate between 1 to 5 stars thank you 🙏')
    