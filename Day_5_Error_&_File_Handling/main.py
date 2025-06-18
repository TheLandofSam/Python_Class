'''
Error and File Handling
File Handling allows us to read and write files using Python built-in fxs

common modes

'r' read mode (default0

'w' write mode (overwrites file if it wxists))

'a' Append mode (ads content without overwriting)
Opening a File
Python provides the 'open()' fx to open files. The synax is:
file = open("file_name.txt", "mode")

enumerate fx gives you the index number
'''

open('file.txt.', 'r') #will open the file.txt to read it

#print(file.read())# can read a file with read

# read a file with keywd With

with open('file.txt', 'r') as file: # will saveall the information in file.txt as file
    content = file.read()
    print("This is read file")
    print(f'{content}')

# Read line by line
with open('file.txt', 'r') as file:
    for line in file:
        print(f'Read by line')

    '''
    if 'cat' in line:
        print('❕')

    '''
# Write file

with open('file.txt', 'w') as file:
    file.write('This is a writing mode')

# Appending to a file

with open('file.txt', 'a') as file:
    file.write('This is a append mode. This line is added. Also, Cats will someday rule the world...as soon as they are done napping.')

#Error Handling
'''
Python uses try-except blocks to handle errors
try:
    except:
        final:
'''
#Basic try

try:
    num = input('Enter a number')
    print(10 + num) #error is that num is  string which cannot be added to an int, change top line to num = int(input('Enter a number')) and it will work

    except:
        print('This is an error in the program')