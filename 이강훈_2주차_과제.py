# 1번
def sum(a, b):
    return a+b

# 2번
def sub(a, b):
    return a-b

# 3번
def mul(a, b):
    return a*b

# 4번
def div(a, b):
    return a/b

# 5번
def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

# 6번
def title():
    lylics = "Switch sides and I'm beside you."
    return lylics[21:31]

# 7번
def reverseStr(string):
    return string[::-1] 

# 8번
def introduce():
    name = input('이름을 입력하세요 : ')
    hobby = input('취미를 입력하세요 : ')
    school = input('재학 중인 학교를 입력하세요 : ')
    birth = input('생일을 입력하세요 : ')
    print("제 이름은 %s입니다. 취미는 %s입니다. 저는 %s를 다니고 있습니다. 제 생일은 %s월 %s일 입니다."%(name,hobby,school,birth[2:4],birth[4:]))
 
# 9번
def calc():
    a=input("첫 번쨰 수를 입력하세요 : ")
    b=input("두 번쨰 수를 입력하세요 : ")
    a=int(a)
    b=int(b)
    print("두 수의 합 :",a+b)
    print("두 수의 차 :",a-b)
    print("두 수의 곱 :",a*b)
    print("두 수의 몫 : ",a//b)


#실행
result1=distance(1,1,0,0) #거리 함수 실행,출력
print(result1)
result2=title() #문자열 슬라이싱 실행,출력
print(result2)
result3 =reverseStr("이강훈") #문자열 뒤집기 실행
print(result3) 
introduce() #소개함수 실행
calc() #계산함수 실행


