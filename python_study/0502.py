# p225

# 이 함수는 두개의 숫자를 input으로 받으면 작은 수로 큰수를 나눈 몫과 나머지를 반환하는 함수이다.

# 반환 값은 튜플로 되어 있으며 몫, 나머지 순으로 되어있다.

# 단, 0으로 나누는 것은 불가하기 때문에 두 수 중에 작은 수가 0이라면 화면에 0은 사용할 수 없습니다. 를 출력하고 종료되어야 한다.


# def div3(a,b):
#     if a<b:
#         big=b
#         small=a
#     elif b<=a:
#         big=a
#         small=b
#     else:
#         print('정수가 아닙니다.')
#     if small==0:
#         print('0은 사용할 수 없습니다.')
#     elif abs(big)<0 or abs(small)<0:
#         print('정수를 입력해주세요.')
#     else:
#         q = big//small
#         r = big%small
#         return (q,r)
# print(div3(10,1))

# p229
# 어떠한 string을 받으면 일정한 단위로 끊어서 화면에 출력하는 함수를 짜보자
# 끊는 단위는 따로 정하지 않으면 2로 설정해보자.
# Hint : input을 string과 unit = 2 로 받고 , while을 사용하고, 길이는 len함수를 사용하도록 하자.

# 정답 1
# def print_by_unit(string, unit=2):
#     idx = 0
#     while idx < len(string):
#         print(string[idx:idx+unit])
#         idx += unit
# print_by_unit("Hello, World!")


# 정답 2
# def func(string, unit=2):
#     i=0
#     while i<len(string):
#         print(string[i:i+unit])
#         i +=unit

# func('테스트를 위한 문장입니다.')


# p230
# add_all함수를 짜봅시다
# add_all(1,2,3,4,5,6,7,8,9,10)
# hint : *args를 input으로 받으세요

# 정답1
# def add_all(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     return result
# print(add_all(1,2,3,4,5,6,7,8))

# 정답2
def add_all3(*args):
    s=0
    for i in args:
        for j in i:
            s +=j
        return s
print(add_all3([1,2,3,4,5,6,7,8,9,10]))

# 정답3 (튜플, 리스트 모두 계산이 가능함)
# def add_all4(*args):
#     temp=0
#     for i in range(len(args)):
#         if type(args[i]) == list:
#             for j in args[i]:
#                 temp +=j
#         else :
#             temp +=args[i]
#     return temp
# print(add_all4([1,2,3,4,5,6,7,8,9,10]))  
# # print(add_all4(1,2,3,4,5,6,7,8,9,10))


# 팩토리얼(Factorial)을 구하시오
# 1부터 시작하여 어떤 범위에 있는 모든 정수를 곱하는 것.
# Ex) 5! = 120

# 정답1

# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
# print(factorial(5))

# 정답2
#재귀적으로 하지 않은 것.
# def fact(n):
#     f=1 #곱을 계산할 변수의 초깃값
#     for i in range(1,n+1): #1부터 n까지 반복
#         f = f*i #곱셈연산
#     return f
# print(fact(5))

# 정답3
#재귀적으로 하는 것.
# def fact1(n):
#     if n<=1: #n이 1이하이면 종료조건
#         return 1
#     return n*fact1(n-1)
# print(fact1(4))



# 함수는 사람이름으로 되어 있는 리스트를 받아서"대기번호x번:사람이름"를 화면에 출력하고 (번호표,사람이름)을 원소로 이루어진 리스트를 반환한다.
# input: 리스트
# output : 리스트

# 정답1
# people = ['펭수','뽀로로','뚝딱이','텔레토비']

# def func1(line):
#     new_lines = []
#     i=1
#     for x in line:
#         print('대기번호 %d번 : %s' %(i,x))
#         new_lines.append((i,x))
#         i +=1
#     return new_lines
# lines = func1(people)


# 정답2

# enumerate(열거하다) 반복 가능한 객체의 인덱스와 원소에 함께 접근할 수 있는 함수.

# people = ['펭수','뽀로로','뚝딱이','텔레토비']

# def func1(line):
#     new_lines = []
#     for idx,val in enumerate(line):
#         print('대기번호 %d번 : %s' %(idx,val))
#         new_lines.append((idx+1,val))
#     return new_lines
# lines = func1(people)


# zip 반복가능한 객체들을(2개 이상) 병렬적으로 묶어주는 함수. 각 원소들을 튜플의 형식으로 묶어줌.
# str_list = ['one','two','three','four']
# num_list = [1,2,3,4]

# for i in zip(num_list,str_list):
#     print(i)

# lambda : 한 줄을 실행한 결과 값이 바로 반환값이 됨.

# def plus_two(num):
#   return num + 2
# a = 2
# b = plus_two(a)
# print(b)


