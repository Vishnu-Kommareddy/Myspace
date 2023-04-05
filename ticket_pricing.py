print('Welocme to the roller coaster!')
height=int(input('enter oyur height: '))
if height >=120:
    age=int(input('enter your age: '))
    if age <=12:
        print('pay $5')
    elif age<=18:
        print('pay $7')
    else:
        print('pay $12')
else:
    print('come back once you grow taller.')