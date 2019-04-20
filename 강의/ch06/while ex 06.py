import random
count = 1
comp_num = random.randint(10,99)

while True:
    user_num = int(input("숫자를 입력하세요"))
    if comp_num == user_num:
        print('정답!')
        break
    elif comp_num > user_num:
        print('숫자가 작습니다, 큰수를 입력하세요')
    else:
        print('숫자가 큽니다, 작은수를 입력하세요')
    count = count + 1

print(count, '번만에 맞추셨네요ㅋㅋㅋㅋ')
