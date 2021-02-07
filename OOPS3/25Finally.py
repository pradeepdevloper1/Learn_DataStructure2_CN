class ZeroDenominatorError(ZeroDivisionError):
    pass
while True:
    try:    
      n=input('Enter the numerator :')
      num=int(n)
      n=input('Enter the denominator :')
      denom=int(n)
      if denom==0:
          raise ZeroDenominatorError('Denominator should not be 0')
      value=num/denom
      
    except NameError:
        print('Name Error occured')
    except ZeroDivisionError:
        print('Division by Zero is not Allowed')
    except ZeroDenominatorError:
        print('ZeroDenominatorError is not Allowed')
    except :
        print('Some Error Occured ')        
    else:
        print(value)
        break
    finally:
        print(num)
        print(denom)
        print(value)
        print('exception may or may not Occur')
