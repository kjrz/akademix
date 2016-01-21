import os
from random import shuffle

qa_list = []

question = ''
answer = None

with open('akademix.txt') as f:
    for line in f.readlines():
        if line[:2] == '--' and answer is None:
            answer = ''
        elif line[:2] == '--':
            qa_list.append((question, answer))
            question = ''
            answer = None
        elif answer is None:
            question += line
        else:
            answer += line

shuffle(qa_list)

clear_screen_command = 'cls' if os.name == 'nt' else 'clear'

for qa in qa_list:
    os.system(clear_screen_command)
    print '\n', qa[0]
    raw_input('[ENTER]')
    os.system(clear_screen_command)
    print '\n', qa[0], qa[1].rstrip(), '\n'
    raw_input('[ENTER]')

os.system(clear_screen_command)
