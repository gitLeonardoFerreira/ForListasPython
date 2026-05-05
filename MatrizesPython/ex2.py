n = 7
primo = True
for divisor in range (2, n):
    if n % divisor == 0:
        primo = False
        break
if primo:
    print('É primo')
else:
    print('Não é primo')