a = input ('File: ').lower().strip()

dot = a.rfind('.')

filetype = a[dot:]

if filetype == '.jpg' or filetype == '.jpeg':
    print('image/jpeg')
elif filetype == '.gif':
    print('image/gif')
elif filetype == '.png':
    print('image/png')
elif filetype == '.pdf':
    print('application/pdf')
elif filetype == '.txt':
    print('text/plain')
elif filetype == '.zip':
    print('application/zip')
else :
    print('application/octet-stream')
