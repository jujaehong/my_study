# function 함수 입
# 입력 -> 처리 > 출력
# input을 받아서 특정 작업을 수행하고 output(출력)을 반환한다.

# 내장함수(built-in)
# 파이썬이 기본적으로 제공해주는 함수
# print()
# len()
# int()
# float()
# str()
# list()
# range()

# abs()
# absolute의 약자
# 입력한 숫자형 데이터의 절댓값을 반환한다.
# print(abs(100)) #결과 100
# print(abs(-100)) #결과 100
# print(abs(3.15)) #결과 3.15
# print(abs(-3.15)) #결과 3.15

# sum(리스트)
# 리스트 안의 숫자를 더한 값을 반환한다.
# print(sum([1, 2, 3, 4, 5])) #결과 15

# max(리스트)
# 리스트 안에서 최댓값을 찾아 반환한다.
# print(max([1, 2, 3, 4, 5])) #결과 5

# min(리스트)
# 리스트 안에서 최솟값을 찾아 반환한다.
# print(min([1, 2, 3, 4, 5])) #결과 1

# chr()
# 정수 1개를 입력받고 해당하는 유니코드 문자를 반환한다.
# print(chr(65)) #결과 A

# ord
# 문자 1개를 입력받고 해당하는 저ㅓㅇ수를 반환한다.
# print(ord("A")) #결과 65


# round(값)
# round(값, 소수 자릿수)
# 반올림 함수
# print(round(1.234)) #결과 1
# print(round(1.234, 2)) #결과 1.23
# print(round(1.369, 1)) #결과 1.4 


# 함수 정의 (define)
# 함수 이름
# 함수 입력값 parameter
# 함수 결과값 return value

"""
def 함수이름(함수입력값):
    함수기능코드
    return 함수 결과값
"""
# def 함수를 정의하는 명령어
# 함수이름도 변수 이름처럼 규칙을 지켜서 지어야 한다.
# 영어, 숫자, _ 만 사용
# 숫자로 시작하면 안됨
# 띄어쓰기하면 안됨
# 키워드 사용하면 안됨
# 기존에 이미 정의된 함수 이름도 피하는것이 좋음.

# def print_names():  # print_name 라는 함수이름 정의
#     print("손흥민")
#     print("황희창")
#     print("김민재")
#     print("이강인") 
# print_names()

# a = print_names() #return 없으므로 None가 나온다.
# print(a)

# def get_name():
#     return "주재홍"  #방법1
# print(get_name())    #방법1

# def get_name():      # 방법2
#     return "주재홍"  # 방법2
# b = get_name()      # 방법2
# print(b) s          # 방법2


# parameter
# 함수에 입력하는 값
# 매개변수, argument 혼용

# def add(a, b): # 괄호안에 a, b 를 parameter 이라고 함.
#     return a + b
# result = print(add(1 , 2))
# print(result)

# def print_add(a, b):
#     print(a + b)
# print_add("하세요", "안녕")
# print_add(b="하세요",a="안녕") # 순서가 틀려도 매개변수를 지정하여 순서를 잡을 수 있다.



# def swap_number(a, b): # 함수안에 있는 변수는 지역변수 ( 함수안에서만 사용되는 변수 )
#     temp = a
#     a = b
#     b = temp
#     print(a,b)
#     return a, b


# a = 8 # 함수안에 있는 변수와 이름만 같은 전역변수(다른 값이다.)
# b = 9 # 함수안에 있는 변수와 이름만 같은 전역변수(다른 값이다.)

# print("함수 호출 전",a, b) 
# swap_number(1, 2)
# print("함수 호출 후",a, b)




# 다음 함수를 정의하세요.
# 함수 이름 : mul
# 함수 입력값 : 정수 2개
# 함수 출력값: 정수 2개의 곱

# def mul(a, b):
#     return a * b
# print(mul(3, 2))  #방법 1
    
# def mul(a, b):
#     return a * b
# result = mul(3,2) #방법 2
# print(result)     #방법 2