# func2 = lambda x : x + 2
# c = func2(2)
# print(c)


# MAP
# 리스트,튜플,스트링 등 자료형 각각의 원소에 동일한 함수를 적용

# items = [1, 2, 3, 4, 5]
# squared = []
# for i in items:
#   squared.append(i*i)
# print(squared)

# items = [1, 2, 3, 4, 5]
# squared1_map = list(map(lambda x : x**2, items))
# print(squared1_map)

# lambda와 map을 이용하여 items의 요소들을 string(문자)바꾸는 것을 짜봅시다.
# items = [1,24,3,6,7]
# str_items = list(map(lambda x:str(x),items))
# print(str_items)

# list comprehension
# 0~9까지를 순서대로 가지고 있는 리스트를 만드세요.
# #1.
# list_1 = [0,1,2,3,4,5,6,7,8,9]
# #2.
# list_2 = []
# for x in range(10):
#     list_2.append(x)
# print(list_2)

# lc_1 = [x for x in range(10)]
# print(lc_1)

#구구단 2단을 list comprehension을 이용하여 구현하고 리스트를 화면에 출력해보자
#1) 구구단 2단
# tables = [2 *x for x in range(1,10)]
# print(tables)

# "코로나 바이러스를 예방ㅎ하기 위해 사회적 거리두기를 실천합니다.마스크를 끼고 손씻기를 생활화합시다." 라는 문자을 띄어쓰기별
# 로 분석하려고 한다. 띄어쓰기별로 문장을 나눈 후각요소의 길이를 리스트에 저장하라 (hint : 띄어쓰기를 spit함수를 써라)  

#2) 코로나 바이러스
# sentence = '코로나 바이러스를 예방하기 위해 사회적 거리두기를 실천합시다. 외출 시에는 마스크를 끼고, 손씻기를 생활화합시다.'
# print(sentence)


# for 문+if 문
# -10부터 20까지의 숫자들 중에서 짝수만을 담은 리스트를 만들어보자!
# list3 = []
# for x in range(10,21):
#     if x%2==0:
#         list3.append(x)
# print(list3)

# lc_2 = [x for x in range(10,21) if x%2==0]
# print(lc_2)

# 1부터 10의 제곱수 중 50 이하인 수만 리스트에 저장하라
#1)
# lc_3 = [x**2 for x in range(1,11) if x**2<50]
# print(lc_3)

# "코로나 바이러스를 예방하기 위해 사회적거리두기를 실천합시다. 마스크를 끼고 손씻기를 생활화합시다."라는 문장을 띄어쓰기별로 분석
# 하려고 한다. 띄어쓰기별로 문장을 나눈 후 각 요소의 길이가 5미만인것들만 리스트에 저장하라.
# sentence = '코로나 바이러스를 예방하기 위해 사회적 거리두기를 실천합시다. 외출 시에는 마스크를 끼고, 손씻기를 생활화합시다.'
# lc_4 = [s for s in sentence.split() if len(s) <5]
# print(lc_4)


# 1부터 10까지의 숫자들 중 홀수이면 제곱수를,짝수이면 세제곱수를 담은 리스트를 만들어보자

# 방법1

# list_4 = []
# for x in range(1,11):
#     if x%2==1:
#         list_4.append(x**2)
#     else :
#         list_4.append(x**3)
# print(list_4)

# # 방법2
# list_10 = [x**2 if x%2==0 else x**3 for x in range(1,11)]
# print(list_10)    


# 40이하의 숫자는 5을 더하고, 40 초과의 숫자는 41로 바꾸어 리스트로 저장하고 리스트를 출력하라.

# 방법1
# list_5 = [12,67,32,48,19,57,29,49]
# lc_6 = [x+5 if x<=40 else 41 for x in list_5]
# print(lc_6)


# 컷트라인이 60점일때 사람이름과 통과여부를 리스트로 담아서 출력하라. 이름과 통과여부는 튜플로 묶어 있는 자료이다.

# 방법1
# students = {"보라돌이":61, "뚜비":35, "나나":78,"뽀":88}
# result = [(name,"합격") if score>60 else (name, "불합격")for name,score in students.items()]
# print(result)


# 백터화
# - 배열은 for문을 작성하지 않고 데이터를 일괄처리 하는것.

# import numpy as np
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr)


# print(10-arr) # 빼기
# print(arr * 3) # 곱하기
# print(arr / 3) # 나누기

# import numpy as np
# arr2 = np.array([100,200,300])
# print(arr2)


# import numpy as np
# arr3 = np.array([100,200])
# print(arr3 )


# list_1 = [1,2,3]
# print(list_1 + list_1 ) # 리스트 + 리스트 ( 결과 : [1, 2, 3, 1, 2, 3] )

