
class Subject:
    def __init__(self):
        self.score = None
        self.subject_name = None
        self.max_score = None

    def get_subject_name(self):
        return self.subject_name 

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def get_max_score(self):
        return self.max_score

class Korean(Subject):
    def __init__(self):
        self.subject_name = "국어"
        self.max_score = 100

class Math(Subject):
    def __init__(self):
        self.subject_name ="수학"
        self.max_score = 100

class History(Subject):
    def __init__(self):
        self.subject_name = "역사"
        self.max_score = 50

class Student:
    def __init__(self, name):
        self.name = name
        self.kor = Korean()
        self.math = Math()
        self.his = History()
        self.subjects = [self.kor,self.math,self.his]

    def get_name(self):
        return self.name
    
    def make_sum(self):
        sum_score = self.kor.score + self.math.score + self.his.score
        return sum_score
    
    def print(self):
        print(f"===== Student {self.name} =====")
        for i in self.subjects:
            print(f"{i.subject_name} : {i.score} / {i.max_score}")

def print_rank(students):
    students = sorted(students,key=lambda student : student.make_sum(),reverse=True)
    sum_max_score=0
    for k in students[0].subjects:
        sum_max_score+=k.max_score

    for j in range(len(students)):
        print(f"Rank {j+1} : {students[j].name} ({students[j].make_sum()} / {sum_max_score})")

# 실행 함수 (수정하지 마세요. 코드 테스트용 함수입니다.)
def Test():
    n = int(input("How many students: "))

    students = []

    for i in range(n):
        name = input("Name of Student: ")

        student = Student(name)

        for subject in student.subjects:
            score = int(input("Score of %s : " %subject.get_subject_name()))
            subject.set_score(score)

        print()
        student.print()
        print()
        students.append(student)

    print("===== Rank =====")
    print_rank(students)

Test()