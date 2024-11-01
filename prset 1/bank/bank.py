greetings = input('Greeting: ').lower().strip()
if 'hello' in greetings:
    print('$0')
elif 'h' in greetings[0]:
    print('$20')
else:
    print('$100')
