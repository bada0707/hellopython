su = int(input("네자리 이하정수를 입력하시오"))










su_1000 = su

su_1 = su % 10

su_2 = (su % 100 - su_1)//10

su_3 = (su % 1000 - su % 100)//100

su_4 = (su % 10000 - su % 1000)//1000

also = su_1 + su_2 + su_3 + su_4



print('자리수의 합', also)
