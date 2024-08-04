base = 2          # 변수
 
def square(n):    # 함수
    """return n-squared value of base"""
    return base ** n

class Person:    # 클래스
    def __init__(self, name, age, address):
        """Person class initialization"""
        self.name = name
        self.age = age
        self.address = address
 
    def greeting(self):
        """greeting message print out"""
        print('안녕하세요. 저는 {0}입니다.'.format(self.name))

# C 의 main 함수처럼 이렇게 starting point 를 만들어 주면 된다.
# Library function 을 이렇게 test 를 하고, 그대로 다른 file 에서 불러쓰면 된다.
if __name__ == '__main__':
    print(square(10)) 