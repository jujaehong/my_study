# tuple(튜플)형
# 튜플은 element의 값을
# 수정할 수 없다.
# mutable / immutable
# mutable 수정 가능한 # 바인딩을 바꿀 수 있다. # 마음대로 바꿀 수 있다.
# list, dict
# immutable 수정 불가능 # 바인딩을 바꿀 수 없다. # 자리가 확정
# int, float, str, tuple

# list 값 바꾸기
# my_list = [1, 2, 3] #순서1
# my_list[0] = 5      #순서2
# print(my_list)      #순서3 결과는 [5, 2, 3]  

# tuple 값 바꾸기 (튜플형은 수정 불가능)
# my_tuple = (1, 2, 3)
# my_tuple[0] = 5       
# print(my_tuple)       # TypeError: 'tuple' object does not support item assignment 에러발생

# 튜플은 리스트와 동일하게 사용하나 수정이나 삭제가 안됨.
tuple_1 = ("Hello","World","python") 
t2 = (1, 2, 3, 4, 5)
t3 = (1, 2, "Hello")
t4 = 1, 2, 3
t5 = (1,2, (3,4,5))

t6 = tuple_1 + t2 # 연산이 된다. (이어붙이기)
print(t6) # 결과 : ('Hello', 'World', 'python', 1, 2, 3, 4, 5)

t7 = t3 * 3
t7 = t3 * 4 
print(t7)     # 결과 : (1, 2, 'Hello', 1, 2, 'Hello', 1, 2, 'Hello', 1, 2, 'Hello')

print(t3[2])
print(t3[0:2]) # 결과 : (1, 2) [슬라이싱을 하면 묶여져있는 구조로 가져옴 (튜플형-수정안됨)]
print(len(t3))

print(t5[2][1]) #결과 : 4


t8 = (5, 3, 1, 4, 2)  # 튜플형이므로 차순정렬이 안된다. ( 리스트형에서 사용하던 sort같은 함수 사용 안됨.)
for i in t8:
    print(i) # 결과는 인덱스 순으로 출력된다.