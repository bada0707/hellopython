import random

lotto_num = random.randint(10,99)
#print(lotto_num)

user_num = int(input('복권번호를 입력하시요(10부터 99까지)'))

print('복권번호는',lotto_num,'입니다.')



if user_num == lotto_num:
    print('100만원 당첨!')
elif (lotto_num//10 == user_num//10) or (lotto_num%10 == user_num%10):
    print('50만원 당첨! 돈벌기 쉽네요')
else:
    print('꽝!')
