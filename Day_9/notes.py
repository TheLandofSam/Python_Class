'''
Python Packages, generators(fx using yield, good for memory) and time(library)

generators are a special type of fx in pyth that allow you to iterate over a seq of values without storing them in memory
generators are memory efficent
lazy eval - they create values only when required
useful for large data: if you need to process a large dataset, generators are better than lists

after a RETURN all the info disappears.

'''

def magic_hat(): #generator
    print('Wiz reaches into his magic hat')
    yield('A white rabit appears')
    print('Wiz reaches in to his coin purse')
    yield('a shiny old coin drops out')
    print('Wiz cuts into his mysterious box')
    yield('A body in half appears')
 
hat = magic_hat()

print(next(hat)) # Next allows me to access to the next yield item. This will allways give me the first value, if I add another ...
print(next(hat)) # this one will print the next one.

surprises = ['🐇', '🧣', '💀']

def magic_tricks():
    for surprise in surprises:
        yield surprise

tricks = magic_tricks()

for trick in tricks: # next() works like when you are in a loop, this takes place of the print(next(tricks)), works better if you have 100 items on your list
    print(trick)

#print(next(tricks))

