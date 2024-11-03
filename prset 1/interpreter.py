inpt = input('Expression: ').split()
a = float(inpt[0])
b = float(inpt[2])
opr = inpt[1]
if opr == '+':
    print(f"{a+b:.1f}")
elif opr == '-':
    print(f"{a-b:.1f}")
elif opr == '*':
    print(f"{a*b:.1f}")
elif opr == '/':
    print(f"{a/b:.1f}")
