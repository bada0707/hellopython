gr = int(input('성적입력하세요'))

if gr > 100 or gr <0:
    print('장난치지 마세요;;')
elif gr >= 90:
    print('A학점입니다')
elif gr >= 80:
    print('B학점입니다')
elif gr >= 70:
    print('C학점입니다')
elif gr >= 60:
    print('D학점입니다')
else :
    print('F학점이시네요 인생도 접으세요ㅋㅋㅋ')
