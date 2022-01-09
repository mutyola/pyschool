#your code goes here
print('Welcome')
print('This is your Body Mass Index Calculator!')
weight = int(input('Enter your weight:'));
height = float(input('Enter your height:'));
x = weight/float(height*height);
if x < 18.5:
    print('You are Underweight.')
if x>=18.5 and x<25:
    print("You are Normal.")
if x >= 25 and x < 30:
   print('You are Overweight.')
if x >= 30:
   print('You are Obese.')
