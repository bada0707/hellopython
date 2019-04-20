count = 1
sum_all = 0


while True:
    num = int(input("숫자를 입력하세요"))
    sum_all = sum_all + num
    yesno = input("계속(yes/no)")
    if yesno== "no":
          break
    count = count + 1
ave = sum_all / count
          

print("합계", sum_all)
print("평균", ave)
