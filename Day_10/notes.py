import re

#extract cat from the text
text = 'My cat is being so lazy,'

is_match = re.search(r'cat', text) # r before quotes you are telling python that you start tp creating a pattern

if is_match:
    print('cat')
else:
    print('no cat')
'''
 Read document
with open(data.txt, r) as file
    content = file.read()
    pattern= r'[a-zA-Z0-9._]+@[a-z]+\.[a-z]+'

#url
#(http|https):\/\/www.[a-zA-Z0-9]+.(com|net) #\ if you need a literal



\d matches numbers
[.-] will match characters in the brackets, acts as an or, can also put a regex in the bracket like such [\s.-] (which stands for space, period, or dash)

abcdefghijklmnopqurtuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890
\. tells the system the . is literal [a-zA-Z]
() says it is a group of words such as (com|edu|net)
Ma MaMa

MetaCharacters:
.[{()\^$|?*+

codeworks.com

321-555-4321
123.555.1234

Mr. Mick
Mr Jake
Ms Paula
Mrs. Robinson
Mr. T

My cat is being so lazy, my cat does not like to be pet sometimes, my cat is a grumpy old cat
'''