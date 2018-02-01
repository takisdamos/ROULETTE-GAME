mport random
print('*** - YOUR - ***********************')
print('************ - LUCKY - *************')
print('***** - GAME - *********************')
print('************************************')
print('**** - IS - ******* - NOW - ********')
print('************************************')
print('************ - READY - *************')
print('************************************')

while True:
    num=random.randint(0,36)
    print(' \n Your Lucky number is :',num)
    # Checking if the number is ZERO
    if num == 0:
        print (' You get the number ZERO \n')
        continue
    # Checking for Small or Big number
    elif num<=17:
        size=' S M A L L '
    else:
        size=' B I G '
    # From here i check for Color and Type 
    if num>0 and num <=10:
        if num % 2 ==0:
            color=' B L A C K '
            tipos=' E V E N '
        else:
            color=' R E D '
            tipos=' O D D '

    if num>18 and num<=28:
        if num % 2 ==0:
            color=' B L A C K '
            tipos='E V E N'
        else:
            color=' R E D '
            tipos=' ODD'
    if num>10 and num<=18:
        if num % 2==0:
            tipos=' E V E N'
            color=' R E D '
        else:
            color=' B L A C K '
            tipos=' ODD '
            
    if num>28 and num<=36:
        if num % 2 ==0:
            tipos=' E V E N '
            color=' R E D '
        else:
            color=' B L A C K '
            tipos=' ODD'
    print('\n Your num is :',size, tipos, color)
    # Check if the game is going to stop or not !!!!
    s=input('\n If you want to play again click on ENTER key  - If you don''t type the Letter q \n')
    if s=='q'or s=='Q':
        break
    elif s=='':
        continue
print('\n***** You decide to put an END...*****\n Than''s a lot for your time ! ')

# what if i type the letter 't'?????????? or something else??????
