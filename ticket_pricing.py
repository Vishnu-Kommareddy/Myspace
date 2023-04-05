print('Welocme to the roller coaster!')
height=int(input('enter your height: '))
if height >=120:
    age=int(input('enter your age: '))
    if age <=12:
        photo=str(input('do you want your photo? choose Y/N : '))
        if photo=='Y':
            print('pay $8')
        else:
            print('pay $5')
            
    elif age<=18:
        photo=str(input('do you want your photo? choose Y/N : '))
        if photo=='Y':
            print('pay $10')
        else:
            print('pay $7')
    else:
        photo=str(input('do you want your photo? choose Y/N : '))
        if photo=='Y':
            print('pay $15')
        else:
            print('pay $12')
else:
    print('come back once you grow taller.')