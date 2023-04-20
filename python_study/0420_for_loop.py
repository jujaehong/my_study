# for문 
# iterable (이터러블:순회가능하다)
"""
for 변수 in iterable값: 
    반복할 코드
"""
# li_1 = ["one", "two", "three"]
# for i in li_1:  # i 는 변수
#     print(i)

# 첫번째 요소부터 마지막 요소까지
# 변수에 대입하면서 반복
# 무한반복은 while에서만 됨.

# s1 = "hello"
# for i in s1:
#     print(i)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# for number in numbers:
#     print(number)

# numbers.reverse()
# for number in numbers:
#     print(number)

# range() 
# 숫자 range 객체를 만들어주는 함수

# range(끝 정수)
# 0 ~ 끝 정수 -1
# for i in range(10): # 0 ~  9 까지 출력
#     print(i)

# range(시작,끝)
# 시작 ~ 끝 -1
# for i in range(1,11):
#     print(i)

# range(시작,끝,스텝)
# 시작 ~ 끝 -1 까지인데 스템만큼 차이나게
# for i in range(1,21,3):
#     print(i)

# for문을 사용하여 2부터 30까지 출력해보세요.
# for i in range(2,31):
#     print(i)

# for문을 사용하여 2부터 30까지 숫자 중
# 짝수만 출력해보세요.

# 방법1
# for i in range(2,31,2):
#         print(i)

# 방법2
# for i in range(2,31):
#     if i % 2 == 1: # 홀수
#         # continue
#         pass # 아무것도 안하고 그냥 넘어갈때
#     else: # 짝수
#         print(i)

# 방법3
# for i in range(2,31):
#     if i % 2 == 0:
#                print(i)


# for문을 사용하여 10부터 1까지 출력해보세요

# 방법1
# for i in range(10,0,-1): #(10 ,0, -1) range에서 앞자리는 포함, 두번째자리는 미포함 
#             print(i)

# 방법2
# for i in reversed(range(1,11)): 
#         print(i)   

# 방법3
# for i in range(1,11)[::-1]:
#     print(i)
# 슬라이싱 [시작인덱스:끝인덱스:방향] 여기서 방향을 -1을 주면 거꾸로 방향이 된다.



# while문을 for문으로 바꾸기

# money = 10000
# price = 1000
# coffee = 5 #커피수량
# while money >= price:
# # while money - price >= 0:
#     print("커피를 구매했습니다.")
#     money -= price
#     coffee -= 1
#     print("남은커피 :", coffee)
#     if coffee == 0:
#         break

# break
# 반복문을 즉시 종료한다.

# # 방법1)
# money = 10000
# price = 1000
# coffee = 5 #커피수량
# for i in range(coffee): # 0 ~ 4
#     print("커피를 구매했습니다.")
#     money -= price # money = money - price
# print("남은 커피:",coffee - 1 - i)

# # 방법2)
# money = 10000
# price = 1000
# coffee = 5 #커피수량
# for i in range(1, coffee +1):  # 1 ~ 4
#     print("커피를 구매했습니다.")
#     money -= price # money = money - price
# print("남은 커피:",coffee - i)  # 4 ~ 0

# # 방법3)
# money = 10000
# price = 1000
# coffee = 5 #커피수량
# for i in range(coffee):
#     print("커피를 구매했습니다.")
#     money -= price # money = money - price
#     coffee -= 1 
# print("남은 커피:",coffee)  # 4 ~ 0 


# break 함수 사용
# money = 2000
# price = 1000
# coffee = 5 #커피수량
# for i in range(coffee): # 0 ~ 4
#     print("커피를 구매했습니다.")
#     money -= price # money = money - price
#     print("남은 커피:",coffee - 1 - i)
#     if money < price:
#         break

# ----------------------------------------------------------

# while는 특정조건식을 체크하면서 반복할때 유용하다.
# 횟수가 정해져 있을때는 for문을 사용하는것이 유용하다.
# ----------------------------------------------------------

# # while 문과 비교
# idx = 0
# prices = [500, 700, 930]
# money = int(input("돈:"))

# while idx <= len(prices):
#     price = prices[idx]
#     print(money // price)
#     print(money % price)
#     idx += 1

# # 위 while문을 for로 바꾸기

# prices = [500, 700, 930]
# money = int(input("돈:"))
# for i in range(len(prices)):
#     price = prices[i]
#     print(money // price)
#     print(money % price)


# # 위 for문 보다 더 유용한방법

# prices = [500, 700, 930]
# money = int(input("돈:"))
# for price in prices:
#     print(money // price)
#     print(money % price)

# # 다른에제

# scores = []
# for i in range(5):    # 5번 반복하겠다 의미
#     score = int(input("시험점수:"))
#     scores.append(score)
 

# #구구단 2단
# for i in range(1,10):   # 1 ~ 9
#     print("2 *", i, "=", 2*i)


# # 구구단 2단부터 9단까지
# 이중 for문
# for i in range(2,10): # 2 ~ 9
#     print(i, "단")
#     for j in range(1,10): # 1 ~ 9   # 안쪽 for문이 먼저 바뀐다.
#         print(i,"*",j, "=", i*j)
#     print("-----------------")


