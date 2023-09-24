# in, not, not in, is, is not

a=2
if a>5:
    print('5 er beshi')
elif a>3:
    print('olpo boro')
elif a==2:
    print('2 er soman')
else:
    print('choto')

boss=False

if boss is not True:
    print("tel marbo")
else:
    print("lunch er pore asen")


    # nested conditions
    coin='head'

    if boss==True:
        print('boss you are joss')
        if coin=='tail':
            print('batting')
        else:
            print('bowling')
            if 5>2 or boss!=True:
                print('do something')
                if 8%2==0 and 5%2==1:
                    print('even 9 is an even number')

    else:
        print('you are loss not a boss')