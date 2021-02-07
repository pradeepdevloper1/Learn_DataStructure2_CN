# a=10/0
# a='1'+19
# a=b+8


try:
    n=input('Enter the numerator :')
    num=int(n)
    n=input('Enter the denominator :')
    denom=int(n)

    value=num/denom
    print(value)
except  ValueError:
    print('numerator and denominator should be integer')
