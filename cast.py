#input numbers
num1=input('Please enter a whole number:')
num2=input('Now enter another whole number:')
print('Input is:',type(num1),type(num2))

#addition
total=num1+num2
print('Total:',total,type(total))

#re-addition
total=int(num1)+int(num2)
print('Total:',total,type(total))

#store and concatenate
total=float(num1)+float(num2)
print('Total:'+str(total),type(total))