# import numpy as np
# arr_1 = np.array([1,2,3]) #np.arrat 사용 (리스트끼리 더하기 , 결과 [2 4 6] )
# print(arr_1 + arr_1)


# dtype (배열에 담긴 원소의 자료형(ndarray는 같은 자료형을 담음.)

# import numpy as np
# arr = np.array([[1,2,3],[4,5,6]]) # 2행 3열
# print(arr)

# import numpy as np
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr.size) # 결과 6
# print(arr.shape) # 결과 (2,3)

# 0차원(상수)
# import numpy as np
# a = np.array(10)
# print(a)
# print(a.ndim) # 결과 0 (0차원뜻) --> 괄호안에 대괄호 0개


# 1차원
# import numpy as np
# a = np.array([1,2,3])
# print(a)
# print(a.ndim) # 결과 1 (1차원뜻) --> 괄호안에 대괄호 1개

# 2차원
# import numpy as np
# a = np.array([[1,2],[4,5]])
# print(a)
# print(a.ndim) # 결과 2 (2차원뜻) --> 괄호안에 대괄호 2개

# import numpy as np
# a = np.array([[[1,2],[3,4]]])
# print(a)
# print(a.ndim)  # 결과 3 (3차원뜻) --> 괄호안에 대괄호 3개
# print(a.shape) # (1, 2, 2)   


# 1번
# import numpy as np
# arr1 = np.array(range(20)) 
# print(arr1)

# 2번 
# import numpy as np
# arr2 = np.arange(20)
# print(arr2)

# 1번과 2번의 결과값이 같다. ( 결과 : [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19] )


# zeros
# import numpy as np
# print(np.zeros(5)) # 결과 [0. 0. 0. 0. 0.]

# import numpy as np
# print(np.ones((3,3)))

# import numpy as np
# print(np.full((4),5))


# import numpy as np
# print(np.empty((2,3),dtype=np.float32))

# import numpy as np
# print(np.arange(-3,3))

# import numpy as np
# print(np.arange(3,50,3))

# import numpy as np
# print(np.linspace(0,1,6))

# -----------------------------------------------



# - 배열 결합 함수.
#     - hstack, concatenate(axis=0)
#     - 두 배열을 왼쪽에서 오른쪽으로 붙이기.
# import numpy as np
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(np.hstack([a,b]))
# print(np.concatenate((a,b),axis=0))

# import numpy as np
# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])
# print(np.hstack([a,b]))
# print(np.concatenate((a,b),axis=0))

# vstack(vertical), concatenate(axis=1)

# import numpy as np
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(np.vstack([a,b]))
# np.concatenate((a,b),axis=1) #1D vector는 안됨.

# import numpy as np
# c = np.array([[0,1,2],[3,4,5]])
# d = np.array([[6,7,8],[9,10,11]])
# print(np.concatenate((c,d),axis=1))

#  - 두 배열을 위 아래로 붙이기.
# import numpy as np
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(a,b)  # 나란히 붙이기
# print(np.column_stack([a,b])) # 위아래로 붙이기


# import random
# import numpy as np
# print(random.random()) #<=리턴값<=1



# import random
# import numpy as np
# data = [1,2,3,4,5,6,7]

# print(np.random.choice(data,3))



# import random
# import numpy as np
# data = ['apple','banana','grape','orange']

# print(random.choice(data))

# - seed
    # - 난수 초기값 부여-> 재현 가능성(Reporducibility)

# import random
# import numpy as np
# print(np.random.seed(42))
# print(np.random.rand(1000))
# print(np.random.randn(1000)) #정규분포

# 로또 번호 생성기

# 방법1

# import numpy as np

# # 게임수 입력 받기
# num_games = int(input("몇 개의 로또 번호를 생성하시겠습니까? "))

# # 1부터 45까지의 숫자를 포함하는 배열 생성
# numbers = np.arange(1, 46)

# # 입력받은 게임수만큼 로또 번호 생성 후 출력
# for i in range(num_games):
#     # 6개의 숫자를 무작위로 선택하여 배열로 저장
#     lotto = np.random.choice(numbers, size=6, replace=False)

#     # 생성된 로또 번호를 정렬하여 출력
#     print("로또 번호 {}: {}".format(i+1, np.sort(lotto)))

# 방법2 

# import numpy as np
# def make_lotto(count):
#     for i in range(count):
#         lotto_num = [] #로또 번호가 담길 리스트형 변수
#         for j in range(6): #6번 반복
#             lotto_num = np.random.choice(range(1,46),6,replace=False)
#             lotto_num.sort() #값 정렬
#         print('{}.로또번호:{}'.format(i+1,lotto_num)) 
# count = int(input('로또 번호를 몇개 생성할까요?'))
# make_lotto(count)  