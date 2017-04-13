digit, base = input('Enter a number to convert and separated with space number system:\n').split(' ')
wrongFormat = False

def PrintResult(result, operationType):
    if operationType =='2':
        primaryLenght = 6
    else:
        primaryLenght = 7
    i = 0        
    print('/', end='')
    while i < primaryLenght + len(str(num)):
        print('-', end='')
        i += 1
    print('\\')
    print('|', num, '|', operationType, '|')
    i=0
    print('\\', end='')
    while i < primaryLenght + len(str(num)):
        print('-', end='')
        i += 1
    print('/')

if base == '2':
    i = 0
    num = 0
    power = len(digit)
    for i in digit:
        if int(i) > 1:
            print('Wrong format')
            wrongFormat = True
            break            
        power = power - 1
        if i == '1':
            num = num + 2**power 
    if not wrongFormat:         
        PrintResult(num, '10')
elif base == '10':  
    i = 0
    num = ''
    while True:
        if 2**i <= int(digit):
            i += 1
        else:
            i -= 1
            break

    rest = int(digit)

    while i >= 0:
        if 2**i <= rest:
            num += '1'
            rest -= 2**i
        else:
            num += '0' 
        i -= 1   
    PrintResult(num, '2')
else:
    print('Wrong format')


