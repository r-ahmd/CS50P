while True:
    try:
        a,b = input('Fraction: ').split('/')
        a, b=int(a), int(b)
        if b<a:
            raise Eaception
        elif b==0:
            raise ZeroDivisionError
    except:
        pass
    else:
        break

percent = (a/b)*100
if percent <= 1:
    print('E')
elif percent >= 99:
    print('F')
else:
    print(f'{percent:.0f}%')
