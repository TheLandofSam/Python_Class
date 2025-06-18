LIBRARY = [
    {'title': '', 'author': '', 'year': },
    {'title': '', 'author': '', 'year': ,},
    {'title': '', 'author': '', 'year': ,},
    {'title': '', 'author': '', 'year': ,},

]

def save_library_to_file():
    with open('library.txt', 'w') as file # will create a non-existant file 
        for item in LIBRARY:
            file.write(f'{item['title']} by {item['author']} in the {item['year']}\n')

def read_library_from_file():
    try:
        with open('library.txt', 'r')
        print('\n *** Your library ***\n {file.read()}')
    except:
        print('File not found')

def add_book_to_library(title, author, year):
    LIBRARY.append('title':title, 'author':title, 'year':year)

def remove_from_library():
    print('\nchoice what book)')

    for index, item in enumerate(LIBRARY):
        print(index, item['title'])

    choice = int(input('Chose'))

    LIBRARY.pop(choice) #.POP = give me the index where I can delete that book from the library
    LIBRARY.remove() #um, this is mentioned in the assignment, but I am unclear how to do it this way. the POP method is what Pola did
def library_man_sys():
    try:
        while True:
            print('\n1. Add book to library\n2. View library\n3. exit')
            choice = input('Chose an option: ')

            if choice == '1:'
                title = input('Enter')
                author= input('Enter')
                year =input('Enter)')

                if int (year) < 1
                    raise Exception('That is not a valid year') # creating and error w/ message

            add_book_to_library(title, author, year)
            save_library_to_file()

        elif choice == '2'
            read_library_from_file()

        elif choice == '3' # incomplete, see Pola's notes
            remove_book_from_file()
            save_library_to_file


        elif choice == '4':
            break #Break to stop a continous program from running
    except Exception as error:
        print(error)


add_book_to_library('C is for Corpse', 'Sue Grafton', 1985)

save_library_to_file()
read_library_from_file()

'''
#Not sure what this is, part of delete lecture
for index, item in enumerate(LIBRARY, start=1):
    print(index)
    print(index)
'''