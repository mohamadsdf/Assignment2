from operator import le
import random


words = ['amir', 'sina', 'mmd','alireza', 'mehrdad', 'samira', 'mahshid', 'yegane', 'behnaz','golabi']

# index =random.randint(0,9)

# word = words[index]

word = random.choice(words)
true_char = []
joon = 6
while(True):
    for item in range(len(word)):
        if word[item] in true_char:
            print(word[item], end='')
        else:    
            
            print("-",end ="")

    print('\nplease enter char')
    char = input()
    if len(char) == 1 :
        if char in word :
            true_char.append(char)
            print('yes')
        else:
            joon -=1
            print('joonet kam shod alan')
            print('joon baghi monde', joon)
        if(joon == 0) :
            print('bakhti!!!')
            break    
    else:
        print('ye ckakarkter vared kon')

    if len(true_char) == len(word) :
        print('bordi kalame in bod', word)   