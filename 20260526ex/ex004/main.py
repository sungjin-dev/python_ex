from our_dice import Dice

def sortedNumbers(*numbers):
    list = sorted(numbers)
    list.sort(reverse = True)
    return list

game1Dice = Dice()
game2Dice = Dice()
game3Dice = Dice()

for i in range(5):
    game1Dice.playDice()
    game2Dice.playDice()
    game3Dice.playDice()

print(f'gamer1: {game1Dice.getNumbers()}')
print(f'gamer2: {game2Dice.getNumbers()}')
print(f'gamer3: {game3Dice.getNumbers()}')

print(f' sum of gamer1: {game1Dice.getSum()}')
print(f' sum of gamer2: {game2Dice.getSum()}')
print(f' sum of gamer3: {game3Dice.getSum()}')

sortedNumbers(game1Dice.getSum(),
              game2Dice.getSum(),
              game3Dice.getSum())

for idx, item in enumerate(sortedNumbers):
    if idx == 0:
        print(f'{idx+1}등 : {item} WINNER!!')
    else:
        print(f'{idx+1}등 : {item}')  

# print(f'1등: {sortedNumbers[0]} WINNER!!')
# print(f'1등: {sortedNumbers[1]} ')
# print(f'1등: {sortedNumbers[2]} ')

