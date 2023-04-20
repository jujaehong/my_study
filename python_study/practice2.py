# li_1 = ["Hello", "World", "Python"]
# li_1의 원소를 사용하여
# Hello World Python 이라고 출력하세요.
# print(li_1[0], li_1[1], li_1[2])

# join(리스트)
# 리스트의 문자열을 합친다.
# print(" ".join(li_1))

# print(li_1[0] + " " + li_1[1] + " "+ li_1[2])


# li_1의 원소를 사용하여
# Help라고 출력하세요.
# print(li_1[0][0:3] + li_1[2][0]) # 정답 예1
# print(li_1[0][0] + li_1[0][1] + li_1[0][2] + li_1[2][0]) #정답 예2

# li_2 = [1, 2, 3]
# li_1과 li_2를 사용하여
# ["Hello", "World", "Python, 1, 2, 3"] 
# 를 출력하세요.

# print(li_1 + li_2) # 정답 예1

# li_1.extend(li_2) #정답 예2
# print(li_1)

# li_1과 li_2를 사용하여
# [Hello", 1, "World", 2, "Python", 3]
# 를 출력하세요

# li_1.insert(1,li_2[0]) # 정답 예1
# li_1.insert(3,li_2[1])
# li_1.insert(5,li_2[2])
# print(li_1)

# li_1.insert(1,li_2[0]) #정답 예2
# li_1.insert(3,li_2[1])
# li_1.append(li_2[2])
# print(li_1)


"""
eng 변수, kor 변수, math 변수를 만들고
각 변수는 과목의 시험 점수이다.
영어 점수는 80점
국어 점수는 60점
수학 점수는 50점
3과목 점수에 따라 성적을 출력한다.
A : 91 ~ 100
B : 81 ~ 90
C : 71 ~ 90
D : 61 ~ 70
F : 60 이하
"""


# scores = []
# scores = list() # 비어있는 리스트 생성
# scores.append(int(input("영어 점수:")))
# scores.append(int(input("국어 점수:")))
# scores.append(int(input("수학 점수:")))

# avg = (scores[0] + scores[1] + scores[2]) / 3 # 정답예1
# sum()
# 리스트의 요소를 모두 더한다.
# avg = sum(scores) / 3                           # 정답예2  



# if avg >= 91:
#     print("A")
# elif avg >= 81:
#     print("B")
# elif avg >= 71:
#     print("C")
# elif avg >= 61:
#     print("D")
# else:
#     print("F")

# input() 함수
# 정보를 입력받는 함수
# user_input = input()
# print (user_input)

# 정수형 변환 함수
# 정수형, integr형, int형
# int(값)




# 나이와 가지고 있는 돈을 입력받는다.
# 가지고 있는 돈으로 물건을 
# 몇개 살 수 있는지와 잔돈을 출력한다.
# 물건의 가격은 500원이다.

# age = int(input("당신의 나이는?"))
# money = int(input("얼마 있어요?"))
# price = 500

# buy = money // price
# cha = money % price

# print("구매", int(buy),"거스름돈", int(cha))

# 나이와 가지고 있는 돈을 입력받는다
# 가지고 있는 돈으로 물건별로 각각
# 몇 개 살 수 있는지와 잔돈을 출력한다.
# 물건의 가격은 1번 물건 1000원
# 2번 물건 50원 3번 물건 120원이다.

# age = int(input("당신의 나이는?"))
# money = int(input("얼마 있어요?"))
# prices = [1000, 50, 120]

# print(money // prices[0],"개", money % prices[0],"원")
# print(money // prices[1],"개", money % prices[1],"원")
# print(money // prices[2],"개", money % prices[2],"원")
