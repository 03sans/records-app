def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('error:division by zero!')
    except TypeError as e:
        print(f'error: {e}')
    else:
        print(f'result: {result}')
    finally:
        print('execution completed')

divide(10,2)
divide(10,0)
divide(10, 'a')

#recursive function
def facto(n):
    if n == 0:
        return 1
    else:
        return n * facto (n - 1)
    
num = 4
print(f'the factorial of {num} is {facto(num)}')