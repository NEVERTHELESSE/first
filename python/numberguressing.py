import random
def numberGuessinggame():
  print('Welcome to number guessing game the computer have generate a number from 1 to 100 for you try to guess it')
  computerNumber = random.randint(1,100)
  print(computerNumber)
  userNumber = int(input('Kindly enter your number:  '))
  while userNumber != computerNumber:
    userNumber = int(input('Kindly enter your number:  '))
    if (computerNumber > userNumber):
      print('The number is greater than: ',userNumber, 'kindly try again!!')
      userNumber = int(input('Kindly enter your number:  '))
    elif (computerNumber < userNumber):
      print('The number is less than ',userNumber, 'kindly try again!!')
      userNumber = int(input('Kindly enter your number:  '))
    else:
      print('you are correct')

numberGuessinggame()
# a = 4
# while a < 10:
#   print(a)
#   a = a+1