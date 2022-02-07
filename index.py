import random, os

w = 0
r = 0
while True:
    QPass = 0
    os.system('cls')
    one = random.randint(0, 100)
    two = random.randint(0, 100)
    print (f'R / W = [ {r} / {w} ]')
    try:
        ans = input(f'{one} - {two} = ')
        if ans == 'Exit()':
            # w += 1
            print('\nAnswer OF Question ' + str(r + w) +
                  ' IS ' + str(one - two) + ' ...')
            print('\nGood luck Try Next Time...\n')
            print('Questions = ' + str(w + r))
            print('Solved = ' + str(r))
            print('Not-Solved = ' + str(w))
            input('\n Press Any Key To Exit: ')
            break
            
    except:
        ans = 'a'
    try:
        ans2 = int(ans)
    except:
        ans = '0'
        QPass = 1
    if int(ans) == one - two:
        r += 1
    else:
        if QPass == 1:
            pass
        else:
            w += 1
            print ('\nAnswer OF Question ' + str(r + w) + ' IS ' + str(one - two) + ' ...')
            print ('\nGood luck Try Next Time...\n')
            print ('Questions = ' + str(w + r) )
            print ('Solved = ' + str(r))
            print ('Not-Solved = ' + str(w))
            input('\n Press Any Key To Exit: ')
            break
