import random
first_num = random.randint(2,10)
second_num = random.randint(2,10)
quest = str(first_num)+ "*" + str(second_num) + ":"

while True:
    
    answer = int(input(quest))
    if answer == first_num * second_num:
        print('맞았습니다')
        break
