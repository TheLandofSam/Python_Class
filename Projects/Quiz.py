times = 0

questions = [
    {'question': 'In what state is Shoshone Falls located?', 
    'options': ['a) Minnesota','b) Wisconsin','c) Idaho','d) Washington'],
    'answer': 'c'},
     {'question': 'Where is Arches National Park located?', 
    'options': ['a) Arizona','b) Utah','c) Colorado','d) New Mexico'],
    'answer': 'b'},
     {'question': 'If you visit Yosemite National Park, what state would you be in?', 
    'options': ['a) Wyoming','b) Colorado','c) Idaho','d) None of the above'],
    'answer': 'd'},
     {'question': 'In what state is Grand Teton National Park located?', 
    'options': ['a) Montana','b) Idaho','c) Wyoming','d) Utah'],
    'answer': 'c'},
     {'question': 'If you were to climb Mt. Rainer, in what state would you be climbing?', 
    'options': ['a) Washington','b) California','c) Oregon','d) Colorado'],
    'answer': 'a'},
]

for question in questions:
    print(f'?\n{question['question']}')
    for option in question['options']:
        print(f'⭕ {option}')
    
    answer=input('What say you: a/b/c/d ? ')
    if answer.lower() == question['answer']:
        times += 1
        print('Excellent!')
    else:
        print('Fail!')
    
    print({'⭐' * times})

if times == len(questions):
    print('Perfect score! 🥇')
elif times >= 3:
    print('Okay, not bad!')
else:
    print('💩')