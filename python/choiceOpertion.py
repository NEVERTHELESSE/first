def opertion():
  number = input('''
  Which operation did you want to perform
  (a): addition
  (b): subtraction
  (c): multiplication
  (d): division
  (e): find the reminder
  (f): square root
''')
  print('Okey!! Let start the',number)
  firstNumber = input('Kindly provide your first Number:  ')
  secondNumber = input('Kindly provide your second Number:  ')
  try:
    firstNumber = int(firstNumber)
    secondNumber = int(secondNumber)
    if (number == 'a'):
        print('Your answer is ',firstNumber+secondNumber)
    elif (number == 'b'):
      print('Your answer is ',firstNumber - secondNumber)
    elif (number == 'c'):
      print('Your answer is ',firstNumber * secondNumber)
    elif (number == 'd'):
      print('Your answer is ',firstNumber / secondNumber)
    elif (number == 'e'):
      print('Your answer is ',firstNumber % secondNumber)
    elif (number == 'f'):
      print('Your answer is ',firstNumber ** secondNumber)
  except:
    print('it seem like you enter an invalid digit!!, make sure you enter a number and try again!! you are welcome')


opertion()