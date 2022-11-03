from random import randint

minVal = 1
maxVal = 6

while True:
    print(f"Dice rolled to: {randint(minVal, maxVal)}")
    userWantsToQuite = input('Do you want to quit: (yes/no) \n')
    if userWantsToQuite == 'yes':
        print('Over')
        break


