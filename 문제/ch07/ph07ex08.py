def add(a,b):
    print(a,"+",b,"=",a+b)
    
def sub(a,b):
    print(a,"-",b,"=",a-b)
    
def mul(a,b):
    print(a,"*",b,"=",a*b)
    
def div(a,b):
    print(a,"/",b,"=",a/b)
    

first = int(input("첫번째 수를 입력하세요"))
second = int(input("두번째 수를 입력하세요"))
sym = input("사칙연산중 하나를 입력하세요")

if sym == "+":
    result = add(first,second)
elif sym == "-":
    result = sub(first,second)
elif sym == "*":
    result = mul(first,second)
elif sym == "/":
    result = div(first,second)
