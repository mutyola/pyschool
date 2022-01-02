import random
#initialise 3 var
num=random.randint(1,20)
flag=True
guess=0
#display message for  user guess
print('Guess my number 1-20:',end='')

#compare
while flag==True:
guess =input()
if not guess.isdigit():
print('Invalid!Enter only digits 1-20')
break
elif int(guess)<num:
print('Too low,try again:',end='')
else:
print('Correct...My number is'+guess)
flag=False
