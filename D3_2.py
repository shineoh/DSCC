#객체지향 연습문제
#Q1. 학생 클래스
class Student:
    def __init__(self, kor, mat, eng):
        self.__kor = kor
        self.__mat = mat
        self.__eng = eng
 
    @property
    def kor(self):
        return self.__kor
 
    @property
    def mat(self):
        return self.__mat
 
    @property
    def eng(self):
        return self.__eng
 
    def get_total(self):
        return self.__kor + self.__mat + self.__eng
 
 
t_str = input()
t_str = t_str.split(", ")
t_str = list(map(int, t_str))
student = Student(t_str[0], t_str[1], t_str[2])
print("국어, 영어, 수학의 총점: {0}".format(student.get_total()))

#Q2. 국적 
class Korean:
    Nationality = "대한민국"
 
    @classmethod
    def printNationality(cls):
        return cls.Nationality
 
 
print(Korean.printNationality())
print(Korean.printNationality())

#Q3. 부모자식 클래스 정의
class Student:
    def __init__(self, name):
        self.__name = name
 
    @property
    def name(self):
        return self.__name
 
    def __repr__(self):
        return "이름: {}".format(self.name)
 
 
class GraduateStudent(Student):
    def __init__(self, name, major):
        super().__init__(name)
        self.__major = major
 
    @property
    def major(self):
        return self.__major
 
    def __repr__(self):
        return super().__repr__() + ", 전공: {}".format(self.major)
 
 
s1 = Student("홍길동")
s2 = GraduateStudent("이순신", "컴퓨터")
print(s1)
print(s2)

