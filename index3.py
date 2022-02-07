import random
import os

w = 0
r = 0

os.system('cls')

# table = int(input ('Table = '))

while True:
    QPass = 0
    os.system('cls')
    one = random.randint(25, 30)
    # two = random.randint(1, 10)
    print(f'R / W = [ {r} / {w} ]')
    try:
        ans = input(f'{one} * {one} = ')
        if ans == 'Exit()':
            # w += 1
            print('\nAnswer OF Question ' + str(r + w) +
                  ' IS ' + str(one * one) + ' ...')
            print('\nGood luck Try Next Time...\n')
            print('Questions = ' + str(w + r))
            print('Solved = ' + str(r))
            print('Not-Solved = ' + str(w))
            input('\nPress Any Key To Exit: ')
            os.system('cls')
            break

    except:
        ans = 'a'
    try:
        ans2 = int(ans)
    except:
        ans = '0'
        QPass = 1
    if int(ans) == one * one:
        r += 1
    else:
        if QPass == 1:
            pass
        else:
            w += 1
            print('\nAnswer OF Question ' + str(r + w) +
                  ' IS ' + str(one * one) + ' ...')
            print('\nGood luck Try Next Time...\n')
            print('Questions = ' + str(w + r))
            print('Solved = ' + str(r))
            print('Not-Solved = ' + str(w))
            input('\nPress Any Key To Exit: ')
            os.system('cls')
            break
    if w + r > 9:
        os.system('cls')
        print('\nGood Job...\n')
        print('Questions = ' + str(w + r))
        print('Solved = ' + str(r))
        print('Not-Solved = ' + str(w))
        input('\nPress Any Key To Exit: ')
        os.system('cls')
        break