# 기본 값 매개변수
# default value parameter
# 함수 호출시 n2에 입력된 값이 없으면 기본값 사용
# def mul(n1, n2=1):
#     return n1 * n2
# print(mul(1,2)) # 결과 2
# print(mul(1)) # n2는 기본값 호출이 되어서 결과는 1

# def test_func(x, test=[]): # 기본값으로 리스트를 사용하면 계속 누적이 된다.
#     test.append(x)
#     print(x, test)
# test_func(1) # 첫번째 결과 1 [1]
# test_func(2) # 두번째 결과 1 [1, 2] 이렇게 첫번째가 누적되면서 두번째 결과가 합쳐진다.
# test_func(3) # 세번째 결과 1 [1, 2, 3] 이렇게 첫번째,두번째 누적되면서 세번째 결과가 합쳐진다.

# def test_func1(x, test=5):
#     test = test
#     print(x, test)

# test_func1(1) #결과 1 5 #누적이 없이 실행하는 결과만 출력
# test_func1(2) #결과 2 5 #누적이 없이 실행하는 결과만 출력 

# def test_func1(x, test=5):
#     if test == None:
#         test = []
#         test.append(x)
#     print(x, test)


# 기본값이 있는 매개변수는 기본값이 없는 매개변수보다 뒤에 위치해야 함.


# 1 ~ 10까지 더한다.
# *를 사용한 매개변수
# 입력값이 몇개가 될지 모를 때 사용한다.

# def add_many(*args):
#     # 튜플처럼 사용
#     # 인덱싱, 슬라이싱 가능
#     result = 0
#     for i in args:
#         result += i
#     return result
# result1 = add_many(1, 2, 3, 4, 5)
# print(result1)
# result2 = add_many(3, 2, 5, 9, 1)
# print(result2)
# result3 = add_many(1, 2)
# print(result3)


# def calc_many(n1, *args):    #(*args, n1) 처럼 순서를 바꿔서도 가능하다.
#     result = n1
#     for i in args:
#         result += i
#     return n1


# 키워드 매개변수
# **kwargs
# ketword arguments
# 딕셔너리로 사용

# def print_kwargs(**kwargs):
#     print(kwargs)

# print_kwargs(a=1, b=2)             # 방법1 결과 {'a': 1, 'b': 2}
# print_kwargs(name="이름", age=10)  # 방법2 결과 {'name': '이름', 'age': 10}

# 함수의 반환
# return 반환값
# return 을 만나면 반환값을 반환함과 동시에 함수가 종료 된다.

# def test_func5():
#     print(1)
#     print(2)
#     print(3)
#     return None
#     print(4)
#     print(5)
# test_func5()

# 함수의 반환값은 무조건 1개이다.
# def test_func6(a, b):
#    # return (a + b, a * b)
#     return a + b, a * b
# # print(test_func6(2,3))
# result = test_func6(1, 2)
# res_add, res_mul = test_func6(1, 2)
# # res_add, res_m;ul = (a+b, a*b)
# print(result)
# print(res_add, res_mul)



# 실습

# 홀수 판별 함수
# 정수 1개를 입력받고 홀수 인지 판별하는 함수
# 함수 이름 : is_odd_number
# 파라미터 : n
# 반환값 : 홀수면 Ture, 짝수면 False

# 방법 1
# n = int(input("정수:"))
# def is_odd_number(n):
#     if n % 2 != 0:
#         return True
#     else:
#         return False 
# a = is_odd_number(n)
# print(a)

# 방법 2
# def is_odd_number(n):
#     if n % 2 == 1:
#         return True
#     return False 
# a = is_odd_number(3)
# print(a)    


# 방법 3
# def is_odd_number(n):
#     return n % 2 == 1
# a = is_odd_number(3)
# print(a)


# 실습

# 테두리를 출력하는 함수
# 문자열을 입력받고 print 함수를 이용해 테두리와 함께 문자를 출력한다.
# 함수 이름 : get_bordered_str
# 파라미터 : message
# 반환값 : None

