# your code 를 지우고 코드를 작성하세요.
# 5주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# result, answer 변수를 사용하여 문제를 풀이하세요. 반환값은 result나 answer 변수입니다.
# 제출 기한: 2023년 4월 17일 23시 59분
# 지각 제출 기한: 2023년 4월 18일 23시 59분

import math

def calcCircleArea(r):
    result = float(math.pi*(r**2))
    return result

def calcLog(a, b):
    result = float(math.log(b,a))
    return result

def calcSin(x):
    result = float(math.sin(x))
    return result

def calcFactorial(x):
    result = int(math.factorial(x))
    return result

def calcCombination(n, r):
    result = int(math.comb(n,r))
    return result

def calculator(order):
    answer = 0
    euler = order.replace('e',str(math.exp(1)))
    orderlist = euler.split()
    if "원넓이" in order :
        ordernum = float(orderlist[-1])
        answer = calcCircleArea(ordernum)
    elif "로그" in order:
        ordernum1 = float(orderlist[-2])
        ordernum2 =float(orderlist[-1])
        answer=calcLog(ordernum1,ordernum2)
    elif "사인" in order:
        ordernum = float(orderlist[-1])
        answer = calcSin(ordernum)
    elif "팩토리얼" in order:
        ordernum = int(orderlist[-1])
        answer = calcFactorial(ordernum)
    else:
        ordernum1 =int(orderlist[-2])
        ordernum2 =int(orderlist[-1])
        answer=calcCombination(ordernum1,ordernum2)

    return round(answer,2)

print(calculator("원넓이: 10"))
print(calculator("로그: e 10"))
print(calculator("사인: 100"))
print(calculator("팩토리얼: 5"))
print(calculator("조합: 3 2"))

    


    