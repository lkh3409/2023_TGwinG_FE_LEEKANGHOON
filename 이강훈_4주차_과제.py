# # your code 를 지우고 그 부분에 본인의 코드를 작성해주세요.
# 4주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# 제출 기한 : 2023년 4월 10일 23시 59분
# 지각 제출 기한 : 2023년 4월 11일 23시 59분

# 1번
def double(lst):
    count=0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i]*2==lst[j]:
                count+=1
    return count

# 2번
def pascal(n):
    pas=[]
    for i in range(n):
        lst1 = []
        for j in range(i+1):
            if j==0 or j==i:
                lst1.append(1)
            else:
                lst1.append(pas[i-1][j]+pas[i-1][j-1])
        pas.append(lst1)
    return(pas[n-1])

# 3번
def beerRefrigerator(n):
    bestCase = []
    bestScore = 0
    for x in range(1,n+1):
        if n%x==0:
            x2=n//x #n을 x로 나눈 값
            for y in range(1,x2+1):
               if x2%y==0:
                   y2=x2//y #n을 x로 나눈 값을 y로 나눈 값 == z
                   z=y2
                   group = [x,y,z]  
                   score = x + y + z #겉넓이 공식 == 2(x+y+z)
                   if not bestCase or bestScore > score:
                      bestCase = group
                      bestScore = score
    bestCase = sorted(bestCase, reverse=True)
    return f"{bestCase[0]} X {bestCase[1]} X {bestCase[2]}"

# 4번
def matrixMul(mat1, mat2):
    result=[]
    for i in range(len(mat1)):
        lst3 =[]
        for j in range(len(mat2[0])):
            update = 0
            for k in range(len(mat2)):
                update += mat1[i][k] * mat2[k][j] 
            lst3.append(update)
        result.append(lst3)
    return result




