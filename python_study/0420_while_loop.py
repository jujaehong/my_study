# while ( ~동안 ) 반복문
"""
while 조건 :
    반복할 코드
"""
# 조건이 참인 경우에 코드를 걔속 반복
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)


# n = 1
# while n <= 10: # 반복하다 조건과 맞지 않으면  False 이므로 다음 으로 넘어간다. 
#     print(n)
#     n += 1     # n = n+1 실행후 다시 while로 간다.(반복)

# 대입 연산자
# 더하기 연산 후 할당
# n += 1은 n = n+1이라는 의미

# += 연산자
# -= 빼기 반복
# *= 곱하기 반복
# /= 나누기 반복
# **= 제곱 반복
# //= 정수나누기 반복
# %= 몫나누기 반복

# s1 = "안녕"
# s1 += "하세요" # s1 = s1 + "하세요" 와 같은 의미

# while 반복문을 활용하여
# 10부터 1까지 순서대로 출력하세요.

# cnt = 10
# while cnt >= 1:
#     print(cnt)
#     cnt -= 1


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


# while 반복문을 활용하여
# 1부터 10까지 홀수만 출력한다.
# a = 1
# while a <= 10:
#     if a % 2 == 1:
#         print(a)
#     a += 1


# continue
# 반복문의 제일 처음으로 돌아감

# 1부터 10까지 홀수 출력
# b = 0
# while b <= 9:
#     b += 1
#     if b % 2 == 0:
#         continue
#     print(b)

# 무한 반복문
# 무한 루프
# 조건식에 True를 입력해 항상
# 참이 되도록 하여 무한히
# 반복하게 한다.

# while True: 
#     user_input = input("종료하려면 1을 입력해주세요.")
#     if user_input == "1":
#         break

# 강제종료 컨트롤 + c


# 무한반복문으로 계산기 만들기
# +, -, *, / 계산
# 2개의 수를 계산 a + b


# input 데이터 타입까지 같아야 한다. 문자 = 문자 , 숫자 = 숫자
# while True:
#     print("""
#         계산기
#     ============
#     1. 더하기 (+
#     2. 빼기 (-)
#     3. 곱하기 (*)
#     4. 나누기(/)
#     """)
#     operator = input("계산을 선택하세요 : ")

#     if operator  == "1":
#         print("1 + 2 =" , 1 + 2)

#     if operator == "2":
#         print("1 - 2 =" , 1 - 2)

#     if operator == "3":
#         print("1 * 2 =" , 1 * 2)

#     if operator == "4":
#         print("1 / 2 =" , 1 / 2)

# 코드를 수정해서 사용자가 입력한 숫자를
# 계산하도록 변경하시오.
# q를 입력하면 종료되도록 변경하세요.

# while True:
#     print("""
#         계산기
#     ============
#     1. 더하기 (+
#     2. 빼기 (-)
#     3. 곱하기 (*)
#     4. 나누기(/)
#     """)
#     operator = input("계산을 선택하세요 : ")
#     a = int(input("숫자"))
#     b = int(input("숫자"))
#     # q = input("종료하시겠습니까?")

#     if operator  == "1":
#         print(a, "+", b, "=" , a + b)

#     if operator == "2":
#         print(a, "-", b, "=" , a - b)

#     if operator == "3":
#         print(a, "*", b, "=" , a * b)

#     if operator == "4":
#         print(a, "/", b, "=", a / b)
    
#     if operator == "q":
#        break
    


# 사용자가 가지고 있는 돈을 입력 받는다.
# 구매할 수 있는 커피의 개수와 잔돈을 출력한다.
# 구매할 수 있는 음료수의 개수와 잔도을 출력한다.
# 구매할 수 있는 콜라의 개수와 잔돈을 출력한다.
# 커피는 500원 음료수는 700원 콜라는  930원
# 물품의 개수는 무한하다고 가정한다.
# while 반복문을 사용하여 작성한다.

# idx = 0
# prices = [500, 700, 930]
# money = int(input("돈:"))

# while idx <= len(prices):
#     price = prices[idx]
#     print(money // price)
#     print(money % price)
#     idx += 1




# while 반복문을 사용해서
# scores 리스트에 시험 점수 5개를 
# 정수형으로 입력받으세요.

# scores = []
# n = 0
# while n < 5:
    # score = int(input("시험점수:"))
    # scores.append(score)
    # n += 1
# print(scores) # 점수 5개 모두 입력시 한번에 출력
    # print(scores) # 점수 입력때마다 출력


# for 반복문을 사용해서
# scores 리스트에 시험 점수 5개를 
# 정수형으로 입력받으세요.
# scores = []
# for i in range(0,5):
#     score = int(input("시험 점수를 입력하세요: "))
#     scores.append(score)
# print(scores)


    # while 반복문을 사용하여
    # 구구단 2단을 출력하세요.

# n = 1
# while n < 10:
#     print("2 *", n, "=", 2*n)
#     n += 1





