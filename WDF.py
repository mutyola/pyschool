# If file is existing, it appends. Otherwise, it creates
f2 = open('mydoc2', 'a')

# binary files
bf1 = open('mydoc3', 'wb')
bf2 = open('mydoc4', 'ab')

#####################################
# writing data

print('writing data into files...')
for index in range(1, 12):
    data = ''
    name = 'user ' + str(index-1)
    email = 'user' + str(index-1) + '@email.com'
    if index == 1:
        data = '{0:3s} {1:10s} {2:15s}\n'.format('No', 'Name', 'Email')
    else:
        data = '{0:3s} {1:10s} {2:15s}\n'.format(str(index-1), name, email)

    f1.write(data)
    f2.write(data)
    bf1.write(data)
    bf2.write(data)