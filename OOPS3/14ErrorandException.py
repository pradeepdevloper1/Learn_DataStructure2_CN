
# try:
#     n=input('Enter the numerator :')
#     num=int(n)
#     n=input('Enter the denominator :')
#     denom=int(n)

#     value=num/denom
#     print(value)
# except  ValueError:
#     print('numerator and denominator should be integer')
# except ZeroDivisionError:
#     print('denominator should not be zero')


try:
    n=input('Enter the numerator :')
    num=int(n)
    n=input('Enter the denominator :')
    denom=int(n)

    value=num/denom
    print(value)
except  (ValueError,ZeroDivisionError):
    print('numerator and denominator should be integer   or denominator should not be zero')
