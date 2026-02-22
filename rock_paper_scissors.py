import random

option=input('enter yes to play or no to leave:')
opt=option.lower()

while opt=='yes':
    print('instructions')
    print('enter (0 for rock) (1 for paper (2 for scissors)')

    tools =['rock','paper','scissors']

    user_input=int(input('your move:'))
    com_input =random.randrange(0,2)

    print(f'you chose= {tools[user_input]}')
    print(f'computer chose= {tools[com_input]}')

    possibilities=[
    [0,-1,1],
    [1,0,-1],
    [-1,1,0]
    ]

    result=possibilities[user_input][com_input]

    if result==1:
        print('you won\n')
    elif result == 0: 
        print('match draw\n')
    else:
        print('you lose\n')

    anthr=input("want another round:")
    anthr.lower()

    if anthr!="yes":
        exit("thnx for playing")
        

else:
    exit("thankyou for playing")
                   