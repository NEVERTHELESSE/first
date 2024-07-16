def multiplicationtable():
  print('Let build multiplication table')
  try:
    number = int(input('Enter the number you want to perform the operation on:  '))
    limit = int(input('Enter where you want the operation to stop:  '))
    step= input('If you want step then enter it else ignore it:  ')
    if (step==''):
      step = 1
    else:
      step = int(step)
    for i in range(1,limit+1, step):
      print(number,'x',i,'=',number*i)
  except:
    print('it seem like you enter an invalid digit!!, make sure you enter a number and try again!! you are welcome')

multiplicationtable()