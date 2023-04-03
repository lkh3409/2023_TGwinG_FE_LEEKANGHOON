# 1번
def grade(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"
# 2번
def quadrant(x,y):
    if x>0:
        if y>0:
            return "제 1사분면"
        if y<0:
            return "제 4사분면"
    if x<0:
        if y>0:
            return "제 2사분면"
        if y<0:
            return "제 3사분면"

# 3번
def leapYear(year):
    if year%4==0:
        if (year%100==0) and (year%400!=0):
            return "평년"
        else:
            return "윤년"
    else:
        return "윤년"

# 4번
def dice(a, b, c):
    if a==b==c:
        return 10000 + (a*1000)
    elif a==b or b==c:
        return 1000 + b*1000
    elif a==c:
        return 1000 + a*1000
    else:
        return max(a,b,c)*100
# 5번
def alarm(time):
    time = str(time)

    if len(time) == 4 :
        hour = int(time[:2])
        minute = int(time[2:])
        if minute >=45:
            minute-=45
            hour=str(hour)
            minute=str(minute)
        else:
            minute+=15
            hour-=1
            hour=str(hour)
            minute=str(minute)
        return hour+"시"+minute+"분"
        
    elif len(time) == 3 :
        hour = int(time[:1])
        minute = int(time[1:])
        if minute >=45:
            minute-=45
            hour=str(hour)
            minute=str(minute)
        else:
            minute+=15
            hour-=1
            hour=str(hour)
            minute=str(minute)
        return hour+"시"+minute+"분"
    else:
        minute=int(time)
        if minute>=45:
            minute-=45
            hour = "0"
            minute=str(minute)
        else:
            minute+=15
            hour = "23"
            minute=str(minute)
        return hour+"시"+minute+"분"
    