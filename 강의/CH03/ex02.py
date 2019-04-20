americano_price = 2000
cafelatte_price = 3000
capucino_price = 3500

americanos = int(input("아메리카노 판매 개수: "))
lattes = int(input("카페라테 판매 개수: "))
capu = int(input("카푸치노 잔수: "))
sum_all = 0
sum_all = americano_price * americanos
sum_all = sum_all + cafelatte_price * lattes
sum_all = sum_all + capucino_price * capu

print("총매출은"+ str(sum_all) +"원 입니다.")


