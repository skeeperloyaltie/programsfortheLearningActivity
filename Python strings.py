#Python strings

#Creating strings

print ('Creating strings')

print ('Enter a word(most probably a name): ')

string1 = str(input())
print('Enter a text word entered is: ', string1)

#Accessing string characters + sring Slicing
print('Dear ' + string1[0 : -1] + ' Welcome to Programming.')
    


#Updating a string

string1 = 'shwwepered'

print('\nUpdated string', string1)

#deleting a string

del string1

#formating a string

s = '{} {} {} {}'.format('Godfrey', 'is', 'a', 'geek')
print(s)