# print 예시

# *****
# hello
# *****

# def get_bordered_str(message):
#         n = len(message)
#         print("*" * n)
#         print(message)
#         print("*" * n)
# get_bordered_str("hello")        

# message = str(input("입력 : "))
# def get_bordered_str(message):
#         n = len(message) #len함수는 문자형을 체크한다.
#         print("*" * n)
#         print(message)
#         print("*" * n)
# # get_bordered_str("hello") 
# get_bordered_str(message) 


# 예제

# 속도를 변환하는 함수
# m/s단위의 속도가 입력되면
# km/h단위의 속도로 변환한다.
# 함수 이름 : convert_velocity
# 파라미터 : velocity
# 반환값 : km/h로 변환된 속도


    # 1초에 1m -> 1m/s
    # 1m/s로 1시간동안 가면 몇m?
    # 1m/s * 3600 (1시간)
    # 3600m/h
    # 1km는 몇 m? 1000m
    # 3600m/h  / 1000(1km)
    # 1m/s ==> 3.6km/h
    # 1m/s * 3600 / 1000 ==> 3.6km/h
    # 초속 * 3600 / 1000 ==> 시속
    # 초속 * 3.6 = 시속


# def convert_velocity(velocity):
#     result = velocity * 3.6
#     return result
# velocity = convert_velocity(10)
# print(velocity)



# 예제

# 별 찍기 함수
# 정수를 함수에 입력하여 호출하면
# 해당 정수 줄의 별을 화면에 출력한다.
# 함수 이름 : print_stars
# 파라미터 : n
# 반환값 : None
"""

출력결과 n -> 4 
*
**
***
****

출력결과 n -> 1
*

"""
# 방법 for문 사용

# n = int(input("숫자 : "))
# def print_stars(n):
#     for i in range(n): # 0 ~ n-1
#         for j in range(i+1): # 0 ~ i
#             print("*", end="")
#         print()
# print_stars(n)

# 방법 while문 사용
# n = int(input("숫자 : "))
# def print_stars(n):
#     i = 0
#     while i < n:
#         j = 0
#         while j < i+1:
#             print("*", end="")
#             j += 1
    
#         print()
#         i += 1
# print_stars(n)



# 방법 for문 + while문 사용
# n = int(input("숫자 : "))
# def print_stars(n):
#     for i in range(n):
#         j = 0
#         while j < i+1:
#             print("*", end="")
#             j += 1
#         print()
# print_stars(n)




# 구구단 2단부터 9단까지
# 이중 for문
# i = int(input("몇단 ? :"))
# for j in range(1, 10):
#         print( f" {i} * {j} = {i*j}" )
# print("-----------------")



# 별코드

# n = int(input("숫자? :"))
# for i in range(n):
#     print("*" * (i+1))

# 역별코드
# n = int(input("숫자? :"))
# for i in range(n, 0, -1):
#     print("*" * i)    

# 마름모 별코드
# n = int(input("숫자? :"))
# for i in range(n):
#     print(" " * (n-i-1) + "*" * (2*i+1))
# for i in range(n-2, -1, -1):
#     print(" " * (n-i-1) + "*" * (2*i+1)) 

# 정사각형 별코드
# n = int(input("숫자? :"))
# for i in range(n):
#     print("*" * n)


# word = ["school", "game", "piano", "science", "hotel", "mountain"]
# a = list()
# for i in range(len(word)):
#     if len(word[i])>=6:
#         a.append(word[i])
# print(a)

b = int(input('정수를 입력하세요.'))
if b<=0:
    print('음수는 정의하지 않음.')
else:    
    for a in range(1,b+1):
        if a%3==0 and a%5==0:
            print('3과 5의 공배수')
        elif a%3==0:
            print('3의 배수')
        elif a%5==0:
            print('5의 배수')
        elif 1<=a<=100:
            print(a)
        else:
            print('1과 100사이 숫자가 아닙니다.')