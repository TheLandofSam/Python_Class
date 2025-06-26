from ast import pattern
from contextlib import ContextDecorator
import re

#read doc
'''
with open('data.txt', 'r') as file:
    try:
        content = file.read()
        pattern = r'[a-zA-Z0-9._]+@[a-z]+\.[a-z]+'
    except:
        print('File not found')

#telephones

    pattern = r'\d{3}[*\s.-]?\d{3}[*\s.-]?\d{4}'
    phones = re.findall(pattern, content)
    
    for phone in phones:
        print(f'📞 {phone}')

#emails

    pattern = r'[a-zA-Z0-9-._]+@[a-z]+\.(?:com|edu|net)+'
    emails = re.findall(pattern, content)

    for email in emails:
        print(f'📧 {email}')

#Names and Titles

    pattern = r'(?:Mr|Ms|Mrs)[.\s]\s?[a-zA-Z]+'
    names = re.findall(pattern, content)

    for name in names:
        print(f'🧑{name}')

#test recall of newly added data
#with open('data.txt', 'r') as file:
#    content = file.read()
#    print(content)

#pattern = r'?\d{3,4}\w{4,7}?\d{5}'
'''
with open('data.txt', 'r') as file:
    try:
        content = file.read()
    except:
        print('File not found')
    
    pattern = r'^\d{3,4}.+$\d{5}'
    addresses = re.findall(pattern, content)
    for address in addresses:
        print(f'🏠 {address}')
